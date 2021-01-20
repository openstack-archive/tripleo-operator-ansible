tripleo_overcloud_upgrade_converge
==================================

A role to execute an overcloud update converge.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_upgrade_converge_answers_file`: (String) File path to a deployment answers file.
* `tripleo_overcloud_upgrade_converge_baremetal_deployment`: (String) File path to a baremetal deployment configuration.
* `tripleo_overcloud_upgrade_converge_config_download`: (Boolean) Flag to add --config-download option. This is the default as of Rocky and enabling this should have no effect. Default: false
* `tripleo_overcloud_upgrade_converge_config_download_timeout`: (Integer) Timeout in minutes for the config-download steps.
* `tripleo_overcloud_upgrade_converge_debug`: (Boolean) Flag to print out the command that is run. Default: false
* `tripleo_overcloud_upgrade_converge_deployed_server`: (Boolean) Flag to use pre-provisioned nodes. Default: false
* `tripleo_overcloud_upgrade_converge_disable_password_generation`: (Boolean) Flag to disable password generation. Default: false
* `tripleo_overcloud_upgrade_converge_disable_validations`: (Boolean) Flag to disable validations. Default: false
* `tripleo_overcloud_upgrade_converge_dry_run`: (Boolean) Flag to enable dry run. Default: false
* `tripleo_overcloud_upgrade_converge_environment_dirs`: (List) A list of directory paths containing environment files for the deployment. Should not be used with environment files.
* `tripleo_overcloud_upgrade_converge_environment_files`: (List) A list of environment file paths for the deployment.  Should not be used with environment dirs.
* `tripleo_overcloud_upgrade_converge_force_postconfig`: (Boolean) Force the overcloud post-deployment configuration. Default: false
* `tripleo_overcloud_upgrade_converge_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_upgrade_converge_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_upgrade_converge_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_upgrade_converge_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_upgrade_converge_inflight_validations`: (Boolean) Flag to enable in-flight validations. Default: false
* `tripleo_overcloud_upgrade_converge_libvirt_type`: (String) Libvirt domain time. Setting `NovaComputeLibvirtType` in an environment file is preferred over this option.
* `tripleo_overcloud_upgrade_converge_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_upgrade_converge_home_dir }}/overcloud_upgrade_converge.log"
* `tripleo_overcloud_upgrade_converge_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_upgrade_converge_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_upgrade_converge_networks_file`: (String) File path to a networks file for the deployment.
* `tripleo_overcloud_upgrade_converge_no_cleanup`: (Boolean) String to enable no cleanup. Default: false
* `tripleo_overcloud_upgrade_converge_no_config_download`: (Boolean) String to disable the config download software configuration. Default: false
* `tripleo_overcloud_upgrade_converge_no_proxy`: (String) String containing a comma separated list of hosts to skip proxying when http_proxy and https_proxy are used.
* `tripleo_overcloud_upgrade_converge_ntp_server`: (String) String containing a comma separated list of NTP servers. Setting `NtpServer` in an environment file is preferred over this option.
* `tripleo_overcloud_upgrade_converge_os_cloud`: (String) (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_upgrade_converge_rc_file`.
* `tripleo_overcloud_upgrade_converge_output_dir`: (String) Path to a directory to output for the configuration download output.
* `tripleo_overcloud_upgrade_converge_overcloud_ssh_enable_timeout`: (Integer) Timeout for the ssh enable process to finish.
* `tripleo_overcloud_upgrade_converge_overcloud_ssh_key`: (String) Path to an ssh key file to use to access the overcloud nodes.
* `tripleo_overcloud_upgrade_converge_overcloud_ssh_network`: (String) Network name to use for the ssh access to the overcloud nodes.
* `tripleo_overcloud_upgrade_converge_overcloud_ssh_port_timeout`: (Integer) Timeout to wait for the ssh port to become active.
* `tripleo_overcloud_upgrade_converge_overcloud_ssh_user`: (String) User for ssh access to the overcloud nodes.
* `tripleo_overcloud_upgrade_converge_override_ansible_cfg`: (String) File path to an ansible.cfg containing override values.
* `tripleo_overcloud_upgrade_converge_plan_environment_file`: (String) File path to a plan environment file.
* `tripleo_overcloud_upgrade_converge_poll`: (Integer) Number of seconds to wait between each checks to see if the deployment command has completed. Default: 10
* `tripleo_overcloud_upgrade_converge_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"
* `tripleo_overcloud_upgrade_converge_roles_file`: (String) File path to a deployment roles file.
* `tripleo_overcloud_upgrade_converge_run_validations`: (Boolean) Flag to enable running validations. Default: false
* `tripleo_overcloud_upgrade_converge_skip_deploy_identifier`: (Boolean) Flag to enable skip deploy identifier. Default: false
* `tripleo_overcloud_upgrade_converge_skip_postconfig`: (Boolean) Flag to enable skip postconfig. Default: false
* `tripleo_overcloud_upgrade_converge_stack`: (String) Name of the stack to deploy. Default: overcloud
* `tripleo_overcloud_upgrade_converge_templates`: (String) Path to a directory containing the tripleo-heat-templates for the deployment. Default: /usr/share/openstack-tripleo-heat-templates
* `tripleo_overcloud_upgrade_converge_timeout`: (Integer) Number in seconds to wait for the ansible execution of the deployment command to finish. This should be larger than the `tripleo_overcloud_upgrade_converge_timeout_arg` value. Default: 5700
* `tripleo_overcloud_upgrade_converge_timeout_arg`: (Integer) Number in minutes for the deployment to run. Default: 90
* `tripleo_overcloud_upgrade_converge_validation_errors_nonfatal`: (Boolean) Flag to make validation errors not fatal. Default: false
* `tripleo_overcloud_upgrade_converge_validation_warnings_fatal`: (Boolean) Flag to make validation warnings fatal. Default: false

NOTE: Please note that this command should be run against the undercloud so the
OS_CLOUD or rc file variables should be set to use the 'undercloud' when
calling this role. If you are not defining `tripleo_os_cloud` or `tripleo_rc_file`,
stackrc will be used by default.

Output Variables
----------------

* `tripleo_overcloud_upgrade_converge_output`: (String) The command standard output.
* `tripleo_overcloud_upgrade_converge_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example overcloud upgrade converge execution playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Run overcloud upgrade converge
      import_role:
        name: tripleo_overcloud_upgrade_converge
      vars:
        tripleo_overcloud_upgrade_converge_environment_files:
           - /usr/share/openstack-tripleo-heat-templates/environments/enable-swap.yaml
```

License
-------

Apache-2.0
