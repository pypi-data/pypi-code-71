# flake8: noqa
"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.okta_object import OktaObject
from okta.models import protocol_algorithm_type\
    as protocol_algorithm_type


class ProtocolAlgorithms(
    OktaObject
):
    """
    A class for ProtocolAlgorithms objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "request" in config:
                if isinstance(config["request"],
                              protocol_algorithm_type.ProtocolAlgorithmType):
                    self.request = config["request"]
                elif config["request"] is not None:
                    self.request = protocol_algorithm_type.ProtocolAlgorithmType(
                        config["request"]
                    )
                else:
                    self.request = None
            else:
                self.request = None
            if "response" in config:
                if isinstance(config["response"],
                              protocol_algorithm_type.ProtocolAlgorithmType):
                    self.response = config["response"]
                elif config["response"] is not None:
                    self.response = protocol_algorithm_type.ProtocolAlgorithmType(
                        config["response"]
                    )
                else:
                    self.response = None
            else:
                self.response = None
        else:
            self.request = None
            self.response = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "request": self.request,
            "response": self.response
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
