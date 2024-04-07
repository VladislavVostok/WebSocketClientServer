import tornado.websocket
import tornado.ioloop

class WebSocketClient(tornado.websocket.WebSocketClientConnection):
    async def send_message(self, message):
        await self.write_message(message)
        

async def connect_to_server():
    url = "ws://213.226.126.185:5666/ws"
    client = await tornado.websocket.websocket_connect(url)
    await client.send_message("Сервак ты чтоли")
    response = await client.read_message()
    print(f"Received: {response}")

if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(connect_to_server)