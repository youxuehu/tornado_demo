# !/usr/bin/env python
# coding: UTF-8
from tornado_demo.sqllite3db import database


class User(object):

    def __init__(self):
        self.conn = database.Connection(":memory:")

    def create_table(self):
        script = """
        create table user_info (id VARCHAR(255), name VARCHAR(255), owner VARCHAR(255), biz_date VARCHAR(255), gmt_create VARCHAR(255),
         gmt_update VARCHAR(255), gmt_delete VARCHAR(255), operate_create VARCHAR(255), operate_update VARCHAR(255), 
         operate_delete VARCHAR(255), is_deleted VARCHAR(255));
        """
        self.conn.execute(script)

    def insert_table(self, user):
        script = """
        insert into user_info(id, name, owner, biz_date, gmt_create, gmt_update, gmt_delete, operate_create, operate_update, 
        operate_delete, is_deleted) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """ % (user.get("id"), user.get("name"), user.get("owner"), user.get("biz_date"), user.get("gmt_create"), user.get("gmt_update"),  # noqa
               user.get("gmt_delete"), user.get("operate_create"), user.get("operate_update"), user.get("operate_delete"), user.get("is_deleted"), )  # noqa

        print(script)
        self.conn.execute(script)

    def query(self):
        return self.conn.query("select * from user_info;")
