tripleo_overcloud_image_upload
========================

A role to run an overcloud image upload.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_image_upload_architecture`: (String) Architecture type for the images being uploaded.
* `tripleo_overcloud_image_upload_debug`: (Boolean) Flag to print out the command that is run. Default: False
* `tripleo_overcloud_image_upload_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_image_upload_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_image_upload_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_image_upload_home_dir`: (String) Home directory for the undercloud user. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_image_upload_http_boot`: (String) Root directory for the ironic-python-agent-image
* `tripleo_overcloud_image_upload_image_path`: (String) Path to directory overcloud images. By default the command will use the images in `tripleo_overcloud_image_upload_home_dir` if this is not specified.
* `tripleo_overcloud_image_upload_image_type`: (String) If specified, restrict the image type to upload. Should be one of {os,ironic-python-agent}
* `tripleo_overcloud_image_upload_ironic_python_agent_name`: (String) OpenStack ironic-python-agent image filename
* `tripleo_overcloud_image_upload_log_combine`: (Boolean) Flag to combine stdout and stderr in the logfile. Default: true
* `tripleo_overcloud_image_upload_log_output`: (Boolean) Flag to log the output to a file rather than show it in the ansible output. Default: true
* `tripleo_overcloud_image_upload_log`: (String) Install log file path. Default: "{{ tripleo_overcloud_image_upload_home_dir }}/overcloud_image_upload.log"
* `tripleo_overcloud_image_upload_os_cloud`: (String) (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_image_upload_rc_file`.
* `tripleo_overcloud_image_upload_os_image_name`: (String) OpenStack disk image filename
* `tripleo_overcloud_image_upload_platform`: (String) Platform type for the images being uploaded.
* `tripleo_overcloud_image_upload_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"
* `tripleo_overcloud_image_upload_update_existing`: (Boolean) Update the images if they already exist. Default: false
* `tripleo_overcloud_image_upload_whole_disk`: (Boolean) Overcloud image being uploaded is considered a whole disk image. Default: false

NOTE: Please note that this command should be run against the undercloud so the
OS_CLOUD or rc file variables should be set to use the 'undercloud' when
calling this role. If you are not defining `tripleo_os_cloud` or `tripleo_rc_file`,
stackrc will be used by default.

Output Variables
----------------

* `tripleo_overcloud_image_upload_output`: (String) The command standard output when `tripleo_overcloud_image_upload_log_output` is set to false.
* `tripleo_overcloud_image_upload_result`: Ansible shell execution results

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
    - name: Get overcloud image_upload
      import_role:
        name: tripleo_overcloud_image_upload
      vars:
        tripleo_overcloud_image_upload_update_existing: true
```

License
-------

Apache-2.0
