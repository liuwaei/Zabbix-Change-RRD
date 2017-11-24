#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib2
from urllib2 import URLError
from login import zabbix_login

t = zabbix_login()


def item_get(hostid):
    data = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "item.get",
            "params": {
                "output": ["itemids", "key_"],
                "hostids": hostid,
            },
            "auth": t.user_login(),
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
        itemid = []
        for item in response['result']:
            itemid.append(item['itemid'])
            # print item 
        return itemid


if __name__ == "__main__":
    a = item_get(10121)
    i = 0
    n = len(a)
    for i in range(n):
        print a[i]
        i = i + 1
