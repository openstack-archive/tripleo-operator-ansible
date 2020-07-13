tripleo_overcloud_node_import
=================================

A role to run node import.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_node_import_concurrency`: (Integer) Max number of nodes to introspect at once.
* `tripleo_overcloud_node_import_debug`: (Boolean) Flag used to enable the debug version of commands. Default: false
* `tripleo_overcloud_node_import_environment_file`: (String) Path to the file that contains the baremetal node information. Can be a JSON, YAML or CSV file. Default: environment.json
* `tripleo_overcloud_node_import_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_node_import_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_node_import_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_node_import_home_dir`: (String) Path to the directory to execute the command in. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_node_import_http_boot`: (String) Root directory for the ironic-python-agent image.
* `tripleo_overcloud_node_import_instance_boot_option`: (String) Whether to set instances for booting from local hard drive (local) or network (netboot).
* `tripleo_overcloud_node_import_introspect`: (Boolean) Flag to enable introspection of the nodes when importing. Default: false
* `tripleo_overcloud_node_import_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_node_import_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_node_import_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_node_import_home_dir }}/overcloud_node_import.log"
* `tripleo_overcloud_node_import_no_deploy_image`: (Boolean) Flag to skip setting the deploy kernel and ramdisk. Default: false
* `tripleo_overcloud_node_import_os_cloud`: (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_node_import_rc_file`.
* `tripleo_overcloud_node_import_poll`: (Integer) Number of seconds to wait between each checks to see if the deployment command has completed. Default: 10
* `tripleo_overcloud_node_import_provide`: (Boolean) Flag to provide the nodes. Default: false
* `tripleo_overcloud_node_import_rc_file`: (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"
* `tripleo_overcloud_node_import_run_validations`: (Boolean) Flag to runt he pre-deployment validations. false
* `tripleo_overcloud_node_import_timeout`: (Integer) Time in seconds to wait for the command to complete. Default: 900
* `tripleo_overcloud_node_import_validate_only`: (Boolean) Flag to validate the environment file and exit without running the import. Default: false

NOTE: Please note that this command should be run against the undercloud so the
OS_CLOUD or rc file variables should be set to use the 'undercloud' when
calling this role. If you are not defining `tripleo_os_cloud` or `tripleo_rc_file`,
stackrc will be used by default.

Output Variables
----------------

* `tripleo_overcloud_node_import_output`: (String) The command standard output.
* `tripleo_overcloud_node_import_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example overcloud node import playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Introspect node
      import_role:
        name: tripleo_overcloud_node_import
```

License
-------

Apache-2.0
