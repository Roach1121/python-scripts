#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
import json
import requests

file_object = open('/app/tmp/test.txt')
redis1 = redis.Redis(host='10.53.8.13', port=6398,db=0)
for line in file_object:
     line = line.strip('\r\n')
     print line
     for ii in range(1,12):
          data = "u:logined:client:" + str(ii)
          ss = redis1.hget(str(data),line)
          if ss is None:
               break
          else:
               print data
               j1 = json.loads(ss)
               cookie1 =  '{"cookies":"%s"}'%(str(j1['cookie']))
               r = requests.post('http://login.xxxxx.xxx/internal/kickUserLoginByCookie', data=eval(cookie1))
               print(r.url)
               print(r.text)