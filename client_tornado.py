import tornado.websocket
import tornado.ioloop
import json

class WebSocketClient(tornado.websocket.WebSocketClientConnection):
    async def send_message(self, message):
        await self.write_message(message)
        

async def connect_to_server():
    #url = "ws://213.226.126.185:5666/ws"
    url = "wss://ws-api.binance.com:443/ws-api/v3"
    client = await tornado.websocket.websocket_connect(url)
    await client.write_message(json.loads("""{
        \"id\": \"922bcc6e-9de8-440d-9e84-7c80933a8d0d\",
        \"method\": \"ping\"}
        """)
        )
    response = await client.read_message()
    print(f"Received: {response}")

if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(connect_to_server)