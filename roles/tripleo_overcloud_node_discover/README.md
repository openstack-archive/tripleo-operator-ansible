tripleo_overcloud_node_discover
========================

A role to run node discover.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_node_discover_ip`: IP address(es) to probe.
* `tripleo_overcloud_node_discover_range`: IP range to probe.
* `tripleo_overcloud_node_discover_credentials`: Key/value pairs of possible credentials.
* `tripleo_overcloud_node_discover_port`: BMC port(s) to probe.
* `tripleo_overcloud_node_discover_introspect`: (Bool) Introspect the imported nodes.
* `tripleo_overcloud_node_discover_run_validations`: (Bool) Run the pre-deployment validations. These external validations are
   from the TripleO Validations project.
* `tripleo_overcloud_node_discover_provide`: (Bool) Provide (make available) the nodes.
* `tripleo_overcloud_node_discover_no_deploy_image`: (Bool) Skip setting the deploy kernel and ramdisk.
* `tripleo_overcloud_node_discover_instance_boot_option`: Whether to set instances for booting from local hard drive (local)
   or network (netboot).
* `tripleo_overcloud_node_discover_concurrency`: Maximum number of nodes to introspect at once.
* `tripleo_overcloud_node_discover_os_cloud`: (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_node_discover_rc_file`.
* `tripleo_overcloud_node_discover_rc_file`: (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"
* `tripleo_overcloud_node_introspect_node_timeout`: (Integer) Maximum timeout for node introspection.
* `tripleo_overcloud_node_introspect_max_retries`: (Integer) Maximum introspection retries.
* `tripleo_overcloud_node_introspect_retry_timeout`: (Integer) Maximum timeout between introspection retries.

NOTE: Please note that this command should be run against the undercloud so the
OS_CLOUD or rc file variables should be set to use the 'undercloud' when
calling this role. If you are not defining `tripleo_os_cloud` or `tripleo_rc_file`,
stackrc will be used by default.

Output Variables
----------------

* `tripleo_overcloud_node_discover_output`: (String) The command standard output.
* `tripleo_overcloud_node_discover_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example overcloud node discover playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Discover node
      import_role:
        name: tripleo_overcloud_node_discover
```

License
-------

Apache-2.0
