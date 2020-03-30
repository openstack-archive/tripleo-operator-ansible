tripleo_overcloud_node_bios_reset
=================================

A role to run node BIOS reset.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_node_bios_reset_all_manageable`: Reset BIOS on all nodes currently in 'manageable' state.
* `tripleo_overcloud_node_bios_reset_node_uuids`: Baremetal Node UUIDs for the node(s) to reset BIOS.
* `tripleo_overcloud_node_bios_reset_os_cloud`: (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_node_bios_reset_rc_file`.
* `tripleo_overcloud_node_bios_reset_rc_file`: (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"

NOTE: Please note that this command should be run against the undercloud so the
OS_CLOUD or rc file variables should be set to use the 'undercloud' when
calling this role. If you are not defining `tripleo_os_cloud` or `tripleo_rc_file`,
stackrc will be used by default.

Output Variables
----------------

* `tripleo_overcloud_node_bios_reset_output`: (String) The command standard output.
* `tripleo_overcloud_node_bios_reset_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example overcloud node BIOS reset playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Reset node BIOS
      import_role:
        name: tripleo_overcloud_node_bios_reset
```

License
-------

Apache-2.0
