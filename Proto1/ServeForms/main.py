import os
#import time
import tornado.ioloop
import tornado.web
#import tornado.autoreload

root = os.path.dirname(__file__)
print (__file__, root)
port = 1234

#def absolutpath(*paths):
    #for p in paths:
        #print(os.path.abspath(p))
        #tornado.autoreload.watch(os.path.abspath(p))

#def wreload():
    #time.sleep(0.5)  #intentionally so it will be short on upload
    #print("reloading: exiting...")

application = tornado.web.Application([
    (r"/(.*)", tornado.web.StaticFileHandler,
    {"path": root, "default_filename": "index.html"})
    ], debug=True)

if __name__ == '__main__':
    application.listen(port)
    #tornado.autoreload.start()
    #tornado.autoreload.watch("index.html")
    #tornado.autoreload.add_reload_hook(wreload)
    tornado.ioloop.IOLoop.instance().start()