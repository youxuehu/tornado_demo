# !/usr/bin/env python
# coding: UTF-8
import tornado.web
from tornado.log import gen_log


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        gen_log.warn("start MainHandler")
        self.write("Hello, world")
