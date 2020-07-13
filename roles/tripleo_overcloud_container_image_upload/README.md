tripleo_overcloud_container_image_upload
========================================

IMPORTANT: This role is for use in Queens only. This functionality was replaced
by the `openstack tripleo container image prepare` command in Rocky.

A role to perform an overcloud container image upload.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_container_image_upload_cleanup`: (String) Cleanup behaviour for local images
* `tripleo_overcloud_container_image_upload_config_files`: (List) REQUIRED. YAML config files specifying images. Default: []
* `tripleo_overcloud_container_image_upload_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_overcloud_container_image_upload_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_container_image_upload_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_container_image_upload_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_container_image_upload_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_container_image_upload_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_container_image_upload_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_container_image_upload_log`: (String) Path to a log file for the command output. Default: "{{ CHANGEME_home_dir }}/CHANGEME.log"
* `tripleo_overcloud_container_image_upload_poll`: (Integer) Number of seconds to wait between each checks to see if the command has completed. Default: 10
* `tripleo_overcloud_container_image_upload_timeout`: (Integer) Number in seconds to wait for the ansible execution of the command to finish. Default: 3600

Output Variables
----------------

* `tripleo_overcloud_container_image_upload_output`: (String) The command standard output.
* `tripleo_overcloud_container_image_upload_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example overcloud container image upload

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: overcloud container image upload
      import_role:
        name: tripleo_overcloud_container_image_upload
      var:
        tripleo_overcloud_container_image_upload_config_files:
          - /home/stack/containers.yaml
        tripleo_overcloud_container_image_upload_debug: true
```

License
-------

Apache-2.0
