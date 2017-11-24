#!/usr/bin/env python
#-*- coding: utf-8 -*-


import json
import sys
import urllib2
from urllib2 import URLError
reload(sys)
sys.setdefaultencoding('utf-8')
#login
class zabbix_login:
    def __init__(self):
        self.url = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
        self.header = {"Content-Type":"application/json"}
        self.hostid = []
        self.hostname = []
    def user_login(self):
        data = json.dumps({
                           "jsonrpc": "2.0",
                           "method": "user.login",
                           "params": {
                                      "user": "Admin",
                                      "password": "zabbix"
                                      },
                           "id": 0
                           })
        request = urllib2.Request(self.url, data)
        for key in self.header:
            request.add_header(key, self.header[key])
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            print "\033[041m please check url !\033[0m",e.code
        except KeyError as e:
            print "\033[041m please check password !\033[0m",e
        else:
            response = json.loads(result.read())
            result.close()
            self.authID = response['result']
            return self.authID