tripleo_container_image_build
=============================

A role to perform the container image build process.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_container_image_build_authfile`: (String) Path of the authentication file. Default: ''
* `tripleo_container_image_build_base`: (String) Name of the base image. Can also specify a tag , e.g. ubi8:latest. Default: ''
* `tripleo_container_image_build_config_file`: (String) YAML Config file specifying the images to build. Default: ''
* `tripleo_container_image_build_config_path`: (String) YAML Config path where image configs are stored. Default: ''
* `tripleo_container_image_build_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_container_image_build_distro`: (String) Ability to override the distro name; e.g. rhel. Default: ''
* `tripleo_container_image_build_excludes`: (List) Name of containers to exclude from the build. Default: []
* `tripleo_container_image_build_extra_config`: (String) YAML Config file specifying the extra metadata to override; e.g. labels. Default: ''
* `tripleo_container_image_build_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_container_image_build_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_container_image_build_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_container_image_build_home_dir` (String): Path to the home directory. Default: {{ ansible_env.HOME }}
* `tripleo_container_image_build_log` (String): Path to the log file. Default to {{ tripleo_container_image_build_home_dir }}/container_image_build.log
* `tripleo_container_image_build_log_combine`: (Boolean) Whether or not we combine the logs. Default: True
* `tripleo_container_image_build_log_output`: (Boolean) Whether or not we output the logs. Default: True
* `tripleo_container_image_build_namespace`: (String) Namespace for the container images. Default: ''
* `tripleo_container_image_build_poll`: (Integer) Number of seconds to wait between each checks to see if the command has completed. Default: 10
* `tripleo_container_image_build_prefix`: (String) Prefix for the container images names. Default: ''
* `tripleo_container_image_build_push`: (Boolean) Whether or not we push the container images to the registry. Default: False
* `tripleo_container_image_build_registry`: (String) URL of the container image registry. Default: ''
* `tripleo_container_image_build_skip_build`: (Boolean) Whether or not we skip the container image build and just generate configs. Default: False
* `tripleo_container_image_build_tag`: (String) Tag for the container images. Default: ''
* `tripleo_container_image_build_timeout`: (Integer) Number in seconds to wait for the ansible execution of the build command to finish. Default: 5700
* `tripleo_container_image_build_volumes`: (List) Volume to bind mount during the container image builds. Default: []
* `tripleo_container_image_build_work_dir`: (String) Tripleo container builds directory.

Output Variables
----------------

* `tripleo_container_image_build_output`: (String) The command standard output.
* `tripleo_container_image_build_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example container images build.

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Build containers
      import_role:
        name: tripleo_container_image_build
      var:
        tripleo_container_image_build_debug: true
```

License
-------

Apache-2.0
