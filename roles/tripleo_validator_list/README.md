tripleo_validator_list
=====================

A role to list tripleo validations

Requirements
------------

None.

Role Variables
--------------

* `tripleo_validator_list_debug`: (Boolean) Flag to print out the delete command. Default: False

Output Variables
----------------

* `tripleo_validator_list_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example validator list playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: List validations
      import_role:
        name: tripleo_validator_list
```

License
-------

Apache-2.0
