tripleo_overcloud_node_delete
========================

A role to run node delete.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_node_delete_nodes`: (List) Node ID(s) to delete (otherwise specified in the --baremetal-deployment file)
* `tripleo_overcloud_node_delete_baremetal_deployment`: Configuration file describing the baremetal deployment
* `tripleo_overcloud_node_delete_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_node_delete_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_node_delete_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_node_delete_home_dir`: (String) Location to run the command in. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_node_delete_stack`: Name or ID of heat stack to scale (default=Env: OVERCLOUD_STACK_NAME)
* `tripleo_overcloud_node_delete_templates`: The directory containing the Heat templates to deploy.
    This argument is deprecated. The command now utilizes a deployment plan, which should be updated prior to running this
    command, should that be required. Otherwise this argument will be silently ignored.
* `tripleo_overcloud_node_delete_environment_file`: Environment files to be passed to the heat stack-create or heat stack-update command.
    (Can be specified more than  once.) This argument is deprecated. The command now utilizes a deployment plan,
    which should be updated prior to running this command, should that be required. Otherwise this argument will be silently ignored.
* `tripleo_overcloud_node_delete_timeout`: Timeout in minutes to wait for the nodes to be deleted.
    Keep in mind that due to keystone session duration that timeout has an upper bound of 4 hours
* `tripleo_overcloud_node_delete_yes`: Skip yes/no prompt (assume yes)
* `tripleo_overcloud_node_delete_os_cloud`: (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_node_delete_rc_file`.
* `tripleo_overcloud_node_delete_rc_file`: (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"

NOTE: Please note that this command should be run against the undercloud so the
OS_CLOUD or rc file variables should be set to use the 'undercloud' when
calling this role. If you are not defining `tripleo_os_cloud` or `tripleo_rc_file`,
stackrc will be used by default.

Output Variables
----------------

* `tripleo_overcloud_node_delete_output`: (String) The command standard output.
* `tripleo_overcloud_node_delete_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example overcloud node delete playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Delete node
      import_role:
        name: tripleo_overcloud_node_delete
```

License
-------

Apache-2.0
