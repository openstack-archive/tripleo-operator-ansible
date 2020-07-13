tripleo_overcloud_failures
==========================

A role to get the deployment failures output.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_failures_debug`: (Boolean) Flag to print out the command that is run. Default: False
* `tripleo_overcloud_failures_os_cloud`: (String) (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_failures_rc_file`.
* `tripleo_overcloud_failures_plan`: (String) The name of the stack/plan. Default: overcloud
* `tripleo_overcloud_failures_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"

NOTE: Please note that this command should be run against the undercloud so the
OS_CLOUD or rc file variables should be set to use the 'undercloud' when
calling this role. If you are not defining `tripleo_os_cloud` or `tripleo_rc_file`,
stackrc will be used by default.

Output Variables
----------------

* `tripleo_overcloud_failures_output`: (String) The command standard output.
* `tripleo_overcloud_failures_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example overcloud failures execution playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Get overcloud failures
      import_role:
        name: tripleo_overcloud_failures
```

License
-------

Apache-2.0
