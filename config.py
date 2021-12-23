import csv
import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders




#Path to setting_key.json
key = 'path-to-secret-file'


#Email Settings
LOGIN = 'EmailLogin@gmail.com'
PASSWORD = 'EmailPassword'

MAIL_TO = 'Reviever@gmail.com'


#Connection to FireBase
cred = credentials.Certificate(key)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'link-to-firebase'
})