# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import salt.modules.reg as reg
import salt.utils.stringutils
import salt.utils.win_reg
from salt.exceptions import CommandExecutionError
from tests.support.helpers import destructiveTest, random_string
from tests.support.mixins import LoaderModuleMockMixin
from tests.support.mock import MagicMock, patch
from tests.support.unit import TestCase, skipIf

try:
    import win32api

    HAS_WIN32 = True
except ImportError:
    HAS_WIN32 = False

UNICODE_KEY = "Unicode Key \N{TRADE MARK SIGN}"
UNICODE_VALUE = (
    "Unicode Value " "\N{COPYRIGHT SIGN},\N{TRADE MARK SIGN},\N{REGISTERED SIGN}"
)
FAKE_KEY = "SOFTWARE\\{}".format(random_string("SaltTesting-", lowercase=False))


@skipIf(not HAS_WIN32, "Tests require win32 libraries")
class WinFunctionsTestCase(TestCase, LoaderModuleMockMixin):
    """
    Test cases for salt.modules.reg
    """

    def setup_loader_modules(self):
        return {
            reg: {
                "__utils__": {
                    "reg.delete_value": salt.utils.win_reg.delete_value,
                    "reg.delete_key_recursive": salt.utils.win_reg.delete_key_recursive,
                    "reg.key_exists": salt.utils.win_reg.key_exists,
                    "reg.list_keys": salt.utils.win_reg.list_keys,
                    "reg.list_values": salt.utils.win_reg.list_values,
                    "reg.read_value": salt.utils.win_reg.read_value,
                    "reg.set_value": salt.utils.win_reg.set_value,
                    "reg.value_exists": salt.utils.win_reg.value_exists,
                }
            }
        }

    def test_key_exists_existing(self):
        """
        Tests the key_exists function using a well known registry key
        """
        self.assertTrue(reg.key_exists(hive="HKLM", key="SOFTWARE\\Microsoft"))

    def test_key_exists_non_existing(self):
        """
        Tests the key_exists function using a non existing registry key
        """
        self.assertFalse(reg.key_exists(hive="HKLM", key=FAKE_KEY))

    def test_key_exists_invalid_hive(self):
        """
        Tests the key_exists function using an invalid hive
        """
        self.assertRaises(
            CommandExecutionError,
            reg.key_exists,
            hive="BADHIVE",
            key="SOFTWARE\\Microsoft",
        )

    def test_key_exists_unknown_key_error(self):
        """
        Tests the key_exists function with an unknown key error
        """
        mock_error = MagicMock(
            side_effect=win32api.error(123, "RegOpenKeyEx", "Unknown error")
        )
        with patch("salt.utils.win_reg.win32api.RegOpenKeyEx", mock_error):
            self.assertRaises(
                win32api.error, reg.key_exists, hive="HKLM", key="SOFTWARE\\Microsoft"
            )

    def test_value_exists_existing(self):
        """
        Tests the value_exists function using a well known registry key
        """
        self.assertTrue(
            reg.value_exists(
                hive="HKLM",
                key="SOFTWARE\\Microsoft\\Windows\\CurrentVersion",
                vname="CommonFilesDir",
            )
        )

    def test_value_exists_non_existing(self):
        """
        Tests the value_exists function using a non existing registry key
        """
        self.assertFalse(
            reg.value_exists(
                hive="HKLM",
                key="SOFTWARE\\Microsoft\\Windows\\CurrentVersion",
                vname="NonExistingValueName",
            )
        )

    def test_value_exists_invalid_hive(self):
        """
        Tests the value_exists function using an invalid hive
        """
        self.assertRaises(
            CommandExecutionError,
            reg.value_exists,
            hive="BADHIVE",
            key="SOFTWARE\\Microsoft\\Windows\\CurrentVersion",
            vname="CommonFilesDir",
        )

    def test_value_exists_key_not_exist(self):
        """
        Tests the value_exists function when the key does not exist
        """
        mock_error = MagicMock(
            side_effect=win32api.error(2, "RegOpenKeyEx", "Unknown error")
        )
        with patch("salt.utils.win_reg.win32api.RegOpenKeyEx", mock_error):
            self.assertFalse(
                reg.value_exists(
                    hive="HKLM",
                    key="SOFTWARE\\Microsoft\\Windows\\CurrentVersion",
                    vname="CommonFilesDir",
                )
            )

    def test_value_exists_unknown_key_error(self):
        """
        Tests the value_exists function with an unknown error when opening the
        key
        """
        mock_error = MagicMock(
            side_effect=win32api.error(123, "RegOpenKeyEx", "Unknown error")
        )
        with patch("salt.utils.win_reg.win32api.RegOpenKeyEx", mock_error):
            self.assertRaises(
                win32api.error,
                reg.value_exists,
                hive="HKLM",
                key="SOFTWARE\\Microsoft\\Windows\\CurrentVersion",
                vname="CommonFilesDir",
            )

    def test_value_exists_empty_default_value(self):
        """
        Tests the value_exists function when querying the default value
        """
        mock_error = MagicMock(
            side_effect=win32api.error(2, "RegQueryValueEx", "Empty Value")
        )
        with patch("salt.utils.win_reg.win32api.RegQueryValueEx", mock_error):
            self.assertTrue(
                reg.value_exists(
                    hive="HKLM",
                    key="SOFTWARE\\Microsoft\\Windows\\CurrentVersion",
                    vname=None,
                )
            )

    def test_value_exists_no_vname(self):
        """
        Tests the value_exists function when the vname does not exist
        """
        mock_error = MagicMock(
            side_effect=win32api.error(123, "RegQueryValueEx", "Empty Value")
        )
        with patch("salt.utils.win_reg.win32api.RegQueryValueEx", mock_error):
            self.assertFalse(
                reg.value_exists(
                    hive="HKLM",
                    key="SOFTWARE\\Microsoft\\Windows\\CurrentVersion",
                    vname="NonExistingValuePair",
                )
            )

    def test_list_keys_existing(self):
        """
        Test the list_keys function using a well known registry key
        """
        self.assertIn("Microsoft", reg.list_keys(hive="HKLM", key="SOFTWARE"))

    def test_list_keys_non_existing(self):
        """
        Test the list_keys function using a non existing registry key
        """
        expected = (False, "Cannot find key: HKLM\\{0}".format(FAKE_KEY))
        self.assertEqual(reg.list_keys(hive="HKLM", key=FAKE_KEY), expected)

    def test_list_keys_invalid_hive(self):
        """
        Test the list_keys function when passing an invalid hive
        """
        self.assertRaises(
            CommandExecutionError,
            reg.list_keys,
            hive="BADHIVE",
            key="SOFTWARE\\Microsoft",
        )

    def test_list_keys_unknown_key_error(self):
        """
        Tests the list_keys function with an unknown key error
        """
        mock_error = MagicMock(
            side_effect=win32api.error(123, "RegOpenKeyEx", "Unknown error")
        )
        with patch("salt.utils.win_reg.win32api.RegOpenKeyEx", mock_error):
            self.assertRaises(
                win32api.error, reg.list_keys, hive="HKLM", key="SOFTWARE\\Microsoft"
            )

    def test_list_values_existing(self):
        """
        Test the list_values function using a well known registry key
        """
        values = reg.list_values(
            hive="HKLM", key="SOFTWARE\\Microsoft\\Windows\\CurrentVersion"
        )
        keys = []
        for value in values:
            keys.append(value["vname"])
        self.assertIn("ProgramFilesDir", keys)

    def test_list_values_non_existing(self):
        """
        Test the list_values function using a non existing registry key
        """
        expected = (False, "Cannot find key: HKLM\\{0}".format(FAKE_KEY))
        self.assertEqual(reg.list_values(hive="HKLM", key=FAKE_KEY), expected)

    def test_list_values_invalid_hive(self):
        """
        Test the list_values function when passing an invalid hive
        """
        self.assertRaises(
            CommandExecutionError,
            reg.list_values,
            hive="BADHIVE",
            key="SOFTWARE\\Microsoft",
        )

    def test_list_values_unknown_key_error(self):
        """
        Tests the list_values function with an unknown key error
        """
        mock_error = MagicMock(
            side_effect=win32api.error(123, "RegOpenKeyEx", "Unknown error")
        )
        with patch("salt.utils.win_reg.win32api.RegOpenKeyEx", mock_error):
            self.assertRaises(
                win32api.error, reg.list_values, hive="HKLM", key="SOFTWARE\\Microsoft"
            )

    def test_read_value_existing(self):
        """
        Test the read_value function using a well known registry value
        """
        ret = reg.read_value(
            hive="HKLM",
            key="SOFTWARE\\Microsoft\\Windows\\CurrentVersion",
            vname="ProgramFilesPath",
        )
        self.assertEqual(ret["vdata"], "%ProgramFiles%")

    def test_read_value_default(self):
        """
        Test the read_value function reading the default value using a well
        known registry key
        """
        ret = reg.read_value(
            hive="HKLM", key="SOFTWARE\\Microsoft\\Windows\\CurrentVersion"
        )
        self.assertEqual(ret["vdata"], "(value not set)")

    def test_read_value_non_existing(self):
        """
        Test the read_value function using a non existing value pair
        """
        expected = {
            "comment": "Cannot find fake_name in HKLM\\SOFTWARE\\Microsoft\\"
            "Windows\\CurrentVersion",
            "vdata": None,
            "vname": "fake_name",
            "success": False,
            "hive": "HKLM",
            "key": "SOFTWARE\\Microsoft\\Windows\\CurrentVersion",
        }
        self.assertDictEqual(
            reg.read_value(
                hive="HKLM",
                key="SOFTWARE\\Microsoft\\Windows\\CurrentVersion",
                vname="fake_name",
            ),
            expected,
        )

    def test_read_value_non_existing_key(self):
        """
        Test the read_value function using a non existing registry key
        """
        expected = {
            "comment": "Cannot find key: HKLM\\{0}".format(FAKE_KEY),
            "vdata": None,
            "vname": "fake_name",
            "success": False,
            "hive": "HKLM",
            "key": FAKE_KEY,
        }
        self.assertDictEqual(
            reg.read_value(hive="HKLM", key=FAKE_KEY, vname="fake_name"), expected
        )

    def test_read_value_invalid_hive(self):
        """
        Test the read_value function when passing an invalid hive
        """
        self.assertRaises(
            CommandExecutionError,
            reg.read_value,
            hive="BADHIVE",
            key="SOFTWARE\\Microsoft",
            vname="ProgramFilesPath",
        )

    def test_read_value_unknown_key_error(self):
        """
        Tests the read_value function with an unknown key error
        """
        mock_error = MagicMock(
            side_effect=win32api.error(123, "RegOpenKeyEx", "Unknown error")
        )
        with patch("salt.utils.win_reg.win32api.RegOpenKeyEx", mock_error):
            self.assertRaises(
                win32api.error,
                reg.read_value,
                hive="HKLM",
                key="SOFTWARE\\Microsoft\\Windows\\CurrentVersion",
                vname="ProgramFilesPath",
            )

    def test_read_value_unknown_value_error(self):
        """
        Tests the read_value function with an unknown value error
        """
        mock_error = MagicMock(
            side_effect=win32api.error(123, "RegQueryValueEx", "Unknown error")
        )
        with patch("salt.utils.win_reg.win32api.RegQueryValueEx", mock_error):
            self.assertRaises(
                win32api.error,
                reg.read_value,
                hive="HKLM",
                key="SOFTWARE\\Microsoft\\Windows\\CurrentVersion",
                vname="ProgramFilesPath",
            )

    @destructiveTest
    def test_read_value_multi_sz_empty_list(self):
        """
        An empty REG_MULTI_SZ value should return an empty list, not None
        """
        try:
            self.assertTrue(
                reg.set_value(
                    hive="HKLM",
                    key=FAKE_KEY,
                    vname="empty_list",
                    vdata=[],
                    vtype="REG_MULTI_SZ",
                )
            )
            expected = {
                "hive": "HKLM",
                "key": FAKE_KEY,
                "success": True,
                "vdata": [],
                "vname": "empty_list",
                "vtype": "REG_MULTI_SZ",
            }
            self.assertEqual(
                reg.read_value(hive="HKLM", key=FAKE_KEY, vname="empty_list",), expected
            )
        finally:
            reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY)

    @destructiveTest
    def test_set_value(self):
        """
        Test the set_value function
        """
        try:
            self.assertTrue(
                reg.set_value(
                    hive="HKLM", key=FAKE_KEY, vname="fake_name", vdata="fake_data"
                )
            )
            expected = {
                "hive": "HKLM",
                "key": FAKE_KEY,
                "success": True,
                "vdata": "fake_data",
                "vname": "fake_name",
                "vtype": "REG_SZ",
            }
            self.assertEqual(
                reg.read_value(hive="HKLM", key=FAKE_KEY, vname="fake_name"), expected
            )
        finally:
            reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY)

    @destructiveTest
    def test_set_value_default(self):
        """
        Test the set_value function on the default value
        """
        try:
            self.assertTrue(
                reg.set_value(hive="HKLM", key=FAKE_KEY, vdata="fake_default_data")
            )
            expected = {
                "hive": "HKLM",
                "key": FAKE_KEY,
                "success": True,
                "vdata": "fake_default_data",
                "vname": "(Default)",
                "vtype": "REG_SZ",
            }
            self.assertEqual(reg.read_value(hive="HKLM", key=FAKE_KEY), expected)
        finally:
            reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY)

    @destructiveTest
    def test_set_value_unicode_key(self):
        """
        Test the set_value function on a unicode key
        """
        try:
            self.assertTrue(
                reg.set_value(
                    hive="HKLM",
                    key="\\".join([FAKE_KEY, UNICODE_KEY]),
                    vname="fake_name",
                    vdata="fake_value",
                )
            )
            expected = {
                "hive": "HKLM",
                "key": "\\".join([FAKE_KEY, UNICODE_KEY]),
                "success": True,
                "vdata": "fake_value",
                "vname": "fake_name",
                "vtype": "REG_SZ",
            }
            self.assertEqual(
                reg.read_value(
                    hive="HKLM",
                    key="\\".join([FAKE_KEY, UNICODE_KEY]),
                    vname="fake_name",
                ),
                expected,
            )
        finally:
            reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY)

    @destructiveTest
    def test_set_value_unicode_value(self):
        """
        Test the set_value function on a unicode value
        """
        try:
            self.assertTrue(
                reg.set_value(
                    hive="HKLM", key=FAKE_KEY, vname="fake_unicode", vdata=UNICODE_VALUE
                )
            )
            expected = {
                "hive": "HKLM",
                "key": FAKE_KEY,
                "success": True,
                "vdata": UNICODE_VALUE,
                "vname": "fake_unicode",
                "vtype": "REG_SZ",
            }
            self.assertEqual(
                reg.read_value(hive="HKLM", key=FAKE_KEY, vname="fake_unicode"),
                expected,
            )
        finally:
            reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY)

    @destructiveTest
    def test_set_value_reg_dword(self):
        """
        Test the set_value function on a REG_DWORD value
        """
        try:
            self.assertTrue(
                reg.set_value(
                    hive="HKLM",
                    key=FAKE_KEY,
                    vname="dword_value",
                    vdata=123,
                    vtype="REG_DWORD",
                )
            )
            expected = {
                "hive": "HKLM",
                "key": FAKE_KEY,
                "success": True,
                "vdata": 123,
                "vname": "dword_value",
                "vtype": "REG_DWORD",
            }
            self.assertEqual(
                reg.read_value(hive="HKLM", key=FAKE_KEY, vname="dword_value"), expected
            )
        finally:
            reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY)

    @destructiveTest
    def test_set_value_reg_qword(self):
        """
        Test the set_value function on a REG_QWORD value
        """
        try:
            self.assertTrue(
                reg.set_value(
                    hive="HKLM",
                    key=FAKE_KEY,
                    vname="qword_value",
                    vdata=123,
                    vtype="REG_QWORD",
                )
            )
            expected = {
                "hive": "HKLM",
                "key": FAKE_KEY,
                "success": True,
                "vdata": 123,
                "vname": "qword_value",
                "vtype": "REG_QWORD",
            }
            self.assertEqual(
                reg.read_value(hive="HKLM", key=FAKE_KEY, vname="qword_value"), expected
            )
        finally:
            reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY)

    def test_set_value_invalid_hive(self):
        """
        Test the set_value function when passing an invalid hive
        """
        self.assertRaises(
            CommandExecutionError,
            reg.set_value,
            hive="BADHIVE",
            key=FAKE_KEY,
            vname="fake_name",
            vdata="fake_data",
        )

    def test_set_value_open_create_failure(self):
        """
        Test the set_value function when there is a problem opening/creating
        the key
        """
        mock_error = MagicMock(
            side_effect=win32api.error(123, "RegCreateKeyEx", "Unknown error")
        )
        with patch("salt.utils.win_reg.win32api.RegCreateKeyEx", mock_error):
            self.assertFalse(
                reg.set_value(
                    hive="HKLM", key=FAKE_KEY, vname="fake_name", vdata="fake_data"
                )
            )

    def test_set_value_type_error(self):
        """
        Test the set_value function when the wrong type of data is passed
        """
        mock_error = MagicMock(side_effect=TypeError("Mocked TypeError"))
        with patch("salt.utils.win_reg.win32api.RegSetValueEx", mock_error):
            self.assertFalse(
                reg.set_value(
                    hive="HKLM", key=FAKE_KEY, vname="fake_name", vdata="fake_data"
                )
            )

    def test_set_value_system_error(self):
        """
        Test the set_value function when a SystemError occurs while setting the
        value
        """
        mock_error = MagicMock(side_effect=SystemError("Mocked SystemError"))
        with patch("salt.utils.win_reg.win32api.RegSetValueEx", mock_error):
            self.assertFalse(
                reg.set_value(
                    hive="HKLM", key=FAKE_KEY, vname="fake_name", vdata="fake_data"
                )
            )

    def test_set_value_value_error(self):
        """
        Test the set_value function when a ValueError occurs while setting the
        value
        """
        mock_error = MagicMock(side_effect=ValueError("Mocked ValueError"))
        with patch("salt.utils.win_reg.win32api.RegSetValueEx", mock_error):
            self.assertFalse(
                reg.set_value(
                    hive="HKLM", key=FAKE_KEY, vname="fake_name", vdata="fake_data"
                )
            )

    @destructiveTest
    def test_delete_value(self):
        """
        Test the delete_value function
        """
        try:
            self.assertTrue(
                reg.set_value(
                    hive="HKLM", key=FAKE_KEY, vname="fake_name", vdata="fake_data"
                )
            )
            self.assertTrue(
                reg.delete_value(hive="HKLM", key=FAKE_KEY, vname="fake_name")
            )
        finally:
            reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY)

    def test_delete_value_non_existing(self):
        """
        Test the delete_value function on non existing value
        """
        mock_error = MagicMock(
            side_effect=win32api.error(2, "RegOpenKeyEx", "Unknown error")
        )
        with patch("salt.utils.win_reg.win32api.RegOpenKeyEx", mock_error):
            self.assertIsNone(
                reg.delete_value(hive="HKLM", key=FAKE_KEY, vname="fake_name")
            )

    def test_delete_value_invalid_hive(self):
        """
        Test the delete_value function when passing an invalid hive
        """
        self.assertRaises(
            CommandExecutionError,
            reg.delete_value,
            hive="BADHIVE",
            key=FAKE_KEY,
            vname="fake_name",
        )

    def test_delete_value_unknown_error(self):
        """
        Test the delete_value function when there is a problem opening the key
        """
        mock_error = MagicMock(
            side_effect=win32api.error(123, "RegOpenKeyEx", "Unknown error")
        )
        with patch("salt.utils.win_reg.win32api.RegOpenKeyEx", mock_error):
            self.assertRaises(
                win32api.error,
                reg.delete_value,
                hive="HKLM",
                key=FAKE_KEY,
                vname="fake_name",
            )

    @destructiveTest
    def test_delete_value_unicode(self):
        """
        Test the delete_value function on a unicode value
        """
        try:
            self.assertTrue(
                reg.set_value(
                    hive="HKLM", key=FAKE_KEY, vname="fake_unicode", vdata=UNICODE_VALUE
                )
            )
            self.assertTrue(
                reg.delete_value(hive="HKLM", key=FAKE_KEY, vname="fake_unicode")
            )
        finally:
            reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY)

    @destructiveTest
    def test_delete_value_unicode_vname(self):
        """
        Test the delete_value function on a unicode vname
        """
        try:
            self.assertTrue(
                reg.set_value(
                    hive="HKLM", key=FAKE_KEY, vname=UNICODE_KEY, vdata="junk data"
                )
            )
            self.assertTrue(
                reg.delete_value(hive="HKLM", key=FAKE_KEY, vname=UNICODE_KEY)
            )
        finally:
            reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY)

    @destructiveTest
    def test_delete_value_unicode_key(self):
        """
        Test the delete_value function on a unicode key
        """
        try:
            self.assertTrue(
                reg.set_value(
                    hive="HKLM",
                    key="\\".join([FAKE_KEY, UNICODE_KEY]),
                    vname="fake_name",
                    vdata="junk data",
                )
            )
            self.assertTrue(
                reg.delete_value(
                    hive="HKLM",
                    key="\\".join([FAKE_KEY, UNICODE_KEY]),
                    vname="fake_name",
                )
            )
        finally:
            reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY)

    def test_delete_key_recursive_invalid_hive(self):
        """
        Test the delete_key_recursive function when passing an invalid hive
        """
        self.assertRaises(
            CommandExecutionError,
            reg.delete_key_recursive,
            hive="BADHIVE",
            key=FAKE_KEY,
        )

    def test_delete_key_recursive_key_not_found(self):
        """
        Test the delete_key_recursive function when the passed key to delete is
        not found.
        """
        self.assertFalse(reg.key_exists(hive="HKLM", key=FAKE_KEY))
        self.assertFalse(reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY))

    def test_delete_key_recursive_too_close(self):
        """
        Test the delete_key_recursive function when the passed key to delete is
        too close to root, such as
        """
        mock_true = MagicMock(return_value=True)
        with patch("salt.utils.win_reg.key_exists", mock_true):
            self.assertFalse(reg.delete_key_recursive(hive="HKLM", key="FAKE_KEY"))

    @destructiveTest
    def test_delete_key_recursive(self):
        """
        Test the delete_key_recursive function
        """
        try:
            self.assertTrue(
                reg.set_value(
                    hive="HKLM", key=FAKE_KEY, vname="fake_name", vdata="fake_value"
                )
            )
            expected = {"Deleted": ["\\".join(["HKLM", FAKE_KEY])], "Failed": []}
            self.assertDictEqual(
                reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY), expected
            )
        finally:
            reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY)

    @destructiveTest
    def test_delete_key_recursive_failed_to_open_key(self):
        """
        Test the delete_key_recursive function on failure to open the key
        """
        try:
            self.assertTrue(
                reg.set_value(
                    hive="HKLM", key=FAKE_KEY, vname="fake_name", vdata="fake_value"
                )
            )
            expected = {
                "Deleted": [],
                "Failed": ["\\".join(["HKLM", FAKE_KEY]) + " Failed to connect to key"],
            }
            mock_true = MagicMock(return_value=True)
            mock_error = MagicMock(
                side_effect=[
                    1,
                    win32api.error(3, "RegOpenKeyEx", "Failed to connect to key"),
                ]
            )
            with patch("salt.utils.win_reg.key_exists", mock_true), patch(
                "salt.utils.win_reg.win32api.RegOpenKeyEx", mock_error
            ):
                self.assertDictEqual(
                    reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY), expected
                )
        finally:
            reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY)

    @destructiveTest
    def test_delete_key_recursive_failed_to_delete(self):
        """
        Test the delete_key_recursive function on failure to delete a key
        """
        try:
            self.assertTrue(
                reg.set_value(
                    hive="HKLM", key=FAKE_KEY, vname="fake_name", vdata="fake_value"
                )
            )
            expected = {
                "Deleted": [],
                "Failed": ["\\".join(["HKLM", FAKE_KEY]) + " Unknown error"],
            }
            # pylint: disable=undefined-variable
            mock_error = MagicMock(side_effect=WindowsError("Unknown error"))
            # pylint: enable=undefined-variable
            with patch("salt.utils.win_reg.win32api.RegDeleteKey", mock_error):
                self.assertDictEqual(
                    reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY), expected
                )
        finally:
            reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY)

    @destructiveTest
    def test_delete_key_recursive_unicode(self):
        """
        Test the delete_key_recursive function on value within a unicode key
        """
        try:
            self.assertTrue(
                reg.set_value(
                    hive="HKLM",
                    key="\\".join([FAKE_KEY, UNICODE_KEY]),
                    vname="fake_name",
                    vdata="fake_value",
                )
            )
            expected = {
                "Deleted": ["\\".join(["HKLM", FAKE_KEY, UNICODE_KEY])],
                "Failed": [],
            }
            self.assertDictEqual(
                reg.delete_key_recursive(
                    hive="HKLM", key="\\".join([FAKE_KEY, UNICODE_KEY])
                ),
                expected,
            )
        finally:
            reg.delete_key_recursive(hive="HKLM", key=FAKE_KEY)
