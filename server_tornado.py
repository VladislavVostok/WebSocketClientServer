import tornado.web
import tornado.websocket
import tornado.ioloop
from tornado.routing import HostMatches



class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(f"You said: {message}")


    def on_close(self):
        print("WebSocket closed")


app = tornado.web.Application([
            (HostMatches("213.226.126.185"), [
                (r"/", WebSocketHandler),
            ]),
        ])

if __name__ == "__main__":
    app.listen(5666)
    tornado.ioloop.IOLoop.current().start()
