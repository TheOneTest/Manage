import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
upPath = os.path.abspath(os.path.join(proDir,os.path.pardir))
configPath = os.path.join(upPath, "config\config.ini")
# configPath = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'

class ReadConfig:
    def __init__(self):
        # fd = open(configPath)
        # data = fd.read()
        #
        # #  remove BOM
        # if data[:3] == codecs.BOM_UTF8:
        #     data = data[3:]
        #     file = codecs.open(configPath, "w")
        #     file.write(data)
        #     file.close()
        # fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_redis(self, name):
        value = self.cf.get("REDIS", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

    def get_file(self,name):
        value = self.cf.get("FILE",name)
        return value


if __name__ == "__main__":
    print ReadConfig.get_http("baseurl")