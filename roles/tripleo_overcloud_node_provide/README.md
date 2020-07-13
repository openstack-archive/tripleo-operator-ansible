tripleo_overcloud_node_provide
==============================

A role to set nodes in a manageable state to available.

Requirements
------------

Requires the username and password found in the ~/stackrc file on the undercloud.

Role Variables
--------------

* `tripleo_overcloud_node_provide_all_manageable`: (Boolean) Provide all nodes in manageable state. REQUIRED if UUIDs are not passed. Default: False
* `tripleo_overcloud_node_provide_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_overcloud_node_provide_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_node_provide_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_node_provide_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_node_provide_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_node_provide_home_dir }}/overcloud_node_provide.log"
* `tripleo_overcloud_node_provide_node_uuids`: (List) List of  UUIDs to provide. REQUIRED if '--all-manageable' is not passed. Default []
* `tripleo_overcloud_node_provide_os_cloud`: (String) (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_node_provide_rc_file`.
* `tripleo_overcloud_node_provide_poll`: (Integer) Number of seconds to wait between each checks to see if the command has completed. Default: 10
* `tripleo_overcloud_node_provide_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"
* `tripleo_overcloud_node_provide_timeout`: (Integer) Number in seconds to wait for the ansible execution of the command to finish. Default: 3600

Output Variables
----------------

* `tripleo_overcloud_node_provide_output`: (String) The command standard output.
* `tripleo_overcloud_node_provide_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example overcloud node provide playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Set overcloud nodes to available (provide nodes)
      import_role:
        name: tripleo_overcloud_node_provide
      vars:
        tripleo_overcloud_node_provide_node_uuids:
          - 4ca0448a-3892-4fc8-aea1-1834ac3c0caa
```

License
-------

Apache-2.0
