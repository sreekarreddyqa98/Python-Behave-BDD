from configparser import ConfigParser

def read_configuarion(category, key):
    config = ConfigParser()
    config.read("Configurations/config.ini")
    return config.get(category,key)