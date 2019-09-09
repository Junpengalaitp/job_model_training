from configparser import ConfigParser


def get_config(section, key):
    config = ConfigParser()
    config.read('config/dev_config.ini')
    return config.get(section, key)
