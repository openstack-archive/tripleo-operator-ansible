tripleo_overcloud_container_image_build
=======================================

A role to perform the container image build process.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_container_image_build_config_files`: (List) YAML Config file(s) specifyign the image to build. Default: []
* `tripleo_overcloud_container_image_build_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_overcloud_container_image_build_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_container_image_build_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_container_image_build_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_container_image_build_excludes`: (List) Name of containers to exclude from the build. Default: []
* `tripleo_overcloud_container_image_build_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_container_image_build_kolla_config_file`: (String) Path to Kolla config file.
* `tripleo_overcloud_container_image_build_list_dependencies`: (Boolean) Show the image build dependencies instead of building. Default: false
* `tripleo_overcloud_container_image_build_list_images`: (Boolean) Show the images which would be built rather than building. Default: false
* `tripleo_overcloud_container_image_build_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_container_image_build_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_container_image_build_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_container_image_build_home_dir }}/overcloud_container_image_build.log"
* `tripleo_overcloud_container_image_build_poll`: (Integer) Number of seconds to wait between each checks to see if the command has completed. Default: 10
* `tripleo_overcloud_container_image_build_timeout`: (Integer) Number in seconds to wait for the ansible execution of the command to finish. Default: 3600
* `tripleo_overcloud_container_image_build_use_buildah`: (Boolean) Use Buildah instead of Docker to build. Default: false
* `tripleo_overcloud_container_image_build_work_dir`: (String) Tripleo container builds directory.

Output Variables
----------------

* `tripleo_overcloud_container_image_build_output`: (String) The command standard output.
* `tripleo_overcloud_container_image_build_result`: Ansible shell execution results

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
        name: tripleo_overcloud_container_image_build
      var:
        tripleo_overcloud_container_image_build_debug: true
```

License
-------

Apache-2.0
