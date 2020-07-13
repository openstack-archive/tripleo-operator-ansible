tripleo_overcloud_image_build
============================

A role to perform an overcloud image build for provisioning.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_image_build_config_files`: (List) List of YAML config files specifying the image build.
* `tripleo_overcloud_image_build_debug`: (Boolean) Flag to print out the push command. Default: False
* `tripleo_overcloud_image_build_dib_local_image`: (String) String containing the path to a local image to use when building.
* `tripleo_overcloud_image_build_dib_yum_repo_conf`: (String) String containing the path to the yum files for the image building process. Default: "/etc/yum.repos.d/*"
* `tripleo_overcloud_image_build_extra_env_vars`: (Dictionary) Dictionary containing extra environment variables to be set for the build. Default: {}
* `tripleo_overcloud_image_build_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_image_build_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_image_build_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_image_build_home_dir`: (String) Path that the command should be executed in. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_image_build_image_names`: (List) List of image names to build.
* `tripleo_overcloud_image_build_log_combine`: (Boolean) Flag to combine stdout and stderr in the logfile. Default: true
* `tripleo_overcloud_image_build_log_output`: (Boolean) Flag to log the output to a file rather than show it in the ansible output. Default: true
* `tripleo_overcloud_image_build_log`: (String) Install log file path. Default: "{{ tripleo_overcloud_image_build_home_dir }}/overcloud_image_build.log"
* `tripleo_overcloud_image_build_no_skip`: (Boolean) Flag to skip build if cached image exists. Default: False
* `tripleo_overcloud_image_build_output_directory`: (String) Path to the output directory for the images.
* `tripleo_overcloud_image_build_poll`: (Integer) Number of seconds to wait between checks to see if the build command has completed. This should be set to a value greater or equal to 1. Default: 10
* `tripleo_overcloud_image_build_stable_release`: (String) String containing the name of the stable branch being built.
* `tripleo_overcloud_image_build_timeout`: (Integer) Amount of time to wait for the command to complete. Default: 1800

Output Variables
----------------

* `tripleo_overcloud_image_build_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example container push execution playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Build overcloud image
      import_role:
        name: tripleo_overcloud_image_build
      vars:
        tripleo_overcloud_image_build_config_files:
          - /usr/share/openstack-tripleo-common/image-yaml/overcloud-images.yaml
          - /usr/share/openstack-tripleo-common/image-yaml/overcloud-images-centos7.yaml
```

License
-------

Apache-2.0
