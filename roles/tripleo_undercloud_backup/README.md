tripleo_undercloud_backup
=========================

A role to run backup of a TripleO undercloud.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_undercloud_backup_add_path`: (List) List of additional filesystem paths to backup. Default: []
* `tripleo_undercloud_backup_debug`: (Boolean) Flag used to enable the debug version of commands. Default: false
* `tripleo_undercloud_backup_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_undercloud_backup_exclude_path`: (List) List of filesystems path to skip backing up. Default: []
* `tripleo_undercloud_backup_home_dir`: (String) Home directory for the undercloud user. Default: "{{ ansible_env.HOME }}"
* `tripleo_undercloud_backup_log_combine`: (Boolean) Flag to combine stdout and stderr in the logfile. Default: true
* `tripleo_undercloud_backup_log_output`: (Boolean) Flag to log the output to a file rather than show it in the ansible output. Default: true
* `tripleo_undercloud_backup_poll`: (Integer) Number of seconds to wait between checks to see if the backup command has completed. This should be set to a value greater or equal to 1. Default: 10
* `tripleo_undercloud_backup_timeout`: (Integer) Timeout for the backup command. Default: 7200
* `tripleo_undercloud_backup_log`: (String) Backup log file path. Default: "{{ tripleo_undercloud_backup_home_dir }}/undercloud_backup.log"

Output Variables
----------------

* `tripleo_undercloud_backup_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example backup execution playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Backup undercloud
      import_role:
        name: tripleo_undercloud_backup
      vars:
        tripleo_undercloud_backup_debug: true
```

License
-------

Apache-2.0
