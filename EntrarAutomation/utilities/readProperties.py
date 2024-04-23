from configparser import ConfigParser

config = ConfigParser()
config.read(r"Configurations\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        print(config.get('basic info', 'url'))

        url = config.get('basic info', 'url')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common', 'username')
        #print(config.get('common data', 'username'))
        return username

    @staticmethod
    def getPassword():
        password = config.get('common', 'password')
        return password
