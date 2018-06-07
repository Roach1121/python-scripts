#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
import json
import urllib
import urllib2

file_object = open('/app/tmp/test.txt')
r = redis.Redis(host='10.53.8.13', port=6398,db=0)
for line in file_object:
     line = line.strip('\r\n')
     print line
     for ii in range(1,12):
          data = "u:logined:client:" + str(ii)
          ss = r.hget(str(data),line)
          if ss is None:
               break
          else:
               print data
               j1 = json.loads(ss)
               cookie1 = "cookies=" + j1['cookie']
               cookie1 = urllib.urlencode(cookie1)
               req = "http://login.longzhu.com/internal/kickUserLoginByCookie"
               request = urllib2.Request(req, data=cookie1)
               response = urllib2.urlopen(request)
               print response.read()
     ##print ss
     ##print type(ss)
     ##print (r.smembers(data))
     ##print line