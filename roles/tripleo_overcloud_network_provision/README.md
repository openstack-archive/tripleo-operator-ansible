tripleo_overcloud_network_provision
=========

A role to perform overcloud network provisioning.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_network_provision_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_overcloud_network_provision_deployment_file`: (String) REQUIRED. File path to the deployment file describing the networks.
* `tripleo_overcloud_network_provision_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_network_provision_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_network_provision_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_network_provision_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_network_provision_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_network_provision_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_network_provision_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_network_provision_home_dir }}/overcloud_network_provision.log"
* `tripleo_overcloud_network_provision_os_cloud`: (String) (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_network_provision_rc_file`.
* `tripleo_overcloud_network_provision_output_file`: (String) Path to an output file.
* `tripleo_overcloud_network_provision_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"

Output Variables
----------------

* `tripleo_overcloud_network_provision_output`: (String) The command standard output.
* `tripleo_overcloud_network_provision_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example network provisioning

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Run overcloud network provision
      import_role:
        name: tripleo_overcloud_network_provision
      var:
        tripleo_overcloud_network_provision_debug: true
        tripleo_overcloud_network_provision_deployment_file: /home/stack/network-data.yaml
```

License
-------

Apache-2.0
