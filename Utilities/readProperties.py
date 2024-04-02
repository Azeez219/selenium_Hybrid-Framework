# This File is for reuseable data.
# We have to write the Reuseable data here and get it in anywhere in the projects.


import configparser
config = configparser.RawConfigParser()
config.read(".//Configurations//config.ini")

class readConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('Common Info', 'baseUrl')
        return url
    @staticmethod
    def getUserEmail():
        useremail = config.get('Common Info', 'useremail')
        return useremail

    @staticmethod
    def getUserPassword():
        password = config.get('Common Info', 'password')
        return password

