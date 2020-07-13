tripleo_overcloud_container_image_prepare
=========================================

IMPORTANT: This role is for use in Queens only. This functionality was replaced
by the `openstack tripleo container image prepare` command in Rocky.

A role to perform the overcloud container image prepare.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_container_image_prepare_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_overcloud_container_image_prepare_environment_directory`: (String) Path to a directory containing the environment files specifying which services are containerized.
* `tripleo_overcloud_container_image_prepare_environment_files`: (List) List of environment files specifying which services are containerized. Default: []
* `tripleo_overcloud_container_image_prepare_excludes`: (List) List of patterns to match the image name against to exclude from the output. Default: []
* `tripleo_overcloud_container_image_prepare_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_container_image_prepare_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_container_image_prepare_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_container_image_prepare_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_container_image_prepare_includes`: (List) List of patterns to match the image name against to include in the output. Default: []
* `tripleo_overcloud_container_image_prepare_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_container_image_prepare_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_container_image_prepare_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_container_image_prepare_home_dir }}/overcloud_container_image_prepare.log"
* `tripleo_overcloud_container_image_prepare_modify_role`: (String) Name of ansible role to run between every image pull and push.
* `tripleo_overcloud_container_image_prepare_modify_vars`: (String) Ansible variables file containing variables to use when using modify role.
* `tripleo_overcloud_container_image_prepare_namespace`: (String) Override the default namespace substitution
* `tripleo_overcloud_container_image_prepare_output_env_file`: (String) Output heat environment file which specifies all image parameters.
* `tripleo_overcloud_container_image_prepare_output_images_file`: (String) Path to write the output image entries to.
* `tripleo_overcloud_container_image_prepare_poll`: (Integer) Number of seconds to wait between each checks to see if the command has completed. Default: 10
* `tripleo_overcloud_container_image_prepare_prefix`: (String) Override the default name prefix substitution
* `tripleo_overcloud_container_image_prepare_push_destination`: (String) Location of image registry to push images to
* `tripleo_overcloud_container_image_prepare_roles_file`: (String) Roles file path for the cloud.
* `tripleo_overcloud_container_image_prepare_set`: (List) Set the value of a variable in the template even if it has no dedicated argument. Default: []
* `tripleo_overcloud_container_image_prepare_suffix`: (String) Override the default name suffix substitution
* `tripleo_overcloud_container_image_prepare_tag_from_label`: (String) Use the value of the specify label to discover the tag
* `tripleo_overcloud_container_image_prepare_tag`: (String) Override the default tag substitution
* `tripleo_overcloud_container_image_prepare_template_file`: (String) YAML template file for image config
* `tripleo_overcloud_container_image_prepare_timeout`: (Integer) Number in seconds to wait for the ansible execution of the command to finish. Default: 3600

Output Variables
----------------

* `tripleo_overcloud_container_image_prepare_output`: (String) The command standard output.
* `tripleo_overcloud_container_image_prepare_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example overcloud container image prepare.

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Overcloud container image prepare
      import_role:
        name: tripleo_overcloud_container_image_prepare
      var:
        tripleo_overcloud_container_image_prepare_debug: true
```

License
-------

Apache-2.0
