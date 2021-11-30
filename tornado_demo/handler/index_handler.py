# !/usr/bin/env python
# coding: UTF-8
import tornado.web
from tornado.log import gen_log


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        gen_log.warn("start IndexHandler.")
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("index.html", title="Index", items=items)
