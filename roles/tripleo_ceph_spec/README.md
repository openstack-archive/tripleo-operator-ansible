tripleo_ceph_spec
=====================

A role to generate Ceph spec files.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_ceph_spec_become`: (Boolean) Execute command with escalated privileges. Default: false
* `tripleo_ceph_spec_crush_hierarchy`: (String) Path to an existing crush hierarchy spec file.
* `tripleo_ceph_spec_debug`: (Boolean) Flag to print out the command that is run. Default: false
* `tripleo_ceph_spec_deployed_baremetal`: (String) Path to the environment file output from "openstack overcloud node provision". This argument may be excluded only if tripleo_ceph_spec_standalone is True.
* `tripleo_ceph_spec_file`: "{{ ansible_env.HOME }}/ceph_spec.yaml"
* `tripleo_ceph_spec_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_ceph_spec_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_ceph_spec_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_ceph_spec_mon_ip`: (String) IP address of the first Ceph monitor. Only supported if tripleo_ceph_spec_standalone is True.
* `tripleo_ceph_spec_osd_spec`: (String) Path to an existing OSD spec file. When the Ceph spec file is generated its OSD spec defaults to {data_devices: {all: true}} for all service_type osd. Use this parameter to override the data_devices value inside the Ceph spec file.
* `tripleo_ceph_spec_overwrite`: (Boolean) Flag to skip yes/no prompts about overwriting the tripleo_ceph_spec_file from a previous run. Default: false
* `tripleo_ceph_spec_poll`: (Integer) Number of seconds to wait between each checks to see if the deployment command has completed. Default: 10
* `tripleo_ceph_spec_roles_file`: (String) Path to an alternative roles_data.yaml. Used to decide which node gets which Ceph mon, mgr, or osd service based on the node's role tripleo_ceph_spec_deployed_baremetal.
* `tripleo_ceph_spec_stack`: Name or ID of heat stack. Used to find the working directory.
* `tripleo_ceph_spec_standalone`: (Boolean) Create a spec file for a standalone deployment. Used for single server development or testing environments.
* `tripleo_ceph_spec_timeout_arg`: (Integer) Number in minutes for the deployment to run. Default: 90
* `tripleo_ceph_spec_timeout`: (Integer) Number in seconds to wait for the ansible execution of the deployment command to finish. This should be larger than the `tripleo_ceph_spec_timeout_arg` value. Default: 5700
* `tripleo_ceph_spec_working_dir`: (String) The working directory for the deployment where all input, output, and generated files will be stored. Defaults to "$HOME/overcloud-deploy/<stack>"


Output Variables
----------------

* `tripleo_ceph_spec_output`: (String) The command standard output.
* `tripleo_ceph_spec_result`: Ansible shell execution results


Dependencies
------------

None.

Example Playbook
----------------

Example ceph spec playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Create Ceph Spec for Standalone
      include_role:
        name: tripleo_ceph_spec
      vars:
        tripleo_ceph_spec_standalone: True
        tripleo_ceph_spec_mon_ip: 192.168.122.42
        tripleo_ceph_spec_file: /home/stack/ceph_spec.yaml
        tripleo_ceph_spec_overwrite: True

    - name: Create Ceph Spec from 'openstack overcloud node provision' output
      include_role:
        name: tripleo_ceph_spec
      vars:
        tripleo_ceph_spec_debug: True
        tripleo_ceph_spec_generate_scripts: True
        tripleo_ceph_spec_overwrite: True
        tripleo_ceph_spec_stack: overcloud
        tripleo_ceph_spec_roles_file: /home/stack/custom_roles.yaml
        tripleo_ceph_spec_file: /home/stack/ceph_spec.yaml
        tripleo_ceph_spec_deployed_baremetal: /home/stack/overcloud-baremetal-deployed.yaml
```

License
-------

Apache-2.0
