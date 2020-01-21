tripleo_overcloud_export
========================

A role to run an overcloud export.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_export_config_download_dir`: (String) Directory for config-download export data.
* `tripleo_overcloud_export_debug`: (Boolean) Flag to print out the command that is run. Default: False
* `tripleo_overcloud_export_force_overwrite`: (Boolean) Overwrite the output file if it exists. Default: false
* `tripleo_overcloud_export_no_password_excludes`: (Boolean) Do not exclude certain passwords from the export. Default: false
* `tripleo_overcloud_export_os_cloud`: (String) (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_export_rc_file`.
* `tripleo_overcloud_export_output_file`: (String) Name of the output file for the stack data export.
* `tripleo_overcloud_export_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"
* `tripleo_overcloud_export_stack`: (String) The name of the stakc/plan. Default: overcloud

NOTE: Please note that this command should be run against the undercloud so the
OS_CLOUD or rc file variables should be set to use the 'undercloud' when
calling this role. If you are not defining `tripleo_os_cloud` or `tripleo_rc_file`,
stackrc will be used by default.

Output Variables
----------------

* `tripleo_overcloud_export_output`: (String) The command standard output.
* `tripleo_overcloud_export_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example overcloud export execution playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Get overcloud export
      import_role:
        name: tripleo_overcloud_export
      vars:
        tripleo_overcloud_export_stack: overcloud
```

License
-------

Apache-2.0
