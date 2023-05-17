from configparser import ConfigParser

config = ConfigParser()

configfile = r'src/controller/config.ini'
config.read(configfile)

class credentials ():
    def __init__(self):
        self.user = config["sqlacess"]["user"]
        self.password = config["sqlacess"]["password"]
        self.host = config["sqlacess"]["host"]
        self.database = config["sqlacess"]["database"]
        
    def dbChange(self, db):
        config["sqlacess"]["database"] = db
        self.database = config["sqlacess"]["database"]

if __name__ == "__main__":
    crd = credentials()
    crd.dbChange("NewDatabase")