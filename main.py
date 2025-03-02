import configparser

class VK:
    pass

class YD:
    pass

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('settings.ini')
    yandex_token = config['Tokens']['yd_token']
    vk_token = config['Tokens']['vk_token']