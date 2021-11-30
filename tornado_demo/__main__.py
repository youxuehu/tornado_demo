# !/usr/bin/env python
# coding: UTF-8
import tornado.ioloop
import tornado.web
from tornado_demo.handler.main_handler import MainHandler
from tornado_demo.handler.index_handler import IndexHandler
from tornado.log import gen_log
from tornado_demo import DEFAULT_STATIC_FILES_PATH, DEFAULT_TEMPLATE_PATH_LIST


def make_app():
    settings = {"template_path": DEFAULT_TEMPLATE_PATH_LIST, "static_path": DEFAULT_STATIC_FILES_PATH}
    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/index", IndexHandler),
        ],
        **settings,
    )


def main():
    app = make_app()
    app.listen(8888)
    gen_log.warn("tornado server start...")
    tornado.ioloop.IOLoop.current().start()
