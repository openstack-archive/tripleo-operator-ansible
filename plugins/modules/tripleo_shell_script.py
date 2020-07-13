#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat, Inc.
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

from ansible.module_utils.basic import AnsibleModule

import os
import yaml

try:  # py3
    from shlex import quote
except ImportError:  # py2
    from pipes import quote

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = """
---
module: tripleo_shell_script
author:
  - Alex Schultz <aschultz@redhat.com>
version_added: '2.8'
short_description: Writes out a shell script with environment vars and command
notes: []
description:
  - This module will write out a bash script from a shell environment dict
    and a commandline string.
options:
  dest:
    description:
      - Destination file path for the output shell script.
    required: True
    type: str
  shell_command:
    description:
      - Shell command that will be run
    required: True
    type: str
  shell_environment:
    description:
      - Environment dictionary for the shell execution.
    default: {}
    required: False
    type: dict
"""

EXAMPLES = """
- name: Undercloud install
  tripleo_shell_script:
    dest: /home/stack/undercloud_install.sh
    shell_command: "/usr/bin/openstack undercloud install"
    shell_environment: {}
- name: Image upload
  tripleo_shell_script:
    dest: /home/stack/overcloud_image_upload.sh
    shell_command: "/usr/bin/openstack overcloud image upload"
    shell_environment:
      OS_CLOUD: undercloud
"""

RETURN = """
"""

_SHELL_HEADER = """#!/bin/bash
# This file is managed by ansible
set -xeo pipefail

"""


class TripleoShellScript(object):
    """Notes about this module.

    This module will write out a bash script from the provided parameters.
    """

    def __init__(self, module, results):

        self.module = module
        self.results = results

        # parse args
        args = self.module.params

        # Set parameters
        dest = args['dest']
        shell_command = args['shell_command']
        shell_environment = args.get('shell_environment', {})

        if os.path.exists(dest):
            self.module.debug('File exists, truncating %s' % dest)

        try:
            with open(dest, 'w') as fh:
                fh.write(_SHELL_HEADER)
                for k, v in shell_environment.items():
                    if v:
                        val = quote(str(v))
                        fh.write("export %(key)s=%(val)s\n" % {'key': k,
                                                               'val': val})
                fh.write(shell_command)
                fh.write("\n")
            os.chmod(dest, 0o755)
            self.results['changed'] = True
        except Exception as e:
            self.results['failed'] = True
            self.results['error'] = str(e)
            self.results['msg'] = ("Unable to output shell script %s: %s" % (
                dest, e))

        self.module.exit_json(**self.results)


def main():
    module = AnsibleModule(
        argument_spec=yaml.safe_load(DOCUMENTATION)['options'],
        supports_check_mode=False
    )
    results = dict(
        changed=False
    )
    TripleoShellScript(module, results)


if __name__ == '__main__':
    main()
