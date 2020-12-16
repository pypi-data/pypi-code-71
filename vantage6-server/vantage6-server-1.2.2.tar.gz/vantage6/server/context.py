import os
import sys
import appdirs

from pathlib import Path
from sqlalchemy.engine.url import make_url

import vantage6.server.globals as constants

from vantage6.common import Singleton
from vantage6.common.globals import APPNAME
from vantage6.common.context import AppContext
from vantage6.cli.context import ServerContext
from vantage6.server.configuration.configuration_manager import (
    TestingConfigurationManager
)


class TestContext(AppContext):

    INST_CONFIG_MANAGER = TestingConfigurationManager
    LOGGING_ENABLED = False

    @classmethod
    def from_external_config_file(cls, path):
        return super().from_external_config_file(
            cls.test_config_location(),
            "unittest", "application", True
        )

    @staticmethod
    def test_config_location():
        return ( constants.PACAKAGE_FOLDER / constants.APPNAME / \
            "server" / "_data" / "unittest_config.yaml")

    @staticmethod
    def test_data_location():
        return ( constants.PACAKAGE_FOLDER / constants.APPNAME / \
            "server" / "_data" )