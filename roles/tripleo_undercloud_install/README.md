tripleo_undercloud_install
==========================

A role to run the install of a TripleO undercloud.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_undercloud_install_debug`: (Boolean) Flag used to enable the debug version of commands. Default: false
* `tripleo_undercloud_install_dry_run`: (Boolean) Flag to add --dry-run to the install. Default: false
* `tripleo_undercloud_install_force_stack_update`: (Boolean) Flag to add --force-stack-update to the install. Default: false
* `tripleo_undercloud_install_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_undercloud_install_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_undercloud_install_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_undercloud_install_home_dir`: (String) Home directory for the undercloud user. Default: "{{ ansible_env.HOME }}"
* `tripleo_undercloud_install_inflight_validations`: (Boolean) Flag to add --inflight-validations to the install. Default: false
* `tripleo_undercloud_install_log_combine`: (Boolean) Flag to combine stdout and stderr in the logfile. Default: true
* `tripleo_undercloud_install_log_output`: (Boolean) Flag to log the output to a file rather than show it in the ansible output. Default: true
* `tripleo_undercloud_install_no_validations`: (Boolean) Flag to add --no-validations to the install. Default: false
* `tripleo_undercloud_install_poll`: (Integer) Number of seconds to wait between checks to see if the install command has completed. This should be set to a value greater or equal to 1. Default: 10
* `tripleo_undercloud_install_timeout`: (Integer) Timeout for the install command. Default: 7200
* `tripleo_undercloud_install_yes`: (Boolean) Flag to add --yes to the install. Default: false
* `tripleo_undercloud_install_log`: (String) Install log file path. Default: "{{ tripleo_undercloud_install_home_dir }}/undercloud_install.log"

Output Variables
----------------

* `tripleo_undercloud_install_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example install execution playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Install undercloud
      import_role:
        name: tripleo_undercloud_install
      vars:
        tripleo_undercloud_install_debug: true
```

License
-------

Apache-2.0
