tripleo_overcloud_roles_generate
========================

A role to run 'openstack overcloud roles generate' for generation of the
roles_data.yaml, from the TripleO Roles defined in the tripleo-heat-templates
roles/ directory.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_roles_generate_debug`: (Boolean) Flag used to enable the debug version of commands. Default: false
* `tripleo_overcloud_roles_generate_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_roles_generate_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_roles_generate_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_roles_generate_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_roles_generate_roles_path`: File system path containing the role yaml files. By default this is in tripleo-heat-templates/roles.
* `tripleo_overcloud_roles_generate_output_file`: File to capture all output to. For example, roles_data.yaml
* `tripleo_overcloud_roles_generate_skip_validate`: Skip role metadata type validation when generating the roles_data.yaml
* `tripleo_overcloud_roles_generate_roles`: REQUIRED - list of roles to use to generate the roles_data.yaml file for the deployment.  NOTE: Ordering is important if no role has the "primary" and "controller" tags. If no role is tagged then the first role listed will be considered the primary role. This usually is the controller role.
* `tripleo_overcloud_roles_generate_os_cloud`: (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default.
  Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_roles_generate_rc_file`.
* `tripleo_overcloud_roles_generate_rc_file`: (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"




Output Variables
----------------

* `tripleo_overcloud_roles_generate_output`: (String) The command standard output.
* `tripleo_overcloud_roles_generate_result`: Ansible shell execution results

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
    - name: Generate overcloud roles_data.yaml
      import_role:
        name: tripleo_overcloud_roles_generate
```

License
-------

Apache-2.0
