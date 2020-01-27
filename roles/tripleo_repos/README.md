tripleo_repos
=============

Role to install tripleo_repos and use it to manage tripleo yum repos.

Requirements
------------

None

Role Variables
--------------

* `tripleo_repos_branch`: (String) Repo branch to configure (master|train|stein|etc)
* `tripleo_repos_extra_args`: (List) List of extra arguments to pass to tripleo_repos
* `tripleo_repos_extra_repos`: (List) List of extra repos to configure (e.g. ceph)
* `tripleo_repos_repo_base`: (String) Url base to RDO (default: <https://trunk.rdoproject.org>)
* `tripleo_repos_version`: (String) Version to configure (current-tripleo-dev|current-tripleo|current)

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  roles:
    - name: Setup tripleo_repos
      include_role:
        name: tripleo_repos
      vars:
        tripleo_repos_extra_repos:
          - ceph
        tripleo_repos_extra_args:
          - "--rdo-mirror https://my.awesome.mirror/"
```

License
-------

Apache-2.0
