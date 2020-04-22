# daixijun.php-mcrypt

[![Build Status](https://github.com/daixijun/ansible-role-php-mcrypt/workflows/build/badge.svg)](https://github.com/daixijun/ansible-role-php-mcrypt/actions)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-daixijun.php-mcrypt-660198.svg?style=flat)](https://galaxy.ansible.com/daixijun/php-mcrypt/)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/daixijun/ansible-role-php-mcrypt?sort=semver)](https://github.com/daixijun/ansible-role-php-mcrypt/tags)

Ansible 安装php mcrypt扩展

## 环境要求

* RHEL/Centos 7
* Ansible 2.7 +

## 变量

```yaml
php_mcrypt_version: 1.0.3
php_mcrypt_download_url: http://pecl.php.net/get/mcrypt-{{ php_mcrypt_version }}.tgz

```

## 依赖

[daixijun.php](https://github.com/daixijun/ansible-role-php)

## 示例

```yaml
- hosts: servers
  roles:
    - role: daixijun.php
    - role: daixijun.php-mcrypt
```

## License

BSD

## 维护者

* Xijun Dai <daixijun1990@gmail.com>
