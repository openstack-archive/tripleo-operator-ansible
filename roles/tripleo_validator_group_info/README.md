tripleo_validator_group_info
================================

A role to get info of a tripleo validations group

Requirements
------------

None.

Role Variables
--------------

* `tripleo_validator_group_info_debug`: (Boolean) Flag to print out the debug command. Default: False
* `tripleo_validator_group_info`: (String) Group to gather from

Output Variables
----------------

* `tripleo_validator_group_info_result`: Ansible shell execution results

Dependencies
------------

None.

Example Playbook
----------------

Example validator group info playbook

```yaml
- hosts: undercloud
  gather_facts: true
  tasks:
    - name: Gather validation group info
      import_role:
        name: tripleo_validator_group_info
```

License
-------

Apache-2.0
