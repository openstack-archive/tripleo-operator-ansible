tripleo_overcloud_upgrade_run
=============================

A role to execute an overcloud upgrade run.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_upgrade_run_debug`: (Boolean) Flag to print out the command that is run. Default: false
* `tripleo_overcloud_upgrade_run_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_upgrade_run_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_upgrade_run_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_upgrade_run_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_upgrade_run_limit`: (String) String that identifies a single node or a list of nodes to be upgraded.
* `tripleo_overcloud_upgrade_run_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_upgrade_run_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_upgrade_run_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_upgrade_run_home_dir }}/overcloud_upgrade_run.log"
* `tripleo_overcloud_upgrade_run_playbook`: (List) List of playbook(s) to use for the upgrade. Defaults: []
* `tripleo_overcloud_upgrade_run_poll`: (Integer) Number of seconds to wait between each checks to see if the deployment command has completed. Default: 10
* `tripleo_overcloud_upgrade_run_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"
* `tripleo_overcloud_upgrade_run_skip_tags`: (String) A string specifying the tag or a comma separated list of tags to be excluded.
* `tripleo_overcloud_upgrade_run_ssh_user`: (String) Username of user to be used as the ssh user.
* `tripleo_overcloud_upgrade_run_stack`: (String) Name of the stack to deploy.
* `tripleo_overcloud_upgrade_run_static_inventory`: (String) Path to an existing ansible inventory to use.
* `tripleo_overcloud_upgrade_run_tags`: (String) A string specifying the tag or a comma separated list of tags to be included.
* `tripleo_overcloud_upgrade_run_timeout`: (Integer) Number in seconds to wait for the ansible execution of the deployment command to finish. Default: 5700

NOTE: Please note that this command should be run against the undercloud so the
OS_CLOUD or rc file variables should be set to use the 'undercloud' when
calling this role. If you are not defining `tripleo_os_cloud` or `tripleo_rc_file`,
stackrc will be used by default.

Output Variables
----------------

* `tripleo_overcloud_upgrade_run_output`: (String) The command standard output.
* `tripleo_overcloud_upgrade_run_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example overcloud upgrade run execution playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Run overcloud upgrade run
      import_role:
        name: tripleo_overcloud_upgrade_run
```

License
-------

Apache-2.0
