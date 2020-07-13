tripleo_container_image_push
============================

A role to perform the container image push against a registry.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_container_image_push_append_tag`: (String) Tag to append to the existing tag when pushing the container.
* `tripleo_container_image_push_become`: (Boolean) Run the command as root. This needs to be true when uploading to the local undercloud registry. Default: true
* `tripleo_container_image_push_cleanup`: (Boolean) Remove local copy of the image after uploading. Default: false
* `tripleo_container_image_push_debug`: (Boolean) Flag to print out the push command. Default: False
* `tripleo_container_image_push_dry_run`: (Boolean) Perform a dry run upload which will exercise the authentication process but not upload the container. Default: false
* `tripleo_container_image_push_image`: (String) REQUIRED. Container image to upload. Should be in the form of <registry>/<namespace>/<name>:tag. If the tag is not provided, 'latest' is used.
* `tripleo_container_image_push_local`: (Boolean) Use this flag if the container image is already on the current system and does not need to be pulled from a remote registry. Default: false
* `tripleo_container_image_push_multi_arch`: (Boolean) Enable multi arch support for the upload. Default: false
* `tripleo_container_image_push_password`: (String) Password for the registry
* `tripleo_container_image_push_registry_url`: (String) URL of the destination registry in the form <fqdn>:<port>.
* `tripleo_container_image_push_timeout`: (Number) Amount of time to wait for the command to complete. Default: 360
* `tripleo_container_image_push_username`: (String) Username for the registry

Output Variables
----------------

* `tripleo_container_image_push_result`: Ansible shell execution results

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
    - name: Push a container
      import_role:
        name: tripleo_container_image_push
      vars:
        tripleo_container_image_push_image: docker.io/library/centos:7
    - name: Print output
      debug:
        var: tripleo_container_image_push_output
```

License
-------

Apache-2.0
