import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.append('..')

import pandas as pd

# Load setting.csv (with all input adjustment done over setting_oi.csv)
df_setting = pd.read_csv('setting_messages.csv', header=0, index_col='field')
# Sender Telegram Bot
token = df_setting.loc['token']['value']
# Receiver Telegram ID
chatid = df_setting.loc['chatid']['value']
# Email address to send alert email
sender = df_setting.loc['sender']['value']
# Sender email account password
password = df_setting.loc['password']['value']
# Email address to receive alert email (could be same as above)
receiver = df_setting.loc['receiver']['value']