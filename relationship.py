#!/usr/bin/env python
#coding:utf-8

from rediscluster import StrictRedisCluster
import sys
import MySQLdb

def redis_cluster(str1):
    redis_nodes =  [{'host':'10.53.8.10','port':6812},
                    {'host':'10.53.8.11','port':6812},
                    {'host':'10.53.8.12','port':6812}
                   ]
    try:
        redisconn = StrictRedisCluster(startup_nodes=redis_nodes)
    except Exception,e:
        print "Connect Error!"
        sys.exit(1)

    fans = redisconn.hget('r:fanscount',str1)
    return fans

def redis_hset(str2,str3):
    redis_nodes =  [{'host':'10.53.8.10','port':6812},
                    {'host':'10.53.8.11','port':6812},
                    {'host':'10.53.8.12','port':6812}
                   ]
    try:
        redisconn = StrictRedisCluster(startup_nodes=redis_nodes)
    except Exception,e:
        print "Connect Error!"
        sys.exit(1)

    fans = redisconn.hset('r:fanscount',str2,str3)
    return fans

db = MySQLdb.connect("192.168.9.226","lz_read","909e8d463991b442e2b3816e712ad8e5","PLURelationship") 


file_object = open('/app/tmp/uid.txt')
for line in file_object:
     line = line.strip('\r\n')
     fans = redis_cluster(line)
     #print "uid:" + line
     if fans is None:
         continue
     else:
         sql1 = "SELECT COUNT(1) FROM relationship WHERE ToUserID=" + line + " AND IsFollow='1';"
         cursor = db.cursor()
         cursor.execute(sql1)
         data = cursor.fetchone()
         #print "fans:" + str(fans)
         if int(data[0]) > int(fans):             
              print "uid:" + line
              print "mysql:" + str(data[0])
              print "redis:" + str(fans)
              redis_hset(int(line),int(data[0]))
db.close()