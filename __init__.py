import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.append('..')

from configparser import ConfigParser
config = ConfigParser()
config.read('setting_messages.ini')

# Telegram
configtg = config['telgram']
token = configtg.get('token')
id = configtg.get('chatif')

# Email
configemail = config['email']
sender = configemail.get('sender')
password = configemail.get('password')
recceiver = configemail.get('receiver')