import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from app.connection_manager import manager

from app.logging import setup_logging

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


@app.get("/", response_model=dict[str, str])
async def root() -> dict[str, str]:
    return {
        "message": "Welcome to the Real-Time Chat Application! Visit /docs for API documentation."
    }


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):

    origin = websocket.headers.get("origin")
    if origin not in origins:
        logger.warning(f"Connection attempt from disallowed origin: {origin}")
        await websocket.close(code=1008)  # Policy Violation
        return

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
