Role Name
=========

[![Build Status](https://travis-ci.org/daixijun/ansible-role-php-mcrypt.svg?branch=master)](https://travis-ci.org/daixijun/ansible-role-php-mcrypt)

Ansible 安装php mcrypt扩展

Requirements
------------

* RHEL/Centos 7
* Ansible 2.7 +

Role Variables
--------------

```yaml
php_mcrypt_version: 1.0.3
php_mcrypt_download_url: http://pecl.php.net/get/mcrypt-{{ php_mcrypt_version }}.tgz

```

Dependencies
------------

[daixijun.php](https://galaxy.ansible.com/daixijun/php)

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: daixijun.php
    - role: daixijun.php-mcrypt
```

License
-------

BSD

Author Information
------------------

Xijun Dai <daixijun1990@gmail.com>
