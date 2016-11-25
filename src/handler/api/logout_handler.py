#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handler.base_handler import BaseHandler


class LogoutHandler(BaseHandler):
    def do_action(self):
        self.clear_cookie('user_id')
        return True
