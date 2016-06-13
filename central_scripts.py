#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tornado.escape
import tornado.ioloop
import tornado.web
import sys
import os
from tornado.concurrent import Future
from tornado import gen
from tornado.options import define, options, parse_command_line


define("port", default=8081, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")
title="Central de Scripts"


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("-")
class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        msg="OPS"
        self.render("error.html",title=title,msg=msg)
    def post(self):
        self.write("OPS")

def main():
    settings = {
        'default_handler_class': ErrorHandler,
        'template_path': os.path.join(os.path.dirname(__file__), "template"),
    }
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/favicon.ico", tornado.web.ErrorHandler, {'status_code': 404}),
            ],
        debug=options.debug,
        **settings
        )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

