tripleo_config_generate_ansible
===============================

A role to generate the default ansible.cfg for a deployment.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_config_generate_ansible_debug`: (Boolean) Flag used to enable the debug version of commands. Default: false
* `tripleo_config_generate_ansible_deployment_user`: (String) Deployment user to use. Default: "{{ ansible_user }}"
* `tripleo_config_generate_ansible_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_config_generate_ansible_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_config_generate_ansible_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_config_generate_ansible_home_dir`: (String) Directory to run the command in. This is the default location for the output if `tripleo_config_generate_ansible_output_dir` is not specified.. Default: "{{ ansible_env.HOME }}"
* `tripleo_config_generate_ansible_os_cloud`: (String) OS_CLOUD value to use when running the command. If tripleo_os_cloud is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_config_generate_ansible_rc_file`.
* `tripleo_config_generate_ansible_output_dir`: (String) Directory to output ansible.cfg and ansible.log files.
* `tripleo_config_generate_ansible_rc_file`: (String) Path to the credential file to use. If tripleo_rc_file is defined, it will be the default. Default: "{{ ansible_env.HOME }}/overcloudrc"

Output Variables
----------------

* `tripleo_config_generate_ansible_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example install execution playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Generate default ansible config
      import_role:
        name: tripleo_config_generate_ansible
```

License
-------

Apache-2.0
