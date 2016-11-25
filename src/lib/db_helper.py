#!/usr/bin/env python
# -*- coding:utf-8 -*-

import records

from util.config import Configuration
from util.logger import api_logger
from util.tools import print_stack


class MySQLHelper:

    def __init__(self, database_url):
        self.logger = api_logger()
        try:
            self.db = records.Database(database_url)
        except Exception, e:
            self.logger.error(e.message)
            raise e

    def query(self, sql):
        rows = self.db.query(sql)
        res = [row.as_dict() for row in rows]
        return res

    def query_one(self, sql):
        rows = self.db.query(sql)
        result = [item for item in rows.all()]
        return result[0] if result else {}

    def un_query(self, sql):
        res = self.db.query(sql)
        return res

    def update(self, tb_name, bag, where):
        row_res = "%s" % ",".join(["`%s`='%s'" % (k, v.replace('\"', '\\"').replace("\'", "\\'") if isinstance(v, type(u"wuhao")) else v) for k, v in bag.items()])
        wrow = []
        for k, v in where.items():
            str = "`%s` = '%s'" % (k, v)
            wrow.append(str)
        wheres = ' and '.join(wrow)
        sql = 'UPDATE `%s` SET %s WHERE %s' % (tb_name, row_res, wheres)
        print sql
        res = self.db.query(sql)
        return res

    def insert(self, table_name, params):
        columns = ", ".join(['`' + key + '`' for key in params.keys()])
        values_template = ", ".join(["'%s'"] * len(params.keys()))
        sql = "INSERT INTO %s (%s) VALUES (%s)" % (
            table_name, columns, values_template)
        keys = params.keys()
        values = tuple(params[key] for key in keys)
        sql = sql % values
        res = self.db.query(sql)
        return res


def Tassadar():
    _db = 'tassadar'
    conf = Configuration().get_section(_db)
    database_url = conf.get('url')
    try:
        return MySQLHelper(database_url)
    except Exception, e:
        print e.message

        print_stack()
        return None


if __name__ == '__main__':
    pass



