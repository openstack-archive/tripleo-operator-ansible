test_molecule_prep
==================

A role to do collection install for molecule testing. The role assumes it's being
run from a molecule path.

Requirements
------------

None.

Role Variables
--------------

* `test_module_prep_collections_build_root`: (String) Path a directory to output the collection build to. Default: "{{ ansible_env.HOME }}/collection-buildroot"
* `test_module_prep_execution_root`: (String) Path to the directory where the build action should run in. Default: '../../../..'

Output Variables
----------------

None.

Dependencies
------------

None.

Example Playbook
----------------

Example install execution playbook

```yaml
- hosts: localhost
  tasks:
    - name: Do molecule prep actions
      import_role:
        name: test_molecule_prep
```

License
-------

Apache-2.0
