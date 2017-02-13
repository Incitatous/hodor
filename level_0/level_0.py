#!/usr/bin/python3
import pycurl
import socket
from urllib.parse import urlencode

target = 'http://54.221.6.249/level0.php'
name = 73


def connect():
    c = pycurl.Curl()
    c.setopt(pycurl.URL, target)

    post_data = {'id': name, 'holdthedoor': ''}
    postfields = urlencode(post_data)

    c.setopt(c.POST, 1)
    c.setopt(c.POSTFIELDS, postfields)

    c.setopt(c.CONNECTTIMEOUT, 10000)
    c.setopt(c.TIMEOUT, 10000)

    c.setopt(pycurl.REFERER, target)
    c.setopt(pycurl.WRITEFUNCTION, lambda x: None)

    try:
        c.perform()

    except pycurl.error:
        print('failed')


for i in range(1024):
    connect()
