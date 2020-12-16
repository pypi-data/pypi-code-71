# -*- coding: utf-8 -*-
'''
    :codeauthor: :email:`Jakub Sliva <jakub.sliva@ultimum.io>`
'''

# Import Python Libs
from __future__ import absolute_import
from __future__ import unicode_literals

# Import Salt Testing Libs
from tests.support.mixins import LoaderModuleMockMixin
from tests.support.unit import TestCase, skipIf
from tests.support.mock import (
    MagicMock,
    patch,
    NO_MOCK,
    NO_MOCK_REASON
)

import salt.states.zabbix_valuemap as zabbix_valuemap


INPUT_PARAMS = {'mappings': [{'newvalue': 'OK', 'value': '0h'}, {'newvalue': 'Failure', 'value': '1'}],
                'name': 'Server HP Health'}

EXISTING_OBJ = [{'valuemapid': '21', 'name': 'Server HP Health', 'mappings': [{'newvalue': 'OK', 'value': '0h'},
                                                                              {'newvalue': 'Failure', 'value': '1'}]}]

EXISTING_OBJ_DIFF = {'valuemapid': '21', 'name': 'Server HP Health', 'mappings': [{'newvalue': 'OK', 'value': '0h'},
                                                                                  {'newvalue': 'Failure', 'value': '1'},
                                                                                  {'newvalue': 'some', 'value': '2'}]}

DIFF_PARAMS = {'valuemapid': '21', 'mappings': [{'newvalue': 'OK', 'value': '0h'},
                                                {'newvalue': 'Failure', 'value': '1'}]}


@skipIf(NO_MOCK, NO_MOCK_REASON)
class ZabbixActionTestCase(TestCase, LoaderModuleMockMixin):
    '''
    Test cases for salt.modules.zabbix
    '''
    def setup_loader_modules(self):
        return {zabbix_valuemap: {}}

    def test_present_create(self):
        '''
        Test to ensure that named value map is created
        '''
        name = 'Server HP Health'
        ret = {'name': name, 'result': False, 'comment': '', 'changes': {}}

        def side_effect_run_query(*args):
            '''
            Differentiate between __salt__ exec module function calls with different parameters.
            '''
            if args[0] == 'valuemap.get':
                return False
            elif args[0] == 'valuemap.create':
                return True

        with patch.dict(zabbix_valuemap.__opts__, {'test': False}):
            with patch.dict(zabbix_valuemap.__salt__,
                            {'zabbix.get_zabbix_id_mapper': MagicMock(return_value={'valuemap': 'valuemapid'}),
                             'zabbix.substitute_params': MagicMock(side_effect=[INPUT_PARAMS, False]),
                             'zabbix.run_query': MagicMock(side_effect=side_effect_run_query),
                             'zabbix.compare_params': MagicMock(return_value={})}):
                ret['result'] = True
                ret['comment'] = 'Zabbix Value map "{0}" created.'.format(name)
                ret['changes'] = {name: {'old': 'Zabbix Value map "{0}" did not exist.'.format(name),
                                         'new': 'Zabbix Value map "{0}" created according definition.'.format(name)}}
                self.assertDictEqual(zabbix_valuemap.present(name, {}), ret)

    def test_present_exists(self):
        '''
        Test to ensure that named value map is present and not changed
        '''
        name = 'Server HP Health'
        ret = {'name': name, 'result': False, 'comment': '', 'changes': {}}

        with patch.dict(zabbix_valuemap.__opts__, {'test': False}):
            with patch.dict(zabbix_valuemap.__salt__,
                            {'zabbix.get_zabbix_id_mapper': MagicMock(return_value={'valuemap': 'valuemapid'}),
                             'zabbix.substitute_params': MagicMock(side_effect=[INPUT_PARAMS, EXISTING_OBJ]),
                             'zabbix.run_query': MagicMock(return_value=['length of result is 1']),
                             'zabbix.compare_params': MagicMock(return_value={})}):
                ret['result'] = True
                ret['comment'] = 'Zabbix Value map "{0}" already exists and corresponds to a definition.'.format(name)
                self.assertDictEqual(zabbix_valuemap.present(name, {}), ret)

    def test_present_update(self):
        '''
        Test to ensure that named value map is present but must be updated
        '''
        name = 'Server HP Health'
        ret = {'name': name, 'result': False, 'comment': '', 'changes': {}}

        def side_effect_run_query(*args):
            '''
            Differentiate between __salt__ exec module function calls with different parameters.
            '''
            if args[0] == 'valuemap.get':
                return ['length of result is 1 = valuemap exists']
            elif args[0] == 'valuemap.update':
                return DIFF_PARAMS

        with patch.dict(zabbix_valuemap.__opts__, {'test': False}):
            with patch.dict(zabbix_valuemap.__salt__,
                            {'zabbix.get_zabbix_id_mapper': MagicMock(return_value={'valuemap': 'valuemapid'}),
                             'zabbix.substitute_params': MagicMock(side_effect=[INPUT_PARAMS, EXISTING_OBJ_DIFF]),
                             'zabbix.run_query': MagicMock(side_effect=side_effect_run_query),
                             'zabbix.compare_params': MagicMock(return_value=DIFF_PARAMS)}):
                ret['result'] = True
                ret['comment'] = 'Zabbix Value map "{0}" updated.'.format(name)
                ret['changes'] = {name: {'old': 'Zabbix Value map "{0}" differed '
                                                'in following parameters: {1}'.format(name, DIFF_PARAMS),
                                         'new': 'Zabbix Value map "{0}" fixed.'.format(name)}}
                self.assertDictEqual(zabbix_valuemap.present(name, {}), ret)

    def test_absent_test_mode(self):
        '''
        Test to ensure that named value map is absent in test mode
        '''
        name = 'Server HP Health'
        ret = {'name': name, 'result': False, 'comment': '', 'changes': {}}
        with patch.dict(zabbix_valuemap.__opts__, {'test': True}):
            with patch.dict(zabbix_valuemap.__salt__, {'zabbix.get_object_id_by_params': MagicMock(return_value=11)}):
                ret['result'] = True
                ret['comment'] = 'Zabbix Value map "{0}" would be deleted.'.format(name)
                ret['changes'] = {name: {'old': 'Zabbix Value map "{0}" exists.'.format(name),
                                         'new': 'Zabbix Value map "{0}" would be deleted.'.format(name)}}
                self.assertDictEqual(zabbix_valuemap.absent(name), ret)

    def test_absent(self):
        '''
        Test to ensure that named value map is absent
        '''
        name = 'Server HP Health'
        ret = {'name': name, 'result': False, 'comment': '', 'changes': {}}
        with patch.dict(zabbix_valuemap.__opts__, {'test': False}):
            with patch.dict(zabbix_valuemap.__salt__,
                            {'zabbix.get_object_id_by_params': MagicMock(return_value=False)}):
                ret['result'] = True
                ret['comment'] = 'Zabbix Value map "{0}" does not exist.'.format(name)
                self.assertDictEqual(zabbix_valuemap.absent(name), ret)

            with patch.dict(zabbix_valuemap.__salt__, {'zabbix.get_object_id_by_params': MagicMock(return_value=11)}):
                with patch.dict(zabbix_valuemap.__salt__, {'zabbix.run_query': MagicMock(return_value=True)}):
                    ret['result'] = True
                    ret['comment'] = 'Zabbix Value map "{0}" deleted.'.format(name)
                    ret['changes'] = {name: {'old': 'Zabbix Value map "{0}" existed.'.format(name),
                                             'new': 'Zabbix Value map "{0}" deleted.'.format(name)}}
                    self.assertDictEqual(zabbix_valuemap.absent(name), ret)
