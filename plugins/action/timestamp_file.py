#!/usr/bin/python
# -*- coding: utf-8 -*-
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
__metaclass__ = type

from ansible.errors import AnsibleActionFail
from ansible.errors import AnsibleActionSkip
from ansible.module_utils.parsing.convert_bool import boolean
from ansible.plugins.action import ActionBase
from datetime import datetime

import yaml

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = """
module: timestamp_file
author:
  - "Alex Schultz (@mwhahaha)"
version_added: '2.9'
short_description: Take a copy of a file and append a timestamp
notes: []
description:
  - Take a copy of a file and append a timestamp
requirements:
  - None
options:
  path:
    description:
      - Path to file
    type: str
  remove:
    description:
      - Remove original file
    default: False
    type: bool
  force:
    description:
      - Overwrite destination file if it exists
    default: False
    type: bool
  date_format:
    description:
      - Timestamp format to use when appending to destination file
    default: "%Y-%m-%d_%H:%M:%S"
    type: str
"""
EXAMPLES = """
- name: Snapshot a file
  timestamp_file:
    path: /tmp/file.log
- name: Snapshot a file and remove original
  timestamp_file:
    path: /tmp/file.log
    remove: True
"""
RETURN = """
dest:
    description: Path to the new file
    returned: if changed
    type: str
    sample: "/tmp/file.log.2017-07-27_16:39:00"
"""


class ActionModule(ActionBase):

    _VALID_ARGS = yaml.safe_load(DOCUMENTATION)['options']

    def _get_args(self):
        missing = []
        args = {}

        for option, vals in self._VALID_ARGS.items():
            if 'default' not in vals:
                if self._task.args.get(option, None) is None:
                    missing.append(option)
                    continue
                args[option] = self._task.args.get(option)
            else:
                args[option] = self._task.args.get(option, vals['default'])

        if missing:
            raise AnsibleActionFail('Missing required parameters: {}'.format(
                ', '.join(missing)))
        return args

    def _get_date_string(self, date_format):
        return datetime.now().strftime(date_format)

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp
        # parse args
        args = self._get_args()

        changed = False
        src_path = args['path']

        # check if source file exists
        file_stat = self._execute_module(
            module_name='stat',
            module_args=dict(path=src_path),
            task_vars=task_vars
        )
        timestamp = self._get_date_string(args['date_format'])
        dest_path = '.'.join([src_path, timestamp])
        if file_stat.get('stat', {}).get('exists', False) is False:
            # file doesn't exist so we're done
            raise AnsibleActionSkip("{} does not exist.".format(src_path))

        # check if destination file exists
        file_stat = self._execute_module(
            module_name='stat',
            module_args=dict(path=dest_path),
            task_vars=task_vars
        )
        if (not args['force']
                and file_stat.get('stat', {}).get('exists', False) is True):
            raise AnsibleActionFail("Destination file {} exists. Use force "
                                    "option to proceed.".format(dest_path))

        # copy file out of the way
        copy_result = self._execute_module(
            module_name='copy',
            module_args=dict(src=src_path, dest=dest_path, remote_src=True),
            task_vars=task_vars
        )
        if copy_result.get('failed', False):
            return copy_result
        changed = True

        if boolean(args.get('remove', False), strict=False):
            # cleanup original file as requested
            file_result = self._execute_module(
                module_name='file',
                module_args=dict(path=src_path, state='absent'),
                task_vars=task_vars
            )
            if file_result.get('failed', False):
                return file_result

        result['dest'] = copy_result['dest']
        result['changed'] = changed
        return result
