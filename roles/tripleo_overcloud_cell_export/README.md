tripleo_overcloud_cell_export
=========

A role to perform an overcloud cell export.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_cell_export_cell_stack`: (String) Name of the controller cell Heat stack to export information from
* `tripleo_overcloud_cell_export_control_plane_stack`: (String) Name of the main Heat stack to export information from.
* `tripleo_overcloud_cell_export_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_overcloud_cell_export_force_overwrite`: (Boolean) Flag to overwrite the output file. Default: false
* `tripleo_overcloud_cell_export_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_cell_export_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_cell_export_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_cell_export_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_cell_export_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_cell_export_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_cell_export_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_cell_export_home_dir }}/overcloud_cell_export.log"
* `tripleo_overcloud_cell_export_name`: (String) REQUIRED. Name of the stack used for additional cell.
* `tripleo_overcloud_cell_export_os_cloud`: (String) (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_cell_export_rc_file`.
* `tripleo_overcloud_cell_export_output_file`: (String) Name of the output file for the cell data export.
* `tripleo_overcloud_cell_export_poll`: (Integer) Number of seconds to wait between each checks to see if the command has completed. Default: 10
* `tripleo_overcloud_cell_export_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"
* `tripleo_overcloud_cell_export_timeout`: (Integer) Number in seconds to wait for the ansible execution of the command to finish. Default: 3600

Output Variables
----------------

* `tripleo_overcloud_cell_export_output`: (String) The command standard output.
* `tripleo_overcloud_cell_export_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example cell export

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: overcloud cell export
      import_role:
        name: tripleo_overcloud_cell_export
      var:
        tripleo_overcloud_cell_export_debug: true
        tripleo_overcloud_cell_export_name: cell1
```

License
-------

Apache-2.0
