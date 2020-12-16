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

import os

from zenml.utils.version import __version__


def handle_bool_env_var(var, default=False):
    """Converts normal env var to boolean"""
    var = os.getenv(var, None)
    for i in ['1', 'y', 'yes', 'True', 'true']:
        if i == var:
            return True
    return default


# Global constants
APP_NAME = 'zenml'
CONFIG_VERSION = '1'

# Environment variables
ZENML_PIPELINE_CONFIG = 'ZENML_PIPELINE_CONFIG'
CE_CLOUD_JOB_PREFIX = 'CE_CLOUD_JOB_PREFIX'
ENV_ZENML_DEBUG = 'ZENML_DEBUG'

# Logging variables
ENV_ZENML_LOGGING_VERBOSITY = 'ZENML_LOGGING_VERBOSITY'
# TODO: [HIGH] Switch to default False before release
IS_DEBUG_ENV = handle_bool_env_var(ENV_ZENML_DEBUG, default=True)
if IS_DEBUG_ENV:
    ZENML_LOGGING_VERBOSITY = os.getenv(ENV_ZENML_LOGGING_VERBOSITY, 4)
else:
    ZENML_LOGGING_VERBOSITY = os.getenv(ENV_ZENML_LOGGING_VERBOSITY, 0)

# Base images for zenml
ZENML_REGISTRY = 'eu.gcr.io/maiot-zenml/'
ZENML_BASE_IMAGE_NAME = f'{ZENML_REGISTRY}/zenml:base-{__version__}'
ZENML_TRAINER_IMAGE_NAME = f'{ZENML_REGISTRY}/zenml:cuda-{__version__}'

# Evaluation utils constants
COMPARISON_NOTEBOOK = 'comparison_notebook.ipynb'
EVALUATION_NOTEBOOK = 'evaluation_notebook.ipynb'

# Pipeline related constants
PREPROCESSING_FN = \
    'zenml.core.components.transform.transform_module.preprocessing_fn'
TRAINER_FN = 'zenml.core.components.trainer.trainer_module.run_fn'
EVALUATOR_MODULE_FN = 'zenml.core.components.evaluator.evaluator_module'
