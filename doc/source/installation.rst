============
Installation
============

Via Package
-----------

At the command line using `yum`.

.. code-block:: console

    $ yum install tripleo-operator-ansible


At the command line using `dnf`.

.. code-block:: console

    $ dnf install tripleo-operator-ansible

From Source
-----------

At the command line install using the ansible-galaxy command.

.. code-block:: console

    $ git clone https://opendev.org/openstack/tripleo-operator-ansible
    $ cd tripleo-operator-ansible
    $ ansible-galaxy collection build --force --output-path ~/collections
    $ ansible-galaxy collection install --force ~/collections/tripleo-operator*
