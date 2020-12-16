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

from ml_metadata.proto import metadata_store_pb2

from zenml.core.metadata.metadata_wrapper import ZenMLMetadataStore
from zenml.utils.enums import MLMetadataTypes


class MockMetadataStore(ZenMLMetadataStore):
    STORE_TYPE = MLMetadataTypes.mock.name

    def __init__(self):
        """Constructor for Mock MetadataStore for ZenML."""
        super().__init__()

    def get_tfx_metadata_config(self):
        config = metadata_store_pb2.ConnectionConfig()
        config.fake_database.SetInParent()  # Sets an empty fake
        return config
