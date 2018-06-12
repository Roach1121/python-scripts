#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
from influxdb import InfluxDBClient
import json

db = MySQLdb.connect(host="10.53.3.24",user="xxxx",passwd="xxxx",db="xxxx",port=3306,charset="utf8")
cursor = db.cursor()
data = cursor.execute("SELECT IP,Port,userid,Passwd FROM all_config;")
info = cursor.fetchmany(data)
print "info",type(info)
for host1,port1,uid1,passwd1 in info:
    print host1
    db = MySQLdb.connect(host=str(host1),user=str(uid1),passwd=str(passwd1),db="information_schema",port=int(port1),charset="utf8",connect_timeout=3)
    cursor = db.cursor()
    data = cursor.execute("select SUBSTRING_INDEX(host,':',1) as ip , count(*) as cishu from information_schema.processlist group by ip order by cishu desc;")
    client = InfluxDBClient('10.53.6.15', 8086, '', '', 'mysql_clientlist')

    info = cursor.fetchmany(data)
    for ii,dd in info:
        print ii,dd
        json_body = [{"measurement": "mysql_clientlist","tags": {"server": str(host1), "host": str(ii), "port": str(port1)}, "fields": {"server": str(host1), "host": str(ii), "port": str(port1), "count": int(dd)}}]
        #print(json_body)
        client.write_points(json_body,retention_policy="autogen")
    cursor.close()
    #db.commit()
    #db.close()
cursor.close()
db.commit()
db.close()