tripleo_deploy
==============

A role to execute a single node standalone deployment.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_deploy_become`: (Boolean) Execute command with escalated privileges. Default: true
* `tripleo_deploy_cleanup`: (Boolean) Cleanup temporary files after execution. Default: false
* `tripleo_deploy_control_virtual_ip`: (String) Control plain VIP address.
* `tripleo_deploy_debug`: (Boolean) Flag to print out the command that is run. Default: false
* `tripleo_deploy_debug_arg`: (Boolean) Flag for ansible to use -vv. Default: false
* `tripleo_deploy_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_deploy_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_deploy_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_deploy_deployment_python_interpreter`: (String) Path to a python interpreter for the deployment actions.
* `tripleo_deploy_deployment_user`: (String) User who is executing the tripleo deployment via sudo. Defaults: "{{ ansible_env.USER }}"
* `tripleo_deploy_environment_files`: (List) A list of environment file paths for the deployment.
* `tripleo_deploy_force_stack_create`: (Boolean) Flag to force stack create. Default: false
* `tripleo_deploy_force_stack_update`: (Boolean) Flag to force stack update. Default: false
* `tripleo_deploy_heat_api_port`: (Number) Heat API port to use for the installer.
* `tripleo_deploy_heat_container_image`: (String) Full container image location for the openstack-heat-all container.
* `tripleo_deploy_heat_user`: (String) User to execute the non-privileged heat-all process.
* `tripleo_deploy_hieradata_override`: (String) Path to hiera data override file.
* `tripleo_deploy_home_dir`: (String) Path to the directory to execute the command in. Default: "{{ ansible_env.HOME }}"
* `tripleo_deploy_inflight_validations`: (Boolean) Flag to enable in-flight validations. Default: false
* `tripleo_deploy_keep_running`: (Boolean) Flag to keep the heat instance running after the deploy has run. Default: false
* `tripleo_deploy_local_domain`: (String): Local domain for standalone cloud and the endpoints.
* `tripleo_deploy_local_ip`: (String) Local IP address to use for the cloud traffic. REQUIRED.
* `tripleo_deploy_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_deploy_home_dir }}/overcloud_deploy.log"
* `tripleo_deploy_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_deploy_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_deploy_networks_file`: (String) File path to a networks file for the deployment.
* `tripleo_deploy_output_dir`: (String) Directory to write output data to.
* `tripleo_deploy_output_only`: (String) Flag to skip ansible execution and only output the deployment scripts. Default: false
* `tripleo_deploy_plan_environment_file`: (String) File path to a plan environment file.
* `tripleo_deploy_poll`: (Integer) Number of seconds to wait between each checks to see if the deployment command has completed. Default: 10
* `tripleo_deploy_public_virtual_ip`: (String) Public network VIP.
* `tripleo_deploy_roles_file`: (String) File path to a deployment roles file.
* `tripleo_deploy_stack`: (String) Name for ephemeral stack. Default: standalone
* `tripleo_deploy_standalone`: (Boolean) Flag to indicate that a standalone cloud is being deployed. Default: true
* `tripleo_deploy_standalone_role`: (String) Role name to deploy. Default: Standalone
* `tripleo_deploy_templates`: (String) Path to the directory containing heat templates for the deployment. Default: /usr/share/openstack-tripleo-heat-templates
* `tripleo_deploy_timeout`: (Integer) Number in seconds to wait for the ansible execution of the deployment command to finish. This should be larger than the `tripleo_deploy_timeout_arg` value. Default: 5700
* `tripleo_deploy_timeout_arg`: (Integer) Number in minutes for the deployment to run. Default: 90
* `tripleo_deploy_upgrade`: (Boolean) Flag to indicate upgrade an existing deployment. Default: true
* `tripleo_deploy_yes`: (Boolean) Flag to skip yes/no prompts. Default: true

Output Variables
----------------

* `tripleo_deploy_output`: (String) The command standard output.
* `tripleo_deploy_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example overcloud deploy execution playbook

```yaml
- hosts: standalone
  gather_facts: true
  tasks:
    - name: Run standalone deploy
      import_role:
        name: tripleo_deploy
      vars:
        tripleo_deploy_local_ip: 192.168.24.2/24
        tripleo_deploy_environment_files:
           - /usr/share/openstack-tripleo-heat-templates/environments/enable-swap.yaml
```

License
-------

Apache-2.0
