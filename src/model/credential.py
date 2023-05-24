from configparser import ConfigParser

config = ConfigParser()

configfile = r'src/model/config.ini'
config.read(configfile)

class credentials:
    def __init__(self):
        self.user = config["sqlacess"]["user"]
        self.password = config["sqlacess"]["password"]
        self.host = config["sqlacess"]["host"]
        self.database = config["sqlacess"]["database"]
        
    def dbChange(self, db, default=False):
        config["sqlacess"]["database"] = db
        self.database = config["sqlacess"]["database"]
        
        if default == True:
            config.set("sqlacess", "database", db)
            with open(configfile, "w") as current_content:
                config.write(current_content)
            
            print(f"Config.ini rewrited. Now is {db}!")

if __name__ == "__main__":
    creds = credentials()
    creds.dbChange("NewDatabase")
    