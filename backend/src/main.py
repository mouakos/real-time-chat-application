import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from backend.src.logging import setup_logging

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


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


@app.websocket("/ws/json")
async def websocket_json_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            name = data.get("name", "Unknown")
            message = data.get("message", "")

            response = {
                "status": "received",
                "message": f"Hello {name}, you said: {message}",
            }
            await websocket.send_json(response)

    except WebSocketDisconnect:
        print("WebSocket disconnected")
