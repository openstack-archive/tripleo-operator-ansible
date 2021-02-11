tripleo_validator_show_parameter
================================

A role to show tripleo validations parameters

Requirements
------------

None.

Role Variables
--------------

* `tripleo_validator_show_parameter_debug`: (Boolean) Flag to print out the debug command. Default: False
* `tripleo_validator_show_parameter`: (String) Parameter to inspect

Output Variables
----------------

* `tripleo_validator_show_parameter_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example validator show parameter playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Show validation parameter
      import_role:
        name: tripleo_validator_show_parameter
      var:
        tripleo_validator_show_parameter: foo
```

License
-------

Apache-2.0
