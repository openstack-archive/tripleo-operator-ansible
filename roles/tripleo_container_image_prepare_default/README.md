tripleo_container_image_prepare_default
=======================================

A role to generate the default container image prepare information.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_container_image_prepare_default_debug`: (Boolean) Flag to print out the push command. Default: False
* `tripleo_container_image_prepare_default_enable_registry_login`: (Boolean) Flag to enable registry login on nodes if credentials are provided. Default: false
* `tripleo_container_image_prepare_default_home_dir`: (String) Home directory for the undercloud user. Default: "{{ ansible_env.HOME }}"
* `tripleo_container_image_prepare_default_local_push_destination`: (Boolean) Include a push_Destination to trigger upload to a local registry on the undercloud. Default: false
* `tripleo_container_image_prepare_default_output_env_file`: (String) File to write environment file containing default ContainerImagePrepare value. When not set, `tripleo_container_image_prepare_default_output` will contain yaml defining ContainerImagePrepare. Default is not set.

Output Variables
----------------

* `tripleo_container_image_prepare_default_output`: (String) YAML defining a default ContainerImagePrepare value.
* `tripleo_container_image_prepare_default_result`: Ansible execution results

Dependencies
------------

None.

Example Playbook
----------------

Example container prepare default execution playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Generate default ContainerImagePrepare
      import_role:
        name: tripleo_container_image_prepare_default
      vars:
        tripleo_container_image_prepare_output_env_file: /home/stack/container-image-prepare.yaml
```

License
-------

Apache-2.0
