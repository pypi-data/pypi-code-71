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
from okta.okta_collection import OktaCollection
from okta.models import app_and_instance_condition_evaluator_app_or_instance\
    as app_and_instance_condition_evaluator_app_or_instance


class AppAndInstancePolicyRuleCondition(
    OktaObject
):
    """
    A class for AppAndInstancePolicyRuleCondition objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.exclude = OktaCollection.form_list(
                config["exclude"] if "exclude"\
                    in config else [],
                app_and_instance_condition_evaluator_app_or_instance.AppAndInstanceConditionEvaluatorAppOrInstance
            )
            self.include = OktaCollection.form_list(
                config["include"] if "include"\
                    in config else [],
                app_and_instance_condition_evaluator_app_or_instance.AppAndInstanceConditionEvaluatorAppOrInstance
            )
        else:
            self.exclude = []
            self.include = []

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "exclude": self.exclude,
            "include": self.include
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
