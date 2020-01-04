import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_redis_extension(host):
    output = host.check_output("/usr/local/php/bin/php -m | grep mcrypt")

    assert output == "mcrypt"


def test_mcrypt_so(host):
    extension_dir = host.check_output("/usr/local/php/bin/php-config --extension-dir")

    so = host.file(os.path.join(extension_dir.strip(), "mcrypt.so"))

    assert so.exists


def test_mcrypt_config_file(host):
    cf = host.file("/usr/local/php/etc/php.d/mcrypt.ini")

    assert cf.exists
