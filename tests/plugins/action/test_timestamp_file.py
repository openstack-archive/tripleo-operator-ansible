# Copyright 2019 Red Hat, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from unittest import mock

from ansible.errors import AnsibleActionFail
from ansible.errors import AnsibleActionSkip
from ansible.playbook.play_context import PlayContext

from tests import base as tests_base
from plugins.action import timestamp_file


class TestTimestampFile(tests_base.TestCase):

    def test_run(self):
        mock_task = mock.MagicMock()
        mock_task.async_val = None
        mock_task.action = "timestamp_file"
        mock_task.args = dict(path='foo.log')
        mock_connection = mock.MagicMock()
        play_context = PlayContext()

        action = timestamp_file.ActionModule(mock_task,
                                             mock_connection,
                                             play_context,
                                             None,
                                             None,
                                             None)

        mock_datetime = mock.MagicMock()
        mock_datetime.return_value = 'foo'
        action._get_date_string = mock_datetime
        mock_execute = mock.MagicMock()
        mock_execute.side_effect = [{'stat': {'exists': True}},
                                    {'stat': {'exists': False}},
                                    {'dest': 'foo.log.foo',
                                     'failed': False,
                                     'changed': True}]

        action._execute_module = mock_execute

        result = action.run()

        execute_calls = [
            mock.call(module_args={'path': 'foo.log'},
                      module_name='stat',
                      task_vars={}),
            mock.call(module_args={'path': 'foo.log.foo'},
                      module_name='stat',
                      task_vars={}),
            mock.call(module_args={'src': 'foo.log',
                                   'dest': 'foo.log.foo',
                                   'remote_src': True},
                      module_name='copy',
                      task_vars={})
        ]
        self.assertEqual(3, mock_execute.call_count)
        mock_execute.assert_has_calls(execute_calls)

        expected_result = {'dest': 'foo.log.foo', 'changed': True}
        self.assertEqual(expected_result, result)

    def test_run_source_missing_skips(self):
        mock_task = mock.MagicMock()
        mock_task.async_val = None
        mock_task.action = "timestamp_file"
        mock_task.args = dict(path='foo.log')
        mock_connection = mock.MagicMock()
        play_context = PlayContext()

        action = timestamp_file.ActionModule(mock_task,
                                             mock_connection,
                                             play_context,
                                             None,
                                             None,
                                             None)

        mock_datetime = mock.MagicMock()
        mock_datetime.return_value = 'foo'
        action._get_date_string = mock_datetime
        mock_execute = mock.MagicMock()
        mock_execute.side_effect = [{'stat': {'exists': False}}]

        action._execute_module = mock_execute

        self.assertRaises(AnsibleActionSkip, action.run)

        execute_calls = [
            mock.call(module_args={'path': 'foo.log'},
                      module_name='stat',
                      task_vars={})
        ]
        self.assertEqual(1, mock_execute.call_count)
        mock_execute.assert_has_calls(execute_calls)

    def test_run_destination_exists_fails(self):
        mock_task = mock.MagicMock()
        mock_task.async_val = None
        mock_task.action = "timestamp_file"
        mock_task.args = dict(path='foo.log')
        mock_connection = mock.MagicMock()
        play_context = PlayContext()

        action = timestamp_file.ActionModule(mock_task,
                                             mock_connection,
                                             play_context,
                                             None,
                                             None,
                                             None)

        mock_datetime = mock.MagicMock()
        mock_datetime.return_value = 'foo'
        action._get_date_string = mock_datetime
        mock_execute = mock.MagicMock()
        mock_execute.side_effect = [{'stat': {'exists': True}},
                                    {'stat': {'exists': True}}]

        action._execute_module = mock_execute

        self.assertRaises(AnsibleActionFail, action.run)

        execute_calls = [
            mock.call(module_args={'path': 'foo.log'},
                      module_name='stat',
                      task_vars={}),
            mock.call(module_args={'path': 'foo.log.foo'},
                      module_name='stat',
                      task_vars={})
        ]
        self.assertEqual(2, mock_execute.call_count)
        mock_execute.assert_has_calls(execute_calls)

    def test_run_destination_exists_force(self):
        mock_task = mock.MagicMock()
        mock_task.async_val = None
        mock_task.action = "timestamp_file"
        mock_task.args = dict(path='foo.log', force=True)
        mock_connection = mock.MagicMock()
        play_context = PlayContext()

        action = timestamp_file.ActionModule(mock_task,
                                             mock_connection,
                                             play_context,
                                             None,
                                             None,
                                             None)

        mock_datetime = mock.MagicMock()
        mock_datetime.return_value = 'foo'
        action._get_date_string = mock_datetime
        mock_execute = mock.MagicMock()
        mock_execute.side_effect = [{'stat': {'exists': True}},
                                    {'stat': {'exists': True}},
                                    {'dest': 'foo.log.foo',
                                     'failed': False,
                                     'changed': True}]

        action._execute_module = mock_execute

        result = action.run()

        execute_calls = [
            mock.call(module_args={'path': 'foo.log'},
                      module_name='stat',
                      task_vars={}),
            mock.call(module_args={'path': 'foo.log.foo'},
                      module_name='stat',
                      task_vars={}),
            mock.call(module_args={'src': 'foo.log',
                                   'dest': 'foo.log.foo',
                                   'remote_src': True},
                      module_name='copy',
                      task_vars={})
        ]
        self.assertEqual(3, mock_execute.call_count)
        mock_execute.assert_has_calls(execute_calls)

        expected_result = {'dest': 'foo.log.foo', 'changed': True}
        self.assertEqual(expected_result, result)
