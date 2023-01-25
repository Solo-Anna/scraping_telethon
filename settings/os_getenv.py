import configparser
import os

# api_id = os.getenv('api_id')
# api_hash = os.getenv('api_hash')
# username = os.getenv('username')
# token = os.getenv('token')
#
config_keys = configparser.ConfigParser()
config_keys.read("./settings/config_keys.ini")
api_id = config_keys['Telegram']['api_id']
api_hash = config_keys['Telegram']['api_hash']
username = config_keys['Telegram']['username']
token_main = config_keys['Token']['token_main']
token = config_keys['Token']['token']
talking_token = config_keys['Token_talking_bot']['token']
token_red = config_keys['Token']['token_red']
