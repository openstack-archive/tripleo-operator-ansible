tripleo_overcloud_node_extract_provisioned
=========

A role to extract the currently provisioned nodes in a format compatible with the
tripleo_overcloud_node_provision role.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_node_extract_provisioned_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_overcloud_node_extract_provisioned_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_node_extract_provisioned_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_node_extract_provisioned_log_combine`: (Boolean) Flag to enable captching stderr with stdout. Default: true
* `tripleo_overcloud_node_extract_provisioned_log_output`: (Boolean) Flag to enable logging to a file. Default: true
* `tripleo_overcloud_node_extract_provisioned_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_node_extract_provisioned_home_dir }}/overcloud_node_extract_provisioned.log"
* `tripleo_overcloud_node_extract_provisioned_os_cloud`: (String) (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_node_extract_provisioned_rc_file`.
* `tripleo_overcloud_node_extract_provisioned_output_file`: (String) Path to an output file.
* `tripleo_overcloud_node_extract_provisioned_overwrite_action`: (String) What action to take if `tripleo_overcloud_node_extract_provisioned_output_file` already exists. Can be one of `skip`, `error`, or `overwrite`.
* `tripleo_overcloud_node_extract_provisioned_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"
* `tripleo_overcloud_node_extract_provisioned_stack`: (String) Name or ID of the heat stack.

Output Variables
----------------

* `tripleo_overcloud_node_extract_provisioned_output`: (String) The command standard output.
* `tripleo_overcloud_node_extract_provisioned_result`: Ansible shell execution results

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
    - name: Run overcloud node extract provisioned
      import_role:
        name: tripleo_overcloud_node_extract_provisioned
      var:
        tripleo_overcloud_node_extract_provisioned_debug: true
        tripleo_overcloud_node_extract_provisioned_output_file: /home/stack/deployment.yaml
```

License
-------

Apache-2.0
