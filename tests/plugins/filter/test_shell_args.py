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

from tests import base as tests_base
from plugins.filter import shell_args


class TestShellArgsFilters(tests_base.TestCase):
    def setUp(self):
        super(TestShellArgsFilters, self).setUp()
        self.filter = shell_args.FilterModule()

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

    def test_shell_arg_list_none(self):
        expected = ''
        self.assertEqual(expected, self.filter.shell_arg_list(None))

    def test_shell_arg_list_quote(self):
        arg = ["a b"]
        expected = "--p 'a b'"
        self.assertEqual(expected,
                         self.filter.shell_arg_list(arg, parameter='--p'))

    def test_shell_arg_str_quote(self):
        arg = "a b"
        expected = "'a b'"
        self.assertEqual(expected,
                         self.filter.shell_arg_list(arg))

    def test_shell_arg_list_avoid_none_in_list(self):
        arg = ['a', None]
        expected = '-p a'
        self.assertEqual(expected,
                         self.filter.shell_arg_list(arg, parameter='-p'))
