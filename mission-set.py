#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis

file_object = open('/app/tmp/0605.txt')
r = redis.Redis(host='10.53.8.12', port=6925,db=0)
for line in file_object:
     line = line.strip('\r\n')
     data = "mission:context:63683:23:" + str(line)
     ##print data
     ##type(data)
     ss = r.smembers(str(data))
     result = '2' in ss
          #r.sadd(str(data),1)
     a = '1' in ss
     b = '2' in ss
     if a and b:
	print "----1-2:" + str(ss) + "----uid:" + str(line)
     elif a:
        print "^^^^1:" + str(ss) + "^^^^uid:" + str(line)
     else:
        print "===other" + str(ss) + "=====uid:" + str(line)
     ##print ss
     ##print type(ss)
     ##print (r.smembers(data))
     ##print line