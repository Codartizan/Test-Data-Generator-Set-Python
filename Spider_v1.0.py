import requests
import re
from bs4 import BeautifulSoup

def login():
    url = 'http://172.16.1.186:8080/CADENCIE/servlet/app'
    login_url = 'http://172.16.1.186:8080/CADENCIE/servlet/LOGON'
    login_data = {
        'Bank' : 01,
        'Employee Number' : 200010,
        'Password' : 'Cadencie1',
    }