import sys
sys.path.append('..')

from configparser import ConfigParser
config = ConfigParser()
config.read('setting_messages.ini')

# Telegram
configtg = config['telegram']
token = configtg.get('token')
chatid = configtg.get('chatid')

# Email
configemail = config['email']
sender = configemail.get('sender')
password = configemail.get('password')
recceiver = configemail.get('receiver')