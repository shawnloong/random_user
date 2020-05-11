#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：untitled1 -> 11
@IDE    ：PyCharm
@Author ：Netdataquit
@Date   ：2020/1/11 20:29
@Desc   ：
=================================================='''

from faker import Factory
import pymysql
import sys
import datetime

if len(sys.argv) >= 2:
    v_count = sys.argv[1]
else:
    v_count = 1000
    print("please usage %s string "%(sys.argv[0]))

v_counts = v_count * 100
print(v_counts)
print("开始生成：",str(v_counts),"条数据，请等待")

v_count = int(v_count)
#pymysql.connections.DEBUG = True
db = pymysql.connect(""
                     "192.168.137.3",
                     "system",
                     "hxl168168",
                     "netdata")

cursor = db.cursor()
starttime= datetime.datetime.now()


def f_gen_user():
    fake = Factory().create('zh_CN')
    #starttime= datetime.datetime.now()
    li = []
    tp = ()
    num = 0
    v_batch = 100
    while num < v_batch:
        num += 1
        user_info = (fake.profile(fields=None, sex=None))
        v_user = user_info['username']
        v_pass = fake.md5(raw_output=False)
        v_name = user_info['name']
        v_sex = user_info['sex']
        v_mobile = fake.phone_number()
        v_address = user_info['address']
        v_mail = user_info['mail']
        v_ssn = user_info['ssn']
        v_birthdate = user_info['birthdate']
        tp = (v_user,v_pass,v_name,v_sex,v_mobile,v_address,v_birthdate,v_mail,v_ssn)
        li.append(tp)
        #rint(count)
    return li


count = 0
while count < v_count:
    userinfo = f_gen_user()
    # print(userinfo)
    sql = 'insert into user_info(login_name,login_pass,real_name,sex,link_mobile,address,birthdate,email,id_card,create_time,modify_time) ' \
              'values (%s,%s,%s,%s,%s,%s,%s,%s,%s,now(),now())'
    try:
        with db.cursor() as cursor:
            cursor.executemany(sql, userinfo)
            db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    count += 1
endtime= datetime.datetime.now()

print("生成数据花费时间：",(endtime - starttime).seconds,"秒")
print("每秒生成数据：",round(v_counts/((endtime - starttime).seconds)),"条")