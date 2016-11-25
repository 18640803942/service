#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handler.base_handler import BaseHandler
from model.user_info import USER_INFO


class LoginHandler(BaseHandler):
    def do_action(self):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        if username is None or password is None:
            self.set_error(self.error_code.PARAMETERS_INVALID, "参数错误")
            return True
        flag = USER_INFO().check_user(username, password)
        if flag:
            user_id = flag['user_id']
            self.set_secure_cookie("user_id", user_id)
        else:
            self.set_error(self.error_code.USER_INFO_ERROR, "用户信息错误")
            return True
        self.result = {
            'info': flag,
        }
        return True
