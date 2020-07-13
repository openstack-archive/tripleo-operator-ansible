tripleo_overcloud_node_provision
=========

A role to perform overcloud node provisioning with Ironic.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_node_provision_concurrency`: (Integer) Number of nodes to provision at once
* `tripleo_overcloud_node_provision_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_overcloud_node_provision_deployment_file`: (String) REQUIRED. File path to the deployment file describing the nodes.
* `tripleo_overcloud_node_provision_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_node_provision_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_node_provision_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_node_provision_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_node_provision_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_node_provision_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_node_provision_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_node_provision_home_dir }}/overcloud_node_provision.log"
* `tripleo_overcloud_node_provision_os_cloud`: (String) (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_node_provision_rc_file`.
* `tripleo_overcloud_node_provision_output_file`: (String) Path to an output file.
* `tripleo_overcloud_node_provision_overcloud_ssh_key`: (String) Key path for ssh access to overcloud nodes. When not defined, the key will attempt to be auto-detected.
* `tripleo_overcloud_node_provision_overcloud_ssh_user`: (String) User for ssh access to the newly deployed nodes.
* `tripleo_overcloud_node_provision_poll`: (Integer) Number of seconds to wait between each checks to see if the command has completed. Default: 10
* `tripleo_overcloud_node_provision_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"
* `tripleo_overcloud_node_provision_stack`: (String) Name or ID of the heat stack.
* `tripleo_overcloud_node_provision_timeout_arg`: (Integer) Number of seconds to wait for node to complete. Should be smaller than the `overcloud_node_provision_timeout` variable.
* `tripleo_overcloud_node_provision_timeout`: (Integer) Number in seconds to wait for the ansible execution of the command to finish. Default: 3700

Output Variables
----------------

* `tripleo_overcloud_node_provision_output`: (String) The command standard output.
* `tripleo_overcloud_node_provision_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example node provisioning

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Run overcloud node provision
      import_role:
        name: tripleo_overcloud_node_provision
      var:
        tripleo_overcloud_node_provision_debug: true
        tripleo_overcloud_node_provision_deployment_file: /home/stack/deployment.yaml
```

License
-------

Apache-2.0
