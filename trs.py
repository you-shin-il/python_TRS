#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python 3.x
import urllib.parse
import urllib

# python 2.x
# import urllib2
# import urllib

# python 2.x, 3.x 공통
import hashlib
import hmac
import base64
import time
import datetime
import requests

baseurl='https://connector.gigagenie.ai/ai/v1/client/api?'
request={}

client_id = ''
client_secret = ''
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]

request['command'] = 'Translation'
request['transType'] = 'ek'
request['transMsg'] = 'How is the weather in New York?'
request['timestamp'] = timestamp
request['client_id'] = client_id

# python 2.x
# message = client_id + ':' + timestamp
# signature = hmac.new(client_secret, message, hashlib.sha256).hexdigest()
# request_str='&'.join(['='.join([k,urllib.quote_plus(request[k])]) for k in request.keys()])

# python 3.x
message = client_id + ':' + timestamp
signature = hmac.new(bytes(client_secret, 'utf8'), bytes(message, 'utf8'), hashlib.sha256).hexdigest()
request_str='&'.join(['='.join([k,urllib.parse.quote_plus(request[k])]) for k in request.keys()])

request_str = request_str.replace('+','%20')
req=baseurl+request_str+'&signature='+signature

response = requests.get(req)
print(req)
print(response.text)