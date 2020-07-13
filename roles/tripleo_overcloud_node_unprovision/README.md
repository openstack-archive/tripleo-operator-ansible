tripleo_overcloud_node_unprovision
=========

A role to perform unprovisioning of nodes using Ironic.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_overcloud_node_unprovision_all`: (Boolean) Unprovision every instance in the deployment. Defaults: false
* `tripleo_overcloud_node_unprovision_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_overcloud_node_unprovision_deployment_file`: (String) REQUIRED. Configuration file describing the baremetal deployment.
* `tripleo_overcloud_node_unprovision_home_dir`: (String) Home directory to where the command is run from. Default: "{{ ansible_env.HOME }}"
* `tripleo_overcloud_node_unprovision_log_combine`: (Boolean) Flag to enable capturing stderr with stdout. Default: true
* `tripleo_overcloud_node_unprovision_log_output`: (Boolean) Flag to enable logging to a file. Since the output of this command can be large, it is not recommended to disable this. Default: true
* `tripleo_overcloud_node_unprovision_log`: (String) Path to a log file for the command output. Default: "{{ tripleo_overcloud_node_unprovision_home_dir }}/overcloud_node_unprovision.log"
* `tripleo_overcloud_node_unprovision_os_cloud`: (String) (String) OS_CLOUD value to use when running the command. If `tripleo_os_cloud` is defined, it will be the default. Otherwise the default is ''. This variable takes precedence over `tripleo_overcloud_node_unprovision_rc_file`.
* `tripleo_overcloud_node_unprovision_poll`: (Integer) Number of seconds to wait between each checks to see if the command has completed. Default: 10
* `tripleo_overcloud_node_unprovision_rc_file`: (String) (String) Path to the credential file to use. If `tripleo_rc_file` is defined, it will be the default. Default: "{{ ansible_env.HOME }}/stackrc"
* `tripleo_overcloud_node_unprovision_stack`: (String) Name or ID of the heat stack
* `tripleo_overcloud_node_unprovision_timeout`: (Integer) Number in seconds to wait for the ansible execution of the command to finish. Default: 3600
* `tripleo_overcloud_node_unprovision_yes`: (Boolean) Skip yes/no prompt. Default: true

Output Variables
----------------

* `tripleo_overcloud_node_unprovision_output`: (String) The command standard output.
* `tripleo_overcloud_node_unprovision_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example unprovision

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Run overcloud node unprovision
      import_role:
        name: tripleo_overcloud_node_unprovision
      var:
        tripleo_overcloud_node_unprovision_debug: true
        tripleo_overcloud_node_unprovision_deployment_file: /home/stack/deployment.yaml
        tripleo_overcloud_node_unprovision_all: true
```

License
-------

Apache-2.0
