tripleo_container_image_prepare
===============================

A role to perform the container image prepare action.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_container_image_prepare_become`: (Boolean) Run the command as root. This needs to be true when uploading to the local undercloud registry. Default: true
* `tripleo_container_image_prepare_cleanup`: (String) Cleanup behavior for local images left after upload. Can be one of full, partial, or none. Default is not set.
* `tripleo_container_image_prepare_debug`: (Boolean) Flag to print out the prepare command. Default: False
* `tripleo_container_image_prepare_dry_run`: (Boolean) Perform a dry run upload which will not perform any push, pull or modify operations. The environment file will still be populated. Default: false
* `tripleo_container_image_prepare_environment_files`: (List) List of environment files. Default: []
* `tripleo_container_image_prepare_environment_directory`: (List) Directories containing environment files. Should not be used if `tripleo_container_image_prepare_environment_files` is defined. Default: []
* `tripleo_container_image_prepare_home_dir`: (String) Home directory for the undercloud user. Default: "{{ ansible_env.HOME }}"
* `tripleo_container_image_prepare_output_env_file`: (String) File to write heat environment file which specifies all image parameters. Default is not set.
* `tripleo_container_image_prepare_output_roles_file`: (String) Roles file path on the remote system. Default is not set.
* `tripleo_container_image_prepare_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_container_image_prepare_timeout`: (Number) Amount of time to wait for the command to conplete. Default: 1800

Output Variables
----------------

* `tripleo_container_image_prepare_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example container prepare execution playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Run container prepare
      import_role:
        name: tripleo_container_image_prepare
      vars:
        tripleo_container_image_prepare_files:
          - /home/stack/container-image-prepare.yaml
```

License
-------

Apache-2.0
