# Copyright 2020 TestProject (https://testproject.io)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Union

from src.testproject.classes import StepSettings
from src.testproject.enums import SleepTimingType, TakeScreenshotConditionType
from src.testproject.sdk.drivers.webdriver import Remote
from src.testproject.sdk.drivers.webdriver.base import BaseDriver


class DriverStepSettings:
    """Implementation of the 'with' compound statement.

    If driver auto step reports is enabled, all the driver commands within this compound statement will be reported
    according to the given StepSettings.
    """
    def __init__(self, driver: Union[BaseDriver, Remote], step_settings: StepSettings):
        """Initializes the 'with' statement."""
        self.previous_settings = driver.command_executor.settings
        self.driver = driver
        # If inherit take the previous step settings.
        if step_settings.sleep_timing_type and step_settings.sleep_timing_type is SleepTimingType.Inherit:
            step_settings.sleep_timing_type = self.previous_settings.sleep_timing_type
        if step_settings.screenshot_condition \
                and step_settings.screenshot_condition is TakeScreenshotConditionType.Inherit:
            step_settings.screenshot_condition = self.previous_settings.screenshot_condition
        self.step_settings = step_settings

    def __enter__(self):
        """Setting the driver's command_executor new settings."""
        self.driver.command_executor.settings = self.step_settings

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Reverting to the previous settings."""
        self.driver.command_executor.settings = self.previous_settings
