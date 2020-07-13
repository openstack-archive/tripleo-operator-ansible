tripleo_overcloud_credentials
=============================

A role to run the credentials action to output the cloud rc files.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_credentials_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_overcloud_credentials_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_credentials_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_credentials_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_credentials_directory`: (String) The directory to create the rc files in. Defaults to current working directory which will be `tripleo_overcloud_credentials_home_dir`.
* `tripleo_overcloud_credentials_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_credentials_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_credentials_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_credentials_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_credentials_home_dir }}/overcloud_credentials.log"
* `tripleo_overcloud_credentials_os_cloud`: (String) (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_credentials_rc_file`.
* `tripleo_overcloud_credentials_plan`: (String) REQUIRED. The name of the plan you wan to create rc files for.
* `tripleo_overcloud_credentials_poll`: (Integer) Number of seconds to wait between each checks to see if the command has completed. Default: 10
* `tripleo_overcloud_credentials_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"
* `tripleo_overcloud_credentials_timeout`: (Integer) Number in seconds to wait for the ansible execution of the command to finish. Default: 3600

Output Variables
----------------

* `tripleo_overcloud_credentials_output`: (String) The command standard output.
* `tripleo_overcloud_credentials_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example overcloud credentials playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Run overcloud credentials
      import_role:
        name: tripleo_overcloud_credentials
      var:
        tripleo_overcloud_credentials_debug: true
```

License
-------

Apache-2.0
