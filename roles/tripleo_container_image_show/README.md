tripleo_container_image_show
============================

A role to perform the container image show against a registry.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_container_image_show_debug`: (Boolean) Flag to print out the show command. Default: False
* `tripleo_container_image_show_format`: (String) The format that the output will be in. By default we specify 'json' so that the output will be parsed in ansible. Default: json
* `tripleo_container_image_show_image`: (String) Image to fetch the details
* `tripleo_container_image_show_password`: (String) Password for the registry
* `tripleo_container_image_show_username`: (String) Username for the registry

Output Variables
----------------

* `tripleo_container_image_show_output`: (Dictionary|String) If tripleo_container_image_show_format is json, the results will automatically be parsed and a dictionary is returned. If another format is used then this will be the response in String format.
* `tripleo_container_image_show_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example container show execution playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: List containers
      import_role:
        name: tripleo_container_image_show
      vars:
        tripleo_container_image_show_image: docker.io/library/centos:7
    - name: Print containers
      debug:
        var: tripleo_container_image_show_output
```

License
-------

Apache-2.0
