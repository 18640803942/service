#!/usr/bin/env python
# -*- coding:utf-8 -*-

import lib.db_helper


class USER_INFO():

    _table_name = 'USER_INFO'

    def __init__(self):
        self.db = lib.db_helper.Tassadar()

    def check_user(self, username, password):
        sql = 'select username, user_id from USER_INFO where username="%s" and password="%s" and is_del=0' % (username, password)
        res = self.db.query_one(sql)
        if res != {}:
            return res.as_dict()
        return False


if __name__ == '__main__':
    pass
