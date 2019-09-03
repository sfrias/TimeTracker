import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Parsing a request")
        task = self.get_argument("mytask","")
        email = self.get_argument("email","")
        hit = self.get_argument("hit","")
        date = self.get_argument("date","")
        time = self.get_argument("time","")
        misite = self.get_argument("misite","")
        progress = self.get_argument("progress","")
        opt = self.get_argument("opt","")
        print(task, email, hit, date, time,
        misite, progress, opt)
        file = open("Requests.txt","a")
        file.write(task+";"+email+";"+hit+";"+
        date+";"+time+";"+misite+";"+progress+
        ";"+opt+"\n")
        file.close()

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(1024)
    tornado.ioloop.IOLoop.current().start()
