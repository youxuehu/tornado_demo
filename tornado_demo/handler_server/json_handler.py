# !/usr/bin/env python
# coding: UTF-8
from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler
import json
from tornado_demo import DEFAULT_STATIC_FILES_PATH, DEFAULT_TEMPLATE_PATH_LIST


class JsonHandler(IPythonHandler):
    def get(self):
        model = self.get_json_body()
        self.log.warn("model: %s" % model)
        data = dict()
        data["name"] = "jack"
        data["age"] = 20
        data["email"] = "jack@hotmail.com"
        data["address"] = "北京市昌平区天通苑一区10号302"
        self.log.warn("data: %s" % json.dumps(data))
        self.render("json.html", title="Json", data=data)

    def post(self):
        model = self.get_json_body()
        self.log.warn("model: %s" % model)
        self.finish(json.dumps(model))


def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    settings = {"template_path": DEFAULT_TEMPLATE_PATH_LIST, "static_path": DEFAULT_STATIC_FILES_PATH}
    web_app = nb_server_app.web_app
    web_app.settings.update(settings)
    host_pattern = ".*$"
    route_pattern = url_path_join(web_app.settings["base_url"], "/json")
    web_app.add_handlers(host_pattern, [(route_pattern, JsonHandler)])
