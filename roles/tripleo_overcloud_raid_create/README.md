tripleo_overcloud_raid_create
=============================

A role to perform raid on given nodes.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_raid_create_configuration`: (String) REQUIRED. Path to file containing raid configuration.
* `tripleo_overcloud_raid_create_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_overcloud_raid_create_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_raid_create_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_raid_create_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_raid_create_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_raid_create_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_raid_create_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_raid_create_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_raid_create_home_dir }}/overcloud_raid_create.log"
* `tripleo_overcloud_raid_create_nodes`: (List) REQUIRED. Nodes to create RAID on. Default: []
* `tripleo_overcloud_raid_create_os_cloud`: (String) (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_raid_create_rc_file`.
* `tripleo_overcloud_raid_create_poll`: (Integer) Number of seconds to wait between each checks to see if the command has completed. Default: 10
* `tripleo_overcloud_raid_create_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"
* `tripleo_overcloud_raid_create_timeout`: (Integer) Number in seconds to wait for the ansible execution of the command to finish. Default: 3600

Output Variables
----------------

* `tripleo_overcloud_raid_create_output`: (String) The command standard output.
* `tripleo_overcloud_raid_create_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example raid create

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Run overcloud raid create
      import_role:
        name: tripleo_overcloud_raid_create
      var:
        tripleo_overcloud_raid_create_debug: true
        tripleo_overcloud_raid_create_configuration: /home/stack/raid.yaml
        tripleo_overcloud_raid_create_nodes:
          - node1
          - node2
```

License
-------

Apache-2.0
