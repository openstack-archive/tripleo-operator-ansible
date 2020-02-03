tripleo_overcloud_node_configure
========================

A role to run a node configuration.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_node_configure_node_uuids`: Baremetal Node UUIDs for the node(s) to be configured
* `tripleo_overcloud_node_configure_all_manageable`: Configure all nodes currently in 'manageable' state
* `tripleo_overcloud_node_configure_deploy_kernel`: Image with deploy kernel.
* `tripleo_overcloud_node_configure_deploy_ramdisk`: Image with deploy ramdisk.
* `tripleo_overcloud_node_configure_instance_boot_option`: Whether to set instances for booting from local hard drive (local) or network (netboot).
* `tripleo_overcloud_node_configure_root_device`: Define the root device for nodes.
   Can be either a list of device names (without /dev) to choose from or one of two strategies: largest or smallest.
   For  it to work this command should be run after the introspection.
* `tripleo_overcloud_node_configure_root_device_minimum_size`: Minimum size (in GiB) of the detected root device. Used with --root-device.
* `tripleo_overcloud_node_configure_overwrite_root_device_hints`: Whether to overwrite existing root device hints when --root-device is used.
* `tripleo_overcloud_node_configure_os_cloud`: (String) (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_node_configure_rc_file`.
* `tripleo_overcloud_node_configure_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"

NOTE: Please note that this command should be run against the undercloud so the
OS_CLOUD or rc file variables should be set to use the 'undercloud' when
calling this role. If you are not defining `tripleo_os_cloud` or `tripleo_rc_file`,
stackrc will be used by default.

Output Variables
----------------

* `tripleo_overcloud_node_configure_output`: (String) The command standard output.
* `tripleo_overcloud_node_configure_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example overcloud node configuration playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Configure node
      import_role:
        name: tripleo_overcloud_node_configure
```

License
-------

Apache-2.0
