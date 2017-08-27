'''
Created on 26-Aug-2017

@author: haxo
'''
import requests
from pyquery import PyQuery

link = "https://www.udemy.com/join/login-popup/"

client = requests.Session()

client.get(link) #Set cookie

token = client.cookies['csrftoken']

params = {'email' : 'myemail@gmail.com', 'password' : 1234567899, 'csrfmiddlewaretoken': token}

headers = {'Referer': 'https://www.udemy.com/'} #'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'}

r = client.post(link, headers=headers, data=params)

pq = PyQuery(r.text)

tag = pq('div.form-errors')

if tag.text() == 'Please check your email and password.':
    print 'Email pass is wrong buddy!'
