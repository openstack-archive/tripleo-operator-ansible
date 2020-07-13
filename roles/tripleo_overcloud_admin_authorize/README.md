tripleo_overcloud_admin_authorize
=================================

A role to run the overcloud admin authorize action.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_admin_authorize_debug`: (Boolean) Flag used to enable the debug version of commands. Default: false
* `tripleo_overcloud_admin_authorize_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_admin_authorize_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_admin_authorize_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_admin_authorize_home_dir`: (String) Location to execute the command in. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_admin_authorize_os_cloud`: (String) OS_CLOUD value to use when running the command. If tripleo_os_cloud is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_admin_authorize_rc_file`.
* `tripleo_overcloud_admin_authorize_output_dir`: (String) Directory to output ansible.cfg and ansible.log files. If not specified, will output to the `tripleo_overcloud_admin_authorize_home_dir`.
* `tripleo_overcloud_admin_authorize_poll`: (Integer) Number of seconds to wait between each checks to see if the deployment command has completed. Default: 10
* `tripleo_overcloud_admin_authorize_rc_file`: (String) Path to the credential file to use. If tripleo_rc_file is defined, it will be the default. Default: "{{ ansible_env.HOME }}/overcloudrc"
* `tripleo_overcloud_admin_authorize_ssh_enable_timeout`: (Integer) Timeout for the ssh enable process to finish (Train version only)
* `tripleo_overcloud_admin_authorize_ssh_key`: (String) Path to ssh key for the overcloud nodes.
* `tripleo_overcloud_admin_authorize_ssh_network`: (String) Network name to use for ssh access to the overcloud nodes.
* `tripleo_overcloud_admin_authorize_ssh_port_timeout`: (Integer) Timeout for the ssh port to become active.
* `tripleo_overcloud_admin_authorize_ssh_user`: (String) User for ssh access to overcloud nodes
* `tripleo_overcloud_admin_authorize_stack`: (String) Name or ID of the heat stack
* `tripleo_overcloud_admin_authorize_timeout`: (Integer) Number in seconds to wait for the ansible execution of the deployment command to finish. Default: 3600

Output Variables
----------------

* `tripleo_overcloud_admin_authorize_output`: (String) The command standard output.
* `tripleo_overcloud_admin_authorize_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example execution playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Deploy the ssh key for the overcloud
      import_role:
        name: tripleo_overcloud_admin_authorize
      vars:
        tripleo_overcloud_admin_authorize_stack: overcloud
        tripleo_overcloud_admin_authorize_ssh_user: admin
        tripleo_overcloud_admin_authorize_ssh_key: "/home/stack/my_key.pub"
```

License
-------

Apache-2.0
