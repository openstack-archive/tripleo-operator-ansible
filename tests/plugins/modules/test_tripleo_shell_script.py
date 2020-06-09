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

from plugins.modules import tripleo_shell_script
from tests import base as tests_base


class TestTripleoShellScript(tests_base.TestCase):

    @mock.patch('os.chmod')
    def test_run(self, mock_chmod):
        mock_module = mock.Mock()
        mock_exit_json = mock.Mock()
        mock_open = mock.mock_open()
        mock_module.exit_json = mock_exit_json
        params = {'dest': '/tmo/foo.sh',
                  'shell_command': 'foo'}
        mock_module.params = params
        results = {}

        with mock.patch('plugins.modules.tripleo_shell_script.open',
                        mock_open):
            tripleo_shell_script.TripleoShellScript(mock_module, results)

        mock_calls = [
            mock.call().write(tripleo_shell_script._SHELL_HEADER),
            mock.call().write('foo'),
            mock.call().write("\n")
        ]
        mock_open.assert_has_calls(mock_calls)
        mock_chmod.assert_called_once_with('/tmo/foo.sh', 0o755)
        mock_exit_json.assert_called_once_with(changed=True)

    @mock.patch('os.chmod')
    def test_run_env(self, mock_chmod):
        mock_module = mock.Mock()
        mock_exit_json = mock.Mock()
        mock_open = mock.mock_open()
        mock_module.exit_json = mock_exit_json
        params = {'dest': '/tmo/foo.sh',
                  'shell_command': 'foo',
                  'shell_environment': {
                      'OS_CLOUD': 'undercloud'}
                  }
        mock_module.params = params
        results = {}

        with mock.patch('plugins.modules.tripleo_shell_script.open',
                        mock_open):
            tripleo_shell_script.TripleoShellScript(mock_module, results)

        mock_calls = [
            mock.call().write(tripleo_shell_script._SHELL_HEADER),
            mock.call().write('export OS_CLOUD=undercloud\n'),
            mock.call().write('foo'),
            mock.call().write("\n")
        ]
        mock_open.assert_has_calls(mock_calls)
        mock_chmod.assert_called_once_with('/tmo/foo.sh', 0o755)
        mock_exit_json.assert_called_once_with(changed=True)

    @mock.patch('os.chmod')
    def test_run_env_avoid_none(self, mock_chmod):
        mock_module = mock.Mock()
        mock_exit_json = mock.Mock()
        mock_open = mock.mock_open()
        mock_module.exit_json = mock_exit_json
        params = {'dest': '/tmo/foo.sh',
                  'shell_command': 'foo',
                  'shell_environment': {
                      'OS_CLOUD': 'undercloud',
                      'FOO_BAR': None}
                  }
        mock_module.params = params
        results = {}

        with mock.patch('plugins.modules.tripleo_shell_script.open',
                        mock_open):
            tripleo_shell_script.TripleoShellScript(mock_module, results)

        mock_calls = [
            mock.call().write(tripleo_shell_script._SHELL_HEADER),
            mock.call().write('export OS_CLOUD=undercloud\n'),
            mock.call().write('foo'),
            mock.call().write("\n")
        ]
        mock_open.assert_has_calls(mock_calls)
        mock_chmod.assert_called_once_with('/tmo/foo.sh', 0o755)
        mock_exit_json.assert_called_once_with(changed=True)

    @mock.patch('os.chmod')
    def test_run_env_quote_int(self, mock_chmod):
        mock_module = mock.Mock()
        mock_exit_json = mock.Mock()
        mock_open = mock.mock_open()
        mock_module.exit_json = mock_exit_json
        params = {'dest': '/tmo/foo.sh',
                  'shell_command': 'foo',
                  'shell_environment': {
                      'OS_CLOUD': 'undercloud',
                      'FOO_BAR': 1}
                  }
        mock_module.params = params
        results = {}

        with mock.patch('plugins.modules.tripleo_shell_script.open',
                        mock_open):
            tripleo_shell_script.TripleoShellScript(mock_module, results)

        mock_calls = [
            mock.call().write(tripleo_shell_script._SHELL_HEADER),
            mock.call().write('export OS_CLOUD=undercloud\n'),
            mock.call().write('export FOO_BAR=1\n'),
            mock.call().write('foo'),
            mock.call().write("\n")
        ]
        mock_open.assert_has_calls(mock_calls)
        mock_chmod.assert_called_once_with('/tmo/foo.sh', 0o755)
        mock_exit_json.assert_called_once_with(changed=True)

    @mock.patch('os.chmod')
    def test_run_env_quoted(self, mock_chmod):
        mock_module = mock.Mock()
        mock_exit_json = mock.Mock()
        mock_open = mock.mock_open()
        mock_module.exit_json = mock_exit_json
        params = {'dest': '/tmo/foo.sh',
                  'shell_command': 'foo',
                  'shell_environment': {
                      'OS_CLOUD': 'undercloud',
                      'FILES': 'a.yaml b.yaml'}
                  }
        mock_module.params = params
        results = {}

        with mock.patch('plugins.modules.tripleo_shell_script.open',
                        mock_open):
            tripleo_shell_script.TripleoShellScript(mock_module, results)

        mock_calls = [
            mock.call().write(tripleo_shell_script._SHELL_HEADER),
            mock.call().write('export OS_CLOUD=undercloud\n'),
            mock.call().write('export FILES=\'a.yaml b.yaml\'\n'),
            mock.call().write('foo'),
            mock.call().write("\n")
        ]
        mock_open.assert_has_calls(mock_calls)
        mock_chmod.assert_called_once_with('/tmo/foo.sh', 0o755)
        mock_exit_json.assert_called_once_with(changed=True)

    @mock.patch('os.chmod')
    def test_run_fail(self, mock_chmod):
        mock_module = mock.Mock()
        mock_exit_json = mock.Mock()
        mock_open = mock.mock_open()
        mock_open.side_effect = Exception('err')
        mock_module.exit_json = mock_exit_json
        params = {'dest': '/tmo/foo.sh',
                  'shell_command': 'foo'}
        mock_module.params = params
        results = {}

        with mock.patch('plugins.modules.tripleo_shell_script.open',
                        mock_open):
            tripleo_shell_script.TripleoShellScript(mock_module, results)
        mock_exit_json.assert_called_once_with(
            error='err',
            failed=True,
            msg='Unable to output shell script /tmo/foo.sh: err')
