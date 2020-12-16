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

from enum import Enum, unique


@unique
class ExecutionResultType(Enum):
    """Enumeration of possible action execution results"""
    NoResult = 0
    Executing = 1
    Skipped = 2
    Passed = 3
    Failed = 4
    Disabled = 5
    Aborted = 6
    Suspended = 7
    Error = 8
