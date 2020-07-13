tripleo_validator_run
=====================

A role to run tripleo validations

Requirements
------------

None.

Role Variables
--------------

* `tripleo_validator_run_debug`: (Boolean) Flag to print out the delete command. Default: False
* `tripleo_validator_run_plan`: (String) Plan to run validations against
* `tripleo_validator_run_workers`: (Integer) Number of workers
* `tripleo_validator_run_extra_vars_file`: (String) Path to an ansible vars file to use when running the validations
* `tripleo_validator_run_validation`: (String) Specific validation to run
* `tripleo_validator_run_group`: (String) Group of validations to run

Output Variables
----------------

* `tripleo_validator_run_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example validator run playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Run validations
      import_role:
        name: tripleo_validator_run
      var:
        tripleo_validator_run_debug: true
        tripleo_validator_run_name: overcloud
```

License
-------

Apache-2.0
