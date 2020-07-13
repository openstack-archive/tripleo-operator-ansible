tripleo_overcloud_generate_fencing
==================================

A role to generate overcloud fencing parameters.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_generate_fencing_action`: (String) The fencing action. Deprecated and ignored in later versions.
* `tripleo_overcloud_generate_fencing_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_overcloud_generate_fencing_delay`: (Integer) Number of seconds to wait before fencing is started.
* `tripleo_overcloud_generate_fencing_environment_file`: (String) REQUIRED. Path to the environment file.
* `tripleo_overcloud_generate_fencing_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_generate_fencing_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_generate_fencing_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_generate_fencing_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_generate_fencing_ipmi_cipher`: (String) Cipher squit to use (same as ipmitool -C)
* `tripleo_overcloud_generate_fencing_ipmi_lanplus`: (Boolean) Use lanplus. Option deprecated because it's the default. Default: false
* `tripleo_overcloud_generate_fencing_ipmi_level`: (String) Privilege level on IPMI device. (callback, user, operator, administrator)
* `tripleo_overcloud_generate_fencing_ipmi_no_lanplus`: (Boolean) Do not use lanplus. Default: false
* `tripleo_overcloud_generate_fencing_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_generate_fencing_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_generate_fencing_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_generate_fencing_home_dir }}/overcloud_generate_fencing.log"
* `tripleo_overcloud_generate_fencing_os_cloud`: (String) (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_generate_fencing_rc_file`.
* `tripleo_overcloud_generate_fencing_output_file`: (String) Destination for the output parameters.
* `tripleo_overcloud_generate_fencing_poll`: (Integer) Number of seconds to wait between each checks to see if the command has completed. Default: 10
* `tripleo_overcloud_generate_fencing_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"
* `tripleo_overcloud_generate_fencing_timeout`: (Integer) Number in seconds to wait for the ansible execution of the command to finish. Default: 3600

Output Variables
----------------

* `tripleo_overcloud_generate_fencing_output`: (String) The command standard output.
* `tripleo_overcloud_generate_fencing_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example generate fencing

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Run overcloud generate fencing
      import_role:
        name: tripleo_overcloud_generate_fencing
      var:
        tripleo_overcloud_generate_fencing_debug: true
        tripleo_overcloud_generate_fencing_environment_file: /home/stack/instackenv.json
```

License
-------

Apache-2.0
