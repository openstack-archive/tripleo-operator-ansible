==============
Best Practices
==============


The roles provided in this collection wrap the tripleoclient actions that are
used to deploy and manage an undercloud and overcloud. The point of these
roles is to establish a common interface for Ansible based automation.


Ansible Collection Namespace
----------------------------

tripleo-operator-ansible is an Ansible collection. In order to consume the
roles and plugins within this repository, it needs to be installed as a
collection.  This repository provides the `tripleo.operator` namespace.
When writing playbooks, the usage of the `collections:` keyword
is required in order for them to be executed. See the `Ansible Collection Documentation`_
for additional details.

.. _Ansible Collection Documentation: https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#using-collections-in-a-playbook


Role Naming Convention
----------------------

To general naming scheme for the roles provide is to take the openstackclient
command and replace `openstack` with `tripleo` and use underscores instead
of spaces. For example, `openstack overcloud deploy` becomes
`tripleo_overcloud_deploy`. The exception to this rule is when the command
itself start with `openstack tripleo`. Rather than double the `tripleo` in the
role name, we only specify it once. For example `openstack tripleo container image prepare`
is simply `tripleo_container_image_prepare`.


Variable Naming Convention
--------------------------

The variables used by each role are prefixed with the role name. For example
all roles contain a debug variable that can be used to print out the data used
when executing the specific commands. For example, `tripleo_overcloud_deploy_debug`
can be used to print out the cli command and the environment data used when
the command is executed.
