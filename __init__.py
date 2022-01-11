import os
import sys
sys.path.append('..')

from configparser import ConfigParser
config = ConfigParser()
codepath = os.path.dirname(os.path.abspath(__file__))
config.read(os.path.join(codepath, 'setting_messages.ini'))

# Telegram
configtg = config['telegram']
token = configtg.get('token')
chatid = configtg.get('chatid')

# Email
configemail = config['email']
sender = configemail.get('sender')
password = configemail.get('password')
recceiver = configemail.get('receiver')