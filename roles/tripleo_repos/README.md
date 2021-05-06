tripleo_repos
=============

Role to install tripleo_repos and use it to manage tripleo yum repos.

Requirements
------------

None

Role Variables
--------------

* `tripleo_repos_branch`: (String) Repo branch to configure (master|train|stein|etc)
* `tripleo_repos_repo_branch`: (String) Repo branch to install tripleo-repos tool (master|train|stein|etc)
* `tripleo_repos_debug`: (Boolean) Flag to print out the tripleo-repos command being executed
* `tripleo_repos_extra_args`: (List) List of extra arguments to pass to tripleo_repos
* `tripleo_repos_repo_base`: (String) Url base to RDO (default: <https://trunk.rdoproject.org>)
* `tripleo_repos_repos`: (List) List of repos to install
* `tripleo_repos_mirror`: (String) Base OS mirror to use
* `tripleo_repos_no_stream`: (Boolean) Flag for tripleo-repos to disable stream if CentOS8 Stream is not being used. Default: false
* `tripleo_repos_rdo_mirror`: (String) RDO mirror to use
* `tripleo_repos_output_path`: (String) Directory to save the repos in
* `tripleo_repos_stream`: (Boolean) Flag for tripleo-repos if CentOS8 Stream is used. Default: false

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
        tripleo_repos_repos:
          - current
          - ceph
        tripleo_repos_branch: train
```

License
-------

Apache-2.0
