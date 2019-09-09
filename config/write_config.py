from configparser import ConfigParser

config = ConfigParser()

config['mongodb'] = {
    'ip': '192.168.1.39',
    'port': '27018',
    'username': 'root',
    'password': 'root',
    'db': 'githubJobs',
    'authSource': 'admin'
}

config['mysql'] = {
    'ip': '192.168.1.39',
    'dbname': 'alaitp',
    'port': '3307',
    'user': 'root',
    'password': 'root'
}


def write_config():
    with open('./dev_config.ini', 'w') as f:
        config.write(f)


if __name__ == '__main__':
    write_config()
