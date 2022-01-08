import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import requests

from messages import *

# Send email functions
def sendmail_attach(sender, receiver, password, subject=None, bodytext=None, filelist=None):
    """
    Send email with attachment files from a file list.
    """

    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login(sender, password)

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    body = bodytext
    message.attach(MIMEText(body, 'plain'))

    if filelist != None:
        for name in filelist:
            filename = name
            attachment = open(name, 'rb')
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            message.attach(p)
    else:
        pass

    text = message.as_string()
    smtp_obj.sendmail(sender, receiver, text)
    smtp_obj.quit()
    print('Send Email done.')

# Send via TG functions
def sendtgmessage(token, chatid, bodytext=None):
    sendtext = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s\
                &parse_mode=Markdown&text=%s'%(token, chatid, bodytext)
    
    requests.get(sendtext)
    print('Send via Telegram done.')

