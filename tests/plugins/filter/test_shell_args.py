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

import mock

from tests import base as tests_base
from plugins.filter import shell_args


class TestShellArgsFilters(tests_base.TestCase):
    def setUp(self):
        super(TestShellArgsFilters, self).setUp()
        self.filter = shell_args.FilterModule()

    def test_shell_arg_enabled_default(self):
        self.assertEqual('foo',
                         self.filter.shell_arg_enabled('foo'))

    def test_shell_arg_enabled_disabled(self):
        self.assertEqual('',
                         self.filter.shell_arg_enabled('foo', enabled=False))

    def test_shell_arg_list_default(self):
        arg = ['a', 'b']
        expected = 'a b'
        self.assertEqual(expected, self.filter.shell_arg_list(arg))

    def test_shell_arg_list_string(self):
        arg = 'a'
        expected = 'a'
        self.assertEqual(expected, self.filter.shell_arg_list(arg))

    def test_shell_arg_list_param(self):
        arg = ['a', 'b']
        expected = '--p a --p b'
        self.assertEqual(expected,
                         self.filter.shell_arg_list(arg, parameter='--p'))

    def test_shell_logging_path_default(self):
        location = '/tmp/foo.log'
        expected = ''
        self.assertEqual(expected,
                         self.filter.shell_logging_path(location))

    def test_shell_logging_path_enabled(self):
        location = '/tmp/foo.log'
        expected = ' 2>&1 >/tmp/foo.log'
        self.assertEqual(expected,
                         self.filter.shell_logging_path(location,
                                                        enabled=True))

    def test_shell_logging_path_enabled_not_combined(self):
        location = '/tmp/foo.log'
        expected = ' >/tmp/foo.log'
        self.assertEqual(expected,
                         self.filter.shell_logging_path(location,
                                                        combine=False,
                                                        enabled=True))
