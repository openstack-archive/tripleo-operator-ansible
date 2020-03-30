tripleo_overcloud_node_clean
============================

A role to run node clean.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_node_clean_all_manageable`: Clean all nodes currently in 'manageable' state
* `tripleo_overcloud_node_clean_node_uuids`: Baremetal Node UUIDs for the node(s) to be cleaned
* `tripleo_overcloud_node_clean_os_cloud`: (String) (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_node_clean_rc_file`.
* `tripleo_overcloud_node_clean_provide`: Provide (make available) the nodes once cleaned.
* `tripleo_overcloud_node_clean_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"

NOTE: Please note that this command should be run against the undercloud so the
OS_CLOUD or rc file variables should be set to use the 'undercloud' when
calling this role. If you are not defining `tripleo_os_cloud` or `tripleo_rc_file`,
stackrc will be used by default.

Output Variables
----------------

* `tripleo_overcloud_node_clean_output`: (String) The command standard output.
* `tripleo_overcloud_node_clean_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example overcloud node clean playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Clean node
      import_role:
        name: tripleo_overcloud_node_clean
```

License
-------

Apache-2.0
