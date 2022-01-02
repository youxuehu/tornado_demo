# !/usr/bin/env python
# coding: UTF-8
import unittest
from tornado_demo.sqllite3db.user import User
import datetime


class TestUserInfo(unittest.TestCase):
    def setUp(self):
        self.user = User()
        user_dic = dict()
        user_dic["id"] = "1000"
        user_dic["name"] = "tiger"
        user_dic["owner"] = "WB520289"
        user_dic["biz_date"] = "2021-12-01 22:05:11"
        user_dic["gmt_create"] = "2021-12-01 22:05:11"
        user_dic["gmt_update"] = "2021-12-01 22:05:11"
        user_dic["gmt_delete"] = "2021-12-01 22:05:11"
        user_dic["operate_create"] = "WB520289"
        user_dic["operate_update"] = "WB520289"
        user_dic["operate_delete"] = "WB520289"
        user_dic["is_deleted"] = "0"
        self.user_dic = user_dic

    def test_crate_table(self):
        self.user.create_table()

    def test_insert_table(self):

        self.user.insert_table(self.user_dic)

    def test_query(self):
        # self.test_crate_table()
        # self.test_insert_table()
        self.user.create_table()
        self.user.insert_table(self.user_dic)
        user_list = self.user.query()
        print(user_list)


if __name__ == "__main__":
    unittest.main()
