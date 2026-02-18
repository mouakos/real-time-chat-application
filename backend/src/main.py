import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from src.connection_manager import manager

from src.logging import setup_logging

setup_logging()

logger = logging.getLogger("chat_app")


app = FastAPI(title="Real-Time Chat Application", version="1.0.0")

# -- CORS (allow Vite frontend to connect) --

origins = [
    "http://localhost:5173",  # Vite dev server
    "http://127.0.0.1:5173",  # FastAPI server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    try:
        await manager.broadcast(f"Client #{client_id} joined the chat")
        while True:
            data = await websocket.receive_text()

            # Echo back to sender
            await manager.send_personal_message(f"You wrote: {data}", websocket)

            # Broadcast to others
            await manager.broadcast(
                f"Client #{client_id} says: {data}", exclude=websocket
            )
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
    except Exception:
        #  Any unexpected error: log and close the connection gracefully
        logger.exception("Unexpected error in WebSocket connection")
        try:
            await websocket.close()
        finally:
            manager.disconnect(websocket)
            await manager.broadcast(
                f"Client #{client_id} left the chat due to an error"
            )
