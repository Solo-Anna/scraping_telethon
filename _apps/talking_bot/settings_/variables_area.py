import configparser
import os

config = configparser.ConfigParser()
config.read("./settings_/config.ini")

# database=os.getenv('database')
# user=os.getenv('user')
# host=os.getenv('host')
# password=os.getenv('password')
# port=os.getenv('port')
# token=os.getenv('token')

#---------------------------------
database=config['DB_local_clone']['database']
user=config['DB_local_clone']['user']
host=config['DB_local_clone']['host']
password=config['DB_local_clone']['password']
port=config['DB_local_clone']['port']
token=config['DB_local_clone']['token']