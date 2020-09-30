tripleo_validator_show
=====================

A role to show tripleo validations

Requirements
------------

None.

Role Variables
--------------

* `tripleo_validator_show_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_validator_show_validation`: (String) Group of validations to inspect

Output Variables
----------------

* `tripleo_validator_show_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example validator show playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Show validation
      import_role:
        name: tripleo_validator_show
```

License
-------

Apache-2.0
