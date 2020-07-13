tripleo_overcloud_container_image_tag_discover
=========

IMPORTANT: This role is for use in Queens only. This functionality was replaced
by the `openstack tripleo container image prepare` command in Rocky.

A role to perform a tag discovery for a container.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_container_image_tag_discover_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_overcloud_container_image_tag_discover_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_container_image_tag_discover_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_container_image_tag_discover_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_container_image_tag_discover_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_container_image_tag_discover_image`: (String) REQUIRED. Fully qualified name of the image to discover the tag.
* `tripleo_overcloud_container_image_tag_discover_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_container_image_tag_discover_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_container_image_tag_discover_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_container_image_tag_discover_home_dir }}/overcloud_container_image_tag_discover.log"
* `tripleo_overcloud_container_image_tag_discover_poll`: (Integer) Number of seconds to wait between each checks to see if the command has completed. Default: 10
* `tripleo_overcloud_container_image_tag_discover_tag_from_label`: (String) Label template format
* `tripleo_overcloud_container_image_tag_discover_timeout`: (Integer) Number in seconds to wait for the ansible execution of the command to finish. Default: 3600

Output Variables
----------------

* `tripleo_overcloud_container_image_tag_discover_output`: (String) The command standard output.
* `tripleo_overcloud_container_image_tag_discover_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example tag discover playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Overcloud image tag discover
      import_role:
        name: tripleo_overcloud_container_image_tag_discover
      var:
        tripleo_overcloud_container_image_tag_discover_debug: true
```

License
-------

Apache-2.0
