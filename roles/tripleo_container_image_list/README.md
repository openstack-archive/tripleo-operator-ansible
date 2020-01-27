tripleo_container_image_list
============================

A role to perform the container image list against a registry.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_container_image_list_debug`: (Boolean) Flag to print out the list command. Default: False
* `tripleo_container_image_list_format`: (String) The format that the output will be in. By default we specify 'json' so that the output will be parsed in ansible. Default: json
* `tripleo_container_image_list_password`: (String) Password for the registry
* `tripleo_container_image_list_registry`: (String) Registry to run the list against
* `tripleo_container_image_list_username`: (String) Username for the registry

Output Variables
----------------

* `tripleo_container_image_list_output`: (List|String) If tripleo_container_image_list_format is JSON, the results will automatically be parsed and a list is returned. If another format is used then this will be the response in String format.
* `tripleo_container_image_list_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example container list execution playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: List containers
      import_role:
        name: tripleo_container_image_list
    - name: Print containers
      debug:
        msg: "{{ item['Image Name'] }}"
      loop: "{{ tripleo_container_image_list_output }}"
```

License
-------

Apache-2.0
