#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handler.base_handler import BaseHandler
import tornado.web

class HomeHandler(BaseHandler):

    @tornado.web.authenticated
    def do_action(self):
        self.result = 'ok'
        return True
