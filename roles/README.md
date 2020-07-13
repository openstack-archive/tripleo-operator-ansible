tripleo-operator-ansible roles
==============================

These roles wrap tripleo cli functions for use in automation.

Requirements
------------

None.

Global Variables
----------------

Accross the roles, there are a few variables that can be defined and would be
consumed by default.

* `tripleo_os_cloud`: (String) OS_CLOUD name to use when a command requires authentication. By default this will be used to populate any role specific os_cloud variable that may be defined. If this is defined, it will take precedence over `tripleo_rc_file`.
* `tripleo_rc_file`: (String) File path on the remote system that contains the authentication environment variables that will be used to perform actions that require authentication.

Dependencies
------------

None.

Example Playbooks
-----------------

Example undercloud installation

```yaml
---
- hosts: undercloud
  gather_facts: true
  collections:
    - tripleo.operator
  tasks:
    - name: Create dummy interface
      command: ip link add prov type dummy
      become: true
      when: not 'prov' in ansible_facts.interfaces

    - name: Set hostname
      hostname:
        name: 'undercloud.localdomain'
      become: true

    - name: Configure tripleo repositories
      import_role:
        name: tripleo_repos

    - name: Install python2 tripleoclient
      package:
        name: python2-tripleoclient
        state: present
      become: true
      when: ansible_distribution_major_version|int <= 7

    - name: Install python3 tripleoclient
      package:
        name: python3-tripleoclient
        state: present
      become: true
      when: ansible_distribution_major_version|int >= 8

    # This uses https://opendev.org/openstack/ansible-config_template
    - name: Generate undercloud.conf
      become: True
      config_template:
        src: /usr/share/python-tripleoclient/undercloud.conf.sample
        dest: "{{ ansible_env.HOME }}/undercloud.conf"
        remote_src: true
        render_template: false
        config_overrides:
          'DEFAULT':
              undercloud_debug: true
              enable_telemetry: false
              local_mtu: 1400
              local_interface: prov
              undercloud_enable_selinux: false
          'ctlplane-subnet':
              masquerade: true
        config_type: ini

    - name: Install undercloud
      import_role:
        name: tripleo_undercloud_install
      vars:
        tripleo_undercloud_install_debug: true
```

License
-------

Apache-2.0
