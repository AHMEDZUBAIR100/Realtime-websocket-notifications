from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):
        self.connections = {}

    async def connect(
        self,
        user_id: int,
        websocket: WebSocket
    ):
        await websocket.accept()

        self.connections[user_id] = websocket

        print(f"User {user_id} connected")

    def disconnect(self, user_id: int):

        if user_id in self.connections:
            del self.connections[user_id]

        print(f"User {user_id} disconnected")

    async def send_notification(
        self,
        user_id: int,
        message: str
    ):

        websocket = self.connections.get(user_id)

        if websocket:
            await websocket.send_text(message)


manager = ConnectionManager()