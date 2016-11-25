#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import glob
import tornado.ioloop
import tornado.web
import tornado.httpserver
from util.config import Configuration
import handler
import util.logger

reload(sys)
sys.setdefaultencoding('utf-8')


class ServerApplication(tornado.web.Application):
    def __init__(self, api_entry, **settings):
        self.logger = util.logger.api_logger()
        handlers = self.load_handlers(api_entry)
        super(ServerApplication, self).__init__(handlers, **settings)

    def load_handlers(self, m):
        handlers = []
        append_uri = []
        if hasattr(m, "__all__"):
            for sub_module in m.__all__:
                handler_files = glob.glob('%s/%s/%s/*_handler.py' % (os.getenv('SRC'), m.__name__, sub_module))
                for handler_file in handler_files:
                    handler_name, ext = os.path.splitext(os.path.basename(handler_file))
                    handler_split = handler_name.split("_")
                    module = "%s.%s.%s" % (m.__name__, sub_module, handler_name)
                    attr = "%sHandler" % handler_split[0].capitalize()
                    __import__(module)
                    uri = r"/%s/%s" % (sub_module, handler_split[0])
                    if uri not in append_uri:
                        handlers.append((uri, "%s.%s" % (module, attr)))
                        append_uri.append(uri)
                        sys.stderr.write("routing uri %s to handler %s\n" % (uri, "%s.%s" % (module, attr)))
        return handlers

    def log_request(self, handler):
        if handler.get_status() == 0:
            self.logger.info(handler.get_log_info())
        else:
            self.logger.error(handler.get_log_info())


def main():
    port = Configuration().get("global", "port")
    debug_model = int(Configuration().get('global', 'debug'))
    sys.stderr.write("listen server on port %s ..\n" % port)
    application = ServerApplication(handler, **{
        'debug':True if debug_model else False,
        "cookie_secret": "18640803942",
        "login_url": "/api/login"
    })
    server = tornado.httpserver.HTTPServer(application, max_buffer_size=1024*1024*1024)
    server.bind(port)
    server.start(1 if debug_model else 10)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
