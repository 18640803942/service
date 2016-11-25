#!/usr/bin/env python
#-*- coding:utf-8 -*-

import uuid
import time


def print_stack():
    import traceback
    from util.logger import runtime_logger
    runtime_logger().info(traceback.format_exc().replace("\n", "####"))

def uniq_id(prefix=None):
    i = str(uuid.uuid4()).replace('-','')
    if not prefix:
        return i
    else:
        return '%s_%s' % (prefix, i)

def current_time(string = True):
    now = int(time.time())
    if string:
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))
    return now


