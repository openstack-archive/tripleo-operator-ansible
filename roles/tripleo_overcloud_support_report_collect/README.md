tripleo_overcloud_support_report_collect
========================================

A role to run support report collection.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_support_report_collect_debug`: (Boolean) Flag used to enable the debug version of commands. Default: false
* `tripleo_overcloud_support_report_collect_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_support_report_collect_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_support_report_collect_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_support_report_collect_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_support_report_collect_server_name`: Server name, group name, or partial name to match. For example "Controller" will match all controllers for an environment.
* `tripleo_overcloud_support_report_collect_output_dir`: Output directory for the report.
* `tripleo_overcloud_support_report_collect_os_cloud`: (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_support_report_collect_rc_file`.
* `tripleo_overcloud_support_report_collect_rc_file`: (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"

NOTE: Please note that this command should be run against the undercloud so the
OS_CLOUD or rc file variables should be set to use the 'undercloud' when
calling this role. If you are not defining `tripleo_os_cloud` or `tripleo_rc_file`,
stackrc will be used by default.

Output Variables
----------------

* `tripleo_overcloud_support_report_collect_output`: (String) The command standard output.
* `tripleo_overcloud_support_report_collect_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example overcloud support report collecting playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Report support
      import_role:
        name: tripleo_overcloud_support_report_collect
```

License
-------

Apache-2.0
