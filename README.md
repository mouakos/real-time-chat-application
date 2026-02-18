# real-time-chat-application

## Requirements

- Real-time interaction required ➡️ messages must appears instantly for all users
- Broadcasting ➡️ one user's message must reach all other users immediately
- Low latency essential ➡️ delay break the user experience
- Simple but powerful architecture ➡️ easy to understand, yet demonstrates core Websocket concepts
- Bidirectional communication ➡️ both clients and server can send data anytime
- Multiple concurrent users ➡️ many clients connected at once, exchanging data
- Scale naturally ➡️ from 2 users to many, showing FastAPI's async capabilities


## Key Technical Aspects

- Multiple users for the app
- Simultaneous connections (async)
- Broadcast messages
- Handle disconnects
  
## Architecture

- FastAPI Backend for managing Websockets
- Simple Frontend (React) for connections, Messages, and the chat window
- Clint connects to the server which accepts the connection
- Client sends a message, and the server needs o broadcast to all clients

## Frontend (React) requirements

- Establish Websocket connection to FastAPI backend
- Maintain chat state ➡️ list of messages in components state
- Display messages in real time ➡️ render new messages as they arrive
- Provide input field for composing messages
- Send messages over websocket when user submits input

## Connection and User Management

- Handle connection lifecycle ➡️ on open, on message, on close
- Generate unique client ID for identification
- Shown own client ID
- clean up on unmount ➡️ close Websocket to prevent leaks

## System requirements

- Node.js (>=22.12.0)
- Installed create-vite command