# !/usr/bin/env python
# coding: UTF-8
import os


def pre_save_hook(model, path, contents_manager):
    log = contents_manager.log
    log.info("前置保存 model： %s" % model)
    log.info("前置保存 path： %s" % path)
    log.info("前置保存 content_manager： %s" % contents_manager)


def post_save_hook(model, os_path, contents_manager):
    log = contents_manager.log
    base, ext = os.path.splitext(os_path)
    log.info("后置保存 base： %s" % base)
    log.info("后置保存 ext： %s" % ext)
    log.info("后置保存 model： %s" % model)
    log.info("后置保存 os_path： %s" % os_path)
    log.info("后置保存 content_manager： %s" % contents_manager)
