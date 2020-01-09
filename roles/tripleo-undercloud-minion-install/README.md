tripleo-undercloud-minion-install
==========================

A role to run the install a TripleO undercloud minion.

Requirements
------------

None.

Role Variables
--------------


* `tripleo_undercloud_minion_install_debug`: (Boolean) Flag used to enable the debug version of commands. Default: false
* `tripleo_undercloud_minion_install_home_dir`: (String) Home directory for the undercloud user. Default: "{{ ansible_env.HOME }}"
* `tripleo_undercloud_minion_install_dry_run`: (Boolean) Flag to add --dry-run to the install. Default: false
* `tripleo_undercloud_minion_install_force_stack_update`: (Boolean) Flag to add --force-stack-update to the install. Default: false
* `tripleo_undercloud_minion_install_no_validations`: (Boolean) Flag to add --no-validations to the install. Default: false
* `tripleo_undercloud_minion_install_timeout`: (Number) Timeout for the install command. Default: 7200
* `tripleo_undercloud_minion_install_yes`: (Boolean) Flag to add --yes to the install. Default: false
* `tripleo_undercloud_minion_install_log_combine`: (Boolean) Flag to combine stdout and stderr in the logfile. Default: true
* `tripleo_undercloud_minion_install_log_output`: (Boolean) Flag to log the output to a file rather than show it in the ansible output. Default: true
* `tripleo_undercloud_minion_install_log`: (String) Install log file path. Default: "{{ tripleo_undercloud_minion_install_home_dir }}/undercloud_minion_install.log"

Dependencies
------------

None.

Example Playbook
----------------

Example install execution playbook

    - hosts: undercloud
      gather_facts: true
      tasks:
        - name: Install undercloud minion
          import_role:
            name: tripleo-undercloud-minion-install
          vars:
            tripleo_undercloud_minion_install_debug: true

License
-------

Apache-2.0
