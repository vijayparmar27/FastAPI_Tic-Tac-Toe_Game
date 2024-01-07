from .server import apiServer
import socketio
from main.eventRequestHandler.index import requestHandler

class SocketIO:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self._url = "redis://localhost:6379/0"

        self.sio = socketio.AsyncServer(
            async_mode='asgi',
            cors_allowed_origins="*",
            client_manager=socketio.AsyncRedisManager(self._url),
        )
        self.app = socketio.ASGIApp(self.sio, apiServer)

        # Socket.IO connection event handler
        @self.sio.event
        async def connect(sid, environ):
            print(f"Client connected: {sid}")

        # Socket.IO disconnect event handler
        @self.sio.event
        async def disconnect(sid):
            print(f"Client disconnected: {sid}")

        @self.sio.on("*")
        async def any_event(event,sid, data):
            return await requestHandler(event, sid, data,self.sio)

        

    async def handle_message(self, sid, data):
        print(f"Message from {sid}: {data}")
        await self.sio.enter_room(sid, "chat")
        await self.sio.emit(event="message", data=data, room="chat")

    

# Usage:
socket_io_app = SocketIO()

app = socket_io_app.app


