# !/usr/bin/env python
# coding: UTF-8
from tornado_demo.sqllite3db import database

conn = database.Connection(":memory:")

conn.execute("create table users (id bigint, name char(10));")
for i in range(1000):
    conn.execute("insert into  users (id, name) values (" + str(i) + ', "jack");')

for user in conn.query("select * from users"):
    print(user)
