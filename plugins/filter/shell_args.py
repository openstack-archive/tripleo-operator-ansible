#!/usr/bin/env python
# Copyright 2019 Red Hat, Inc.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

try:  # py3
    from shlex import quote
except ImportError:  # py2
    from pipes import quote


class FilterModule(object):
    def filters(self):
        return {
            'shell_arg_list': self.shell_arg_list
        }

    def shell_arg_list(self, arg, parameter=None):
        # Nothing was passed into this, just return an empty string
        if not arg:
            return ''
        if not isinstance(arg, (list, tuple)):
            arg = [arg]
        return_value = []
        for a in arg:
            if a:
                val = quote(a)
                if parameter:
                    return_value.append("{} {}".format(parameter, val))
                else:
                    return_value.append(val)
        return ' '.join(return_value)
