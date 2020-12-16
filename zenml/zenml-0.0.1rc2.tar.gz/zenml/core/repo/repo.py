#  Copyright (c) maiot GmbH 2020. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
"""Base ZenML repository"""

import os
from pathlib import Path
from typing import Text, List, Dict, Any, Optional, Union, Type

from zenml.core.metadata.metadata_wrapper import ZenMLMetadataStore
from zenml.core.repo.artifact_store import ArtifactStore
from zenml.core.repo.git_wrapper import GitWrapper
from zenml.core.repo.global_config import GlobalConfig
from zenml.core.repo.zenml_config import ZenMLConfig
from zenml.core.standards import standard_keys as keys
from zenml.utils import path_utils, yaml_utils
from zenml.utils.enums import PipelineStatusTypes
from zenml.utils.logger import get_logger
from zenml.utils.zenml_analytics import track, CREATE_REPO, GET_PIPELINES, \
    GET_DATASOURCES, GET_PIPELINE_ARTIFACTS, GET_STEPS_VERSIONS, \
    REGISTER_PIPELINE, GET_STEP_VERSION

logger = get_logger(__name__)


class Repository:
    """ZenML repository definition. This is a Singleton class.

    Every ZenML project exists inside a ZenML repository.
    """
    __instance__ = None

    def __init__(self, path: Text = None):
        """
        Construct reference a ZenML repository

        Args:
            path (str): Path to root of repository
        """
        if Repository.__instance__ is None:
            if path is None:
                try:
                    # Start from cwd and traverse up until find zenml config.
                    path = Repository.get_zenml_dir(os.getcwd())
                except Exception:
                    # If there isnt a zenml.config, use the cwd
                    path = os.getcwd()

            if not path_utils.is_dir(path):
                raise Exception(f'{path} does not exist or is not a dir!')
            self.path = path

            # Hook up git, path needs to have a git folder.
            self.git_wrapper = GitWrapper(self.path)

            # Load the ZenML config
            try:
                self.zenml_config = ZenMLConfig(self.path)
            except AssertionError:
                # We allow this because we of the GCP orchestrator for now
                self.zenml_config = None

            Repository.__instance__ = self
        else:
            raise Exception("You cannot create another Repository class!")

    @staticmethod
    def get_zenml_dir(path: Text):
        """
        Recursive function to find the zenml config starting from path.

        Args:
            path (str): starting path
        """
        if ZenMLConfig.is_zenml_dir(path):
            return path

        if path_utils.is_root(path):
            raise Exception(
                'Looks like you used ZenML outside of a ZenML repo. '
                'Please init a ZenML repo first before you using '
                'the framework.')
        return Repository.get_zenml_dir(Path(path).parent)

    @staticmethod
    def get_instance(path: Text = None):
        """ Static method to fetch the current instance."""
        logger.debug('Repository instance fetched.')
        if not Repository.__instance__:
            Repository(path)
        return Repository.__instance__

    @staticmethod
    @track(event=CREATE_REPO)
    def init_repo(repo_path: Text, artifact_store_path: Text = None,
                  metadata_store: Optional[ZenMLMetadataStore] = None,
                  pipelines_dir: Text = None,
                  analytics_opt_in: bool = None):
        """
        Initializes a git repo with zenml.

        Args:
            repo_path (str): path to root of a git repo
            metadata_store: metadata store definition
            artifact_store_path (str): path where to store artifacts
            pipelines_dir (str): path where to store pipeline configs.
            analytics_opt_in (str): opt-in flag for analytics code.

        Raises:
            InvalidGitRepositoryError: If repository is not a git repository.
            NoSuchPathError: If the repo_path does not exist.
        """
        # check whether its a git repo by initializing GitWrapper
        GitWrapper(repo_path)

        # use the underlying ZenMLConfig class to create the config
        ZenMLConfig.create_config(
            repo_path, artifact_store_path, metadata_store, pipelines_dir)

        # create global config
        global_config = GlobalConfig.get_instance()
        if analytics_opt_in is not None:
            global_config.set_analytics_opt_in(analytics_opt_in)

    def get_artifact_store(self) -> Optional[ArtifactStore]:
        if self.zenml_config:
            return self.zenml_config.get_artifact_store()

    def get_metadata_store(self):
        if self.zenml_config:
            return self.zenml_config.get_metadata_store()

    def get_git_wrapper(self) -> GitWrapper:
        if self.zenml_config:
            return self.git_wrapper

    @track(event=GET_STEP_VERSION)
    def get_step_by_version(self, step_type: Union[Type, Text], version: Text):
        """
        Gets a Step object by version. There might be many objects of a
        particular Step registered in many pipelines. This function just
        returns the first configuration that it matches.

        Args:
            step_type: either a string specifying full path to the step or a
            class path.
            version: either sha pin or standard ZenML version pin.
        """
        from zenml.utils import source_utils
        from zenml.core.steps.base_step import BaseStep

        type_str = source_utils.get_module_path_from_class(step_type)

        for file_path in self.get_pipeline_file_paths():
            c = yaml_utils.read_yaml(file_path)
            for step_name, step_config in c[keys.GlobalKeys.STEPS].items():
                # Get version from source
                class_ = source_utils.get_class_path_from_source(
                    step_config[keys.StepKeys.SOURCE])
                source_version = source_utils.get_version_from_source(
                    step_config[keys.StepKeys.SOURCE])

                if class_ == type_str and version == source_version:
                    return BaseStep.from_config(step_config)
        raise Exception(f'Step Type {type_str} does not exist with version '
                        f'{version}!')

    def get_step_versions_by_type(self, step_type: Union[Type, Text]):
        """
        List all registered steps in repository by step_type.

        Args:
            step_type: either a string specifying full path to the step or a
            class path.
        """
        from zenml.utils import source_utils
        type_str = source_utils.get_module_path_from_class(step_type)

        steps_dict = self.get_step_versions()
        if type_str not in steps_dict:
            raise Exception(f'Type {type_str} not available. Available types: '
                            f'{list(steps_dict.keys())}')
        return steps_dict[type_str]

    @track(event=GET_STEPS_VERSIONS)
    def get_step_versions(self):
        """List all registered steps in repository"""
        from zenml.utils import source_utils
        steps_dict = {}
        for file_path in self.get_pipeline_file_paths():
            c = yaml_utils.read_yaml(file_path)
            for step_name, step_config in c[keys.GlobalKeys.STEPS].items():
                # Get version from source
                version = source_utils.get_version_from_source(
                    step_config[keys.StepKeys.SOURCE])
                class_ = source_utils.get_class_path_from_source(
                    step_config[keys.StepKeys.SOURCE])

                # Add to set of versions
                if class_ in steps_dict:
                    steps_dict[class_].add(version)
                else:
                    steps_dict[class_] = {version}
        return steps_dict

    def get_datasource_by_name(self, name: Text) -> List:
        """
        Get all datasources in this repo.

        Returns: list of datasources used in this repo
        """
        all_datasources = self.get_datasources()
        for d in all_datasources:
            if name == d.name:
                return d
        raise Exception(f'Datasource {name} does not exist')

    def get_datasource_names(self) -> List:
        """
        Get all datasources in this repo.

        Returns: List of datasource names used in this repo.
        """
        n = []
        for file_path in self.get_pipeline_file_paths():
            c = yaml_utils.read_yaml(file_path)
            n.append(c[keys.GlobalKeys.DATASOURCE][keys.DatasourceKeys.NAME])
        return list(set(n))

    @track(event=GET_DATASOURCES)
    def get_datasources(self) -> List:
        """
        Get all datasources in this repo.

        Returns: list of datasources used in this repo
        """
        from zenml.core.datasources.base_datasource import BaseDatasource

        datasources = []
        for file_path in self.get_pipeline_file_paths():
            c = yaml_utils.read_yaml(file_path)
            datasources.append(BaseDatasource.from_config(c))
        return datasources

    def get_pipeline_by_name(self, pipeline_name: Text = None):
        """
        Loads a pipeline just by its name.

        Args:
            pipeline_name (str): Name of pipeline.
        """
        from zenml.core.pipelines.base_pipeline import BasePipeline
        yamls = self.get_pipeline_file_paths()
        for y in yamls:
            n = BasePipeline.get_name_from_pipeline_name(y)
            if n == pipeline_name:
                c = yaml_utils.read_yaml(y)
                return BasePipeline.from_config(c)
        raise Exception(f'No pipeline called {pipeline_name}')

    def get_pipelines_by_type(self, type_filter: List[Text]) -> List:
        """
        Gets list of pipelines filtered by type.

        Args:
            type_filter (list): list of types to filter by.
        """
        pipelines = self.get_pipelines()
        return [p for p in pipelines if p.pipeline_type in type_filter]

    def get_pipeline_names(self) -> Optional[List[Text]]:
        """Gets list of pipeline (unique) names"""
        from zenml.core.pipelines.base_pipeline import BasePipeline
        yamls = self.get_pipeline_file_paths(only_file_names=True)
        return [BasePipeline.get_name_from_pipeline_name(p) for p in yamls]

    def get_pipeline_file_paths(self, only_file_names: bool = False) -> \
            Optional[List[Text]]:
        """Gets list of pipeline file path"""
        pipelines_dir = self.zenml_config.get_pipelines_dir()

        if not path_utils.is_dir(pipelines_dir):
            return []
        return path_utils.list_dir(pipelines_dir, only_file_names)

    def get_pipelines_by_datasource(self, datasource):
        """
        Gets list of pipelines associated with datasource.

        Args:
            datasource (BaseDatasource): object of type BaseDatasource.
        """
        from zenml.core.pipelines.base_pipeline import BasePipeline
        pipelines = []
        for file_path in self.get_pipeline_file_paths():
            c = yaml_utils.read_yaml(file_path)
            if c[keys.GlobalKeys.DATASOURCE][keys.DatasourceKeys.ID] == \
                    datasource._id:
                pipelines.append(BasePipeline.from_config(c))
        return pipelines

    @track(event=GET_PIPELINES)
    def get_pipelines(self) -> List:
        """
        Gets list of all pipelines.

        Args:
            type_filter (list): list of types to filter by.
        """
        from zenml.core.pipelines.base_pipeline import BasePipeline
        pipelines = []
        for file_path in self.get_pipeline_file_paths():
            c = yaml_utils.read_yaml(file_path)
            pipelines.append(BasePipeline.from_config(c))
        return pipelines

    def get_hyperparameters(self):
        """
        Hyper-parameter list of all pipelines in repo
        """
        pass

    @track(event=GET_PIPELINE_ARTIFACTS)
    def get_artifacts_uri_by_component(self, pipeline_name: Text,
                                       component_name: Text):
        """
        Gets the artifacts of any component within a pipeline. All artifacts
        are resolved locally, even if artifact store is remote.

        Args:
            pipeline_name (str): name of pipeline
            component_name (str): name of component
        """
        # mlmd
        metadata_store = self.get_metadata_store()
        status = metadata_store.get_pipeline_status(pipeline_name)
        if status != PipelineStatusTypes.Succeeded.name:
            AssertionError('Cannot retrieve as pipeline is not succeeded.')
        # if component_name not in GDPCOmponents:
        #     raise AssertionError('Component must be one of {}')
        artifacts = metadata_store.get_artifacts_by_component(pipeline_name,
                                                              component_name)

        # Download if not local
        uris = []
        for a in artifacts:
            artifact_store = self.get_artifact_store()
            uris.append(artifact_store.resolve_uri_locally(a.uri))

        return uris

    def get_hyperparameters_pipeline(self):
        pass

    @track(event=REGISTER_PIPELINE)
    def register_pipeline(self, file_name: Text, config: Dict[Text, Any]):
        """
        Registers a pipeline in the artifact store as a YAML file.

        Args:
            file_name (str): file name of pipeline
            config (dict): dict representation of ZenML config
        """
        pipelines_dir = self.zenml_config.get_pipelines_dir()

        # Create dir
        path_utils.create_dir_if_not_exists(pipelines_dir)

        # Write
        yaml_utils.write_yaml(os.path.join(pipelines_dir, file_name), config)

    def load_pipeline_config(self, file_name: Text) -> Dict[Text, Any]:
        """
        Loads a ZenML config from YAML.

        Args:
            file_name (str): file name of pipeline
        """
        pipelines_dir = self.zenml_config.get_pipelines_dir()
        return yaml_utils.read_yaml(os.path.join(pipelines_dir, file_name))

    def compare_pipelines(self):
        pass
