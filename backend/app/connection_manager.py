import asyncio
from typing import Set
from fastapi import WebSocket
import logging

logger = logging.getLogger("connection_manager")


class ConnectionManager:
    def __init__(self) -> None:
        """Initialize the ConnectionManager with an empty set of active connections."""
        self.active_connections: Set[WebSocket] = set()

    async def connect(self, websocket: WebSocket) -> None:
        """Accept a new WebSocket connection and add it to the active connections set.

        Args:
            websocket: The WebSocket connection to accept and add.
        """
        await websocket.accept()
        self.active_connections.add(websocket)
        logger.info(f"Client connected. Active={len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket) -> None:
        """Remove a WebSocket connection from the active connections set.

        Args:
            websocket: The WebSocket connection to remove.
        """
        self.active_connections.discard(websocket)
        logger.info(f"Client disconnected. Active={len(self.active_connections)}")

    async def send_personal_message(self, message: str, websocket: WebSocket) -> None:
        """Send a personal message to a specific WebSocket connection.

        Args:
            message: The message to send.
            websocket: The WebSocket connection to send the message to.
        """
        await websocket.send_text(message)

    async def broadcast(self, message: str, exclude: WebSocket = None) -> None:
        """Broadcast a message to all active connections, optionally excluding one.

        Args:
            message: The message to send.
            exclude: A WebSocket connection to exclude from the broadcast (e.g., the sender).
        """
        send_tasks = []
        for connection in self.active_connections:
            if exclude and connection == exclude:
                continue
            send_tasks.append(connection.send_text(message))

        # Shield against single client failures so one bad connection doesn't break the whole broadcast
        if send_tasks:
            try:
                await asyncio.gather(*send_tasks, return_exceptions=True)
            except Exception:
                logger.exception("Error broadcasting message")


manager = ConnectionManager()
