tripleo_overcloud_config_download
=================================

A role to perform an overcloud config download.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_config_download_config_dir`: (String) Directory where the files will be downloaded to
* `tripleo_overcloud_config_download_config_type`: (String) Type of object config to extract from the deployment
* `tripleo_overcloud_config_download_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_overcloud_config_download_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_overcloud_config_download_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_overcloud_config_download_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_overcloud_config_download_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_config_download_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_config_download_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_config_download_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_config_download_home_dir }}/overcloud_config_download.log"
* `tripleo_overcloud_config_download_name`: (String) Name of the plan
* `tripleo_overcloud_config_download_no_preserve_config`: (Boolean) If set to `true` the config dir will be removed prior to download. Default: false
* `tripleo_overcloud_config_download_os_cloud`: (String) (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_config_download_rc_file`.
* `tripleo_overcloud_config_download_poll`: (Integer) Number of seconds to wait between each checks to see if the command has completed. Default: 10
* `tripleo_overcloud_config_download_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"
* `tripleo_overcloud_config_download_timeout`: (Integer) Number in seconds to wait for the ansible execution of the command to finish. Default: 3600

Output Variables
----------------

* `tripleo_overcloud_config_download_output`: (String) The command standard output.
* `tripleo_overcloud_config_download_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example config download

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: overcloud config download
      import_role:
        name: tripleo_overcloud_config_download
      var:
        tripleo_overcloud_config_download_debug: true
        tripleo_overcloud_config_download_name: overcloud
        tripleo_overcloud_config_download_config_dir: /home/stack/config
```

License
-------

Apache-2.0
