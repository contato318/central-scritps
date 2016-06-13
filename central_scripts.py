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

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def get(self):
        self.write("-")

class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        msg="OPS"
        self.render("error.html",title=title,msg=msg)
    def post(self):
        self.write("OPS")


class LoginHandler(BaseHandler):
    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

    def post(self):
        self.set_secure_cookie("user", self.get_argument("name"))
        self.redirect("/")


def main():
    settings = {
        'default_handler_class': ErrorHandler,
        'template_path': os.path.join(os.path.dirname(__file__), "template"),
        'cookie_secret': "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        'login_url': "/login"
    }
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/login", LoginHandler),
            (r"/favicon.ico", tornado.web.ErrorHandler, {'status_code': 404}),
            ],
        debug=options.debug,
        **settings
        )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

