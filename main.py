from fastapi import FastAPI, WebSocket
from connection_manager import manager

app = FastAPI()


@app.websocket("/ws/{user_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    user_id: int
):
    await manager.connect(user_id, websocket)

    try:
        while True:
            message = await websocket.receive_text()

            await manager.send_notification(
                user_id,
                message
            )

    except Exception:
        manager.disconnect(user_id)