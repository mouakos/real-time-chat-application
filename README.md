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

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern Python web framework
- **[WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)** - Real-time bidirectional communication
- **[Uvicorn](https://www.uvicorn.org/)** - ASGI server
- **[Pydantic](https://docs.pydantic.dev/)** - Data validation and settings management

### Frontend
- **[React 19](https://react.dev/)** - UI component library
- **[TypeScript](https://www.typescriptlang.org/)** - Type-safe JavaScript
- **[Vite](https://vitejs.dev/)** - Fast build tool and dev server

### DevOps
- **[Docker](https://www.docker.com/)** - Containerization platform
- **[Docker Compose](https://docs.docker.com/compose/)** - Multi-container orchestration
- **[Nginx](https://nginx.org/)** - Web server for production frontend

## 📋 Prerequisites

- **Python 3.13+**
- **Node.js 24+** and npm
- **Docker & Docker Compose** (for containerized deployment)
  
### 🚀 Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mouakos/real-time-chat-application.git
cd real-time-chat-application
```

### 2️⃣ Using Docker (Recommended)

**Configure environment:**
```bash
cp backend/.env.template backend/.env  # Edit as needed
```

**Start services:**
```bash
docker-compose up -d
```

**Access:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

**Manage services:**
```bash
docker-compose logs -f      # View logs
docker-compose down         # Stop services
docker-compose up --build   # Rebuild and start
```

### 3️⃣ Local Development Setup

**Backend:**
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate              # Windows
# source .venv/bin/activate         # macOS/Linux
pip install -r requirements.txt
cp .env.template .env               # Configure settings
fastapi dev                         # Runs on http://localhost:8000
```

**Frontend (new terminal):**
```bash
cd frontend
npm install
npm run dev                         # Runs on http://localhost:5173
```

## 🔌 API Endpoints

- `GET /` - API welcome message & health check
- `GET /docs` - Interactive API documentation (Swagger UI)
- `WS /ws/{client_id}` - WebSocket connection for real-time chat


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
## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Stephane Mouako**
- GitHub: [@mouakos](https://github.com/mouakos)

---

⭐ Star this repo if you find it helpful!