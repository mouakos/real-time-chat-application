# Real-Time Chat Application 💬

A simple WebSocket-based real-time chat application built with FastAPI and React.

![Chat Demo](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![Node](https://img.shields.io/badge/node-24.13.1-green.svg)

## ✨ Features

- 🚀 Real-time messaging with WebSocket
- 👥 Multiple concurrent users support
- 🔄 Auto-reconnect functionality
- 🎨 Modern, responsive dark-themed UI
- 📱 Visual connection status indicators
- 🆔 Unique client identifiers
- 🔔 System notifications for user join/leave events
- 🐳 Docker & Docker Compose support

## 🛠️ Tech Stack

**Backend:** FastAPI, WebSocket 
**Frontend:** React, TypeScript, Vite

## 🚀 Quick Start

### Using Docker (Recommended)

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

Access:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

### Local Development

**Backend:**
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
fastapi dev
```
Backend runs on: `http://localhost:8000`

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

Frontend runs on: `http://localhost:5173`

## 🔌 API Endpoints

- `GET /` - API welcome message & health check
- `GET /docs` - Interactive API documentation (Swagger UI)
- `WS /ws/{client_id}` - WebSocket connection for real-time chat

## ⚙️ Configuration

Create a `.env` file in the `backend/` directory:

```bash
cp backend/.env.template backend/.env
```

Configure CORS allowed origins:

```env
# CORS Configuration
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

Add any additional origins as comma-separated values. See `backend/.env.template` for reference.

## 🎉 Start Chatting!

- **Local Development:** Open `http://localhost:5173`
- **Docker:** Open `http://localhost:3000`

Open multiple browser tabs or windows to test multi-user chat functionality!

## 📁 Project Structure

```
real-time-chat-application/
├── docker-compose.yml           # Docker orchestration
├── .dockerignore                # Docker ignore patterns
├── backend/
│   ├── Dockerfile               # Backend container config
│   ├── requirements.txt         # Python dependencies
│   └── src/
│       ├── main.py              # FastAPI app & WebSocket endpoint
│       ├── connection_manager.py # WebSocket connection handler
│       └── logging.py           # Logging configuration
└── frontend/
    ├── Dockerfile               # Frontend container config
    ├── nginx.conf               # Nginx configuration
    ├── package.json             # Node dependencies
    └── src/
        ├── components/
        │   └── ChatApp.tsx      # Main chat component
        ├── App.tsx              # Root component
        └── styles.css           # Global styles
```
##  License

MIT

## 👨‍💻 Author

[@mouakos](https://github.com/mouakos)

---

⭐ Star this repo if you find it helpful!