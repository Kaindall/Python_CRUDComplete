from configparser import ConfigParser

config = ConfigParser()

try:
    configfile = r'src/controller/config.ini'
    config.read(configfile)
    print (config.sections())

except:
    print("Arquivo config.ini não encontrado!")