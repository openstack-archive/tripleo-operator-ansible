tripleo_ceph_deploy
=====================

A role to deploy Ceph on overcloud nodes before deploying the overcloud.

Requirements
------------

None.

Role Variables
--------------

* `tripleo_ceph_deploy_become`: (Boolean) Execute command with escalated privileges. Default: false
* `tripleo_ceph_deploy_crush_hierarchy`: (String) Path to an existing crush hierarchy spec file.
* `tripleo_ceph_deploy_debug`: (Boolean) Flag to print out the command that is run. Default: false
* `tripleo_ceph_deploy_deployed_baremetal`: (String) Path to the environment file output from "openstack overcloud node provision". This argument may be excluded only if tripleo_ceph_deploy_standalone is True.
* `tripleo_ceph_deploy_spec`: (String) Path to an existing Ceph spec file. If not provided a spec will be generated automatically based on `tripleo_ceph_deploy_roles_file` and `tripleo_ceph_deploy_deployed_baremetal`. The `tripleo_ceph_deploy_deployed_baremetal` parameter is optional only if `tripleo_ceph_deploy_spec` is used.
* `tripleo_ceph_user_ssh_user`: (String) Name of the SSH user used by cephadm. Warning: if this option is used, it must be used consistently for every 'openstack overcloud ceph' call. Defaults to 'ceph-admin'. (default=Env: CEPHADM_SSH_USER)
* `tripleo_ceph_deploy_generate_scripts_only`: (Boolean) Do not run the actual command - to be used in conjunction with `tripleo_ceph_deploy_generate_scripts`. By default uses the value of `tripleo_generate_scripts_only` or False if `tripleo_generate_scripts_only` is not defined.
* `tripleo_ceph_deploy_generate_scripts`: (Boolean) Write out a shell script that can be used to reproduce the command being executed. By default uses the value of `tripleo_generate_scripts` or False if `tripleo_generate_scripts` is not defined.
* `tripleo_ceph_deploy_mon_ip`: (String) IP address of the first Ceph monitor. If not set, an IP from the Ceph public_network of a server with the mon label from the Ceph spec is used. IP must already be active on server. Only supported if tripleo_ceph_deploy_standalone is True.
* `tripleo_ceph_deploy_osd_spec`: (String) Path to an existing OSD spec file. When the Ceph spec file is generated its OSD spec defaults to {data_devices: {all: true}} for all service_type osd. Use this parameter to override the data_devices value inside the Ceph spec file.
* `tripleo_ceph_deploy_overwrite`: (Boolean) Flag to skip yes/no prompts about overwriting the deployed_ceph.yaml from a previous run. Default: false
* `tripleo_ceph_deploy_poll`: (Integer) Number of seconds to wait between each checks to see if the deployment command has completed. Default: 10
* `tripleo_ceph_deploy_roles_file`: (String) Path to an alternative roles_data.yaml. Used to decide which node gets which Ceph mon, mgr, or osd service based on the node's role and `tripleo_ceph_deploy_deployed_baremetal`.
* `tripleo_ceph_deploy_stack`: Name or ID of heat stack. Used to find the working directory. If unset `openenstack overcloud ceph deploy` will default this value to 'overcloud'.
* `tripleo_ceph_deploy_standalone`: (Boolean) Use single host Ansible inventory. Used only for development or testing environments. Used for single server development or testing environments. Default: false
* `tripleo_ceph_deploy_timeout_arg`: (Integer) Number in minutes for the deployment to run. Default: 90
* `tripleo_ceph_deploy_timeout`: (Integer) Number in seconds to wait for the ansible execution of the deployment command to finish. This should be larger than the `tripleo_ceph_deploy_timeout_arg` value. Default: 5700
* `tripleo_ceph_deploy_working_dir`: (String) The working directory for the deployment where all input, output, and generated files will be stored. Defaults to "$HOME/overcloud-deploy/<stack>"
* `tripleo_ceph_deploy_output:`: (String) The path to the output environment file describing the Ceph deployment to pass to the overcloud deployment.
* `tripleo_ceph_deploy_skip_user_create`: (Boolean) Do not create the cephadm SSH user. This user is necessary to deploy but may be created in a separate step via 'openstack overcloud ceph user enable'. Default: false
* `tripleo_ceph_deploy_skip_hosts_config`: (Boolean) Do not update /etc/hosts on deployed servers. By default this is configured so overcloud nodes can reach each other and the undercloud by name. Default: false
* `tripleo_ceph_deploy_skip_container_registry_config`: (Boolean) Do not update /etc/containers/registries.conf on deployed servers. By default this is configured so overcloud nodes can pull containers from the undercloud registry. Default: false
* `tripleo_ceph_deploy_network_data`: (String) Path to an alternative network_data.yaml. Used to define Ceph public_network and cluster_network. This file is searched for networks with name_lower values of storage and storage_mgmt. If none found, then search repeats but with service_net_map_replace in place of name_lower. Use `tripleo_ceph_deploy_public_network_name` or `tripleo_ceph_deploy_cluster_network_name` options to override name of the searched for network from storage or storage_mgmt to a customized name. If network_data has no storage networks, both default to ctlplane. If found network has >1 subnet, they are all combined (for routed traffic). If a network has ipv6 true, then the ipv6_subnet is retrieved instead of the ip_subnet, and the Ceph global ms_bind_ipv4 is set false and the ms_bind_ipv6 is set true. Use `tripleo_ceph_deploy_config` to override these defaults if desired.
* `tripleo_ceph_deploy_public_network_name`: (String) Name of the network defined in `tripleo_ceph_deploy_network_data` which should be used for the Ceph public_network. If undefined the client defaults this value to 'storage'.
* `tripleo_ceph_deploy_cluster_network_name`: (String) Name of the network defined in `tripleo_ceph_deploy_network_data` which should be used for the Ceph cluster_network. If undefined the client defaults this value to 'storage_mgmt'.
* `tripleo_ceph_deploy_config`:  (String) Path to an existing ceph.conf with settings to be assimilated by the new cluster via 'cephadm bootstrap --config'
* `tripleo_ceph_deploy_cephadm_extra_args`: (String) String of extra parameters to pass cephadm. E.g. if this parameter is set to '--log-to-file --skip-prepare-host', then cephadm boostrap will use those options. Warning: requires `tripleo_ceph_deploy_force` to be true as not all possible options ensure a functional deployment.
* `tripleo_ceph_deploy_force`: (Boolean) Run command regardless of consequences. Default: false
* `tripleo_ceph_deploy_ceph_vip`: (String) Path to an existing Ceph services/network mapping file.
* `tripleo_ceph_deploy_daemons`: (String) Path to an existing Ceph daemon options definition.
* `tripleo_ceph_deploy_single_host_defaults`: (Boolean) Adjust configuration defaults to suit a single-host Ceph cluster. Default: false
* `tripleo_ceph_deploy_container_image_prepare`: (String) Path to an alternative container_image_prepare_defaults.yaml. Used to control which Ceph container is pulled by cephadm via the ceph_namespace, ceph_image, and ceph_tag variables in addition to registry authentication via ContainerImageRegistryCredentials.
* `tripleo_ceph_deploy_container_cephadm_default`: (Boolean) Use the default continer defined in cephadm instead of container_image_prepare_defaults.yaml. If this is used, 'cephadm bootstrap' is not passed the --image parameter. Default: false
* `tripleo_ceph_deploy_container_namespace`: (String) Override the namespace value set via `tripleo_ceph_deploy_continer_image_prepare`. E.g. quay.io/ceph.
* `tripleo_ceph_deploy_container_image`: (String) Override the image value set via `tripleo_ceph_deploy_continer_image_prepare`. E.g. ceph.
* `tripleo_ceph_deploy_container_tag`: (String) Override the tag value set via `tripleo_ceph_deploy_continer_image_prepare`. E.g. latest.
* `tripleo_ceph_deploy_container_registry_url`: (String) Override the registry URL value set via `tripleo_ceph_deploy_continer_image_prepare`.
* `tripleo_ceph_deploy_container_registry_username`: (String) Override the registry username value set via `tripleo_ceph_deploy_continer_image_prepare`.
* `tripleo_ceph_deploy_container_registry_password`: (String) Override the registry password value set via `tripleo_ceph_deploy_continer_image_prepare`.


Output Variables
----------------

* `tripleo_ceph_deploy_output`: (String) The command standard output.
* `tripleo_ceph_deploy_result`: (String) Ansible shell execution results


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
    - name: Deploy Ceph using 'openstack overcloud node provision' output
      include_role:
        name: tripleo_ceph_deploy
      vars:
        tripleo_ceph_deploy_debug: True
        tripleo_ceph_deploy_generate_scripts: True
        tripleo_ceph_deploy_overwrite: True
        tripleo_ceph_deploy_stack: overcloud
        tripleo_ceph_deploy_roles_file: /home/stack/custom_roles.yaml
        tripleo_ceph_deploy_deployed_baremetal: /home/stack/overcloud-baremetal-deployed.yaml
```

License
-------

Apache-2.0
