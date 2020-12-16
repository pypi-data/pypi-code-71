# pubsubplus-python-client
#
# Copyright 2020 Solace Corporation. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" This module defines a message publisher."""
from abc import ABC

from solace.messaging.publisher.publisher_health_check import PublisherHealthCheck
from solace.messaging.utils.life_cycle_control import LifecycleControl, AsyncLifecycleControl


class MessagePublisher(LifecycleControl, AsyncLifecycleControl, PublisherHealthCheck, ABC):
    """
    This is a base interface class that abstracts message publishing behavior.
    """
