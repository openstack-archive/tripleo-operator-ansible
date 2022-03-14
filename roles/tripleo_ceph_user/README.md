tripleo_ceph_user
=================

A role to enable or disable a ceph-admin SSH user used by cephadm on overcloud nodes.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_ceph_user_enable`: (Boolean) Enable user and distribute SSH key pairs when true. If `tripleo_ceph_user_enable` is false and a valid FSID is passed with `tripleo_ceph_user_fsid`, then the ceph-admin user is disabled (by removing their SSH keys) and cephadm is disabled. If `tripleo_ceph_user_enable` is true and a valid FSID is passed with `tripleo_ceph_user_fsid` and the user has been disabled, cephadm will be re-enabled for the Ceph cluster idenified by the FSID. Default: true
* `tripleo_ceph_user_fsid`: (String) The FSID of the Ceph cluster to be disabled or re-enabled. If the user disable option has been used (when `tripleo_ceph_user_enable` is false), the FSID may be passed with `tripleo_ceph_user_enable` set to true so that cephadm will be re-enabled for the Ceph cluster idenified by the FSID.
* `tripleo_ceph_user_become`: (Boolean) Execute command with escalated privileges. Default: false
* `tripleo_ceph_user_debug`: (Boolean) Flag to print out the command that is run. Default: false
* `tripleo_ceph_user_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_ceph_user_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_ceph_user_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_ceph_user_poll`: (Integer) Number of seconds to wait between each checks to see if the deployment command has completed. Default: 10
* `tripleo_ceph_user_spec`: (String) Path to an existing Ceph spec file which describes the Ceph cluster where the cephadm SSH user will be created (if necessary) and have their public and private keys installed. Spec file is necessary to determine which nodes to modify and if a public or private key is required. Defaults to "{{ ansible_env.HOME }}/ceph_spec.yaml".
* `tripleo_ceph_user_ssh_user`: (String) Name of the SSH user used by cephadm. Warning: if this option is used, it must be used consistently for every 'openstack overcloud ceph' call. Defaults to 'ceph-admin'. (default=Env: CEPHADM_SSH_USER)
* `tripleo_ceph_user_stack`: Name or ID of heat stack. Used to find the working directory.
* `tripleo_ceph_user_standalone:`: (Boolean) Use single host Ansible inventory. Used only for development or testing environments. Default: false
* `tripleo_ceph_user_timeout_arg`: (Integer) Number in minutes for the deployment to run. Default: 90
* `tripleo_ceph_user_timeout`: (Integer) Number in seconds to wait for the ansible execution of the deployment command to finish. This should be larger than the `tripleo_ceph_user_timeout_arg` value. Default: 5700
* `tripleo_ceph_user_working_dir`: (String) The working directory for the deployment where all input, output, and generated files will be stored. Defaults to "$HOME/overcloud-deploy/<stack>"


Output Variables
----------------

* `tripleo_ceph_user_output`: (String) The command standard output.
* `tripleo_ceph_user_result`: Ansible shell execution results


Dependencies
------------

None.

Example Playbooks
-----------------

Create the ceph-admin user on based on a Ceph Spec in a standalone
deployment.

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Create ceph-admin SSH user
      include_role:
        name: tripleo_ceph_user
      vars:
        tripleo_ceph_user_spec: /home/stack/ceph_spec.yaml
        standalone: true
        stack: standalone
```

On an overcloud with a running Ceph cluster with a known FSID, disable
the ceph-admin user by removing their public and private keys and
disable cephadm. The spec file is necessary to determine which nodes
to modify. WARNING: Ceph cluster administration or modification will
no longer function though Ceph can still read/write its data.

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Disable ceph-admin SSH user and disable cephadm
      include_role:
        name: tripleo_ceph_user
      vars:
        tripleo_ceph_user_enable: false
        fsid: dbd6d8c5-e8b4-4dba-b789-0945ab353c76
        tripleo_ceph_user_spec: /home/stack/ceph_spec.yaml
        stack: overcloud
```

Run cephadm commands which should re-enable cephadm for a Ceph
cluster with a known FSID.

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Re-enable ceph-admin SSH user and and cephadm
      include_role:
        name: tripleo_ceph_user
      vars:
        tripleo_ceph_user_enable: true
        fsid: dbd6d8c5-e8b4-4dba-b789-0945ab353c76
        tripleo_ceph_user_spec: /home/stack/ceph_spec.yaml
        stack: overcloud
```

License
-------

Apache-2.0
