tripleo_overcloud_netenv_validate
=================================

A role to perform a netenv validation.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_netenv_validate_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_overcloud_netenv_validate_file`: (String) REQUIRED. Path to the network environment file
* `tripleo_overcloud_netenv_validate_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_netenv_validate_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_netenv_validate_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_netenv_validate_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_netenv_validate_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_netenv_validate_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_netenv_validate_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_netenv_validate_home_dir }}/overcloud_netenv_validate.log"
* `tripleo_overcloud_netenv_validate_poll`: (Integer) Number of seconds to wait between each checks to see if the command has completed. Default: 10
* `tripleo_overcloud_netenv_validate_timeout`: (Integer) Number in seconds to wait for the ansible execution of the command to finish. Default: 3600

Output Variables
----------------

* `tripleo_overcloud_netenv_validate_output`: (String) The command standard output.
* `tripleo_overcloud_netenv_validate_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example network environment validation

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: overcloud netenv validate
      import_role:
        name: tripleo_overcloud_netenv_validate
      var:
        tripleo_overcloud_netenv_validate_debug: true
        tripleo_overcloud_netenv_validate_file: /home/stack/templates/network-environment.yaml
```

License
-------

Apache-2.0
