#!/usr/bin/env python
#-*- coding: utf-8 -*-
import json
import urllib2
from urllib2 import URLError
from login import zabbix_login
t=zabbix_login()
def hostid_get():
    data = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                        "output": ["hostid","name"],
                        "groupids":6,
                        "filter":{"flags": "4" },
                        },
            "auth":t.user_login(),
            "id": 1,
        })
    request = urllib2.Request(t.url, data)
    for key in t.header:
        request.add_header(key, t.header[key])
    try:
        result = urllib2.urlopen(request)
    except URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print 'The server could not fulfill the request.'
            print 'Error code: ', e.code
    else:
        response = json.loads(result.read())
        result.close()
        hostid=[]
        hostname=[]
        for host in response['result']:
            hostid.append(host['hostid'])
            hostname.append(host['name'])
        return hostid,hostname

if __name__ == "__main__":
    a,b=hostid_get()
    i=0
    n=len(b)
    for i in range(n):
        print a[i],b[i]
        i=i+1



