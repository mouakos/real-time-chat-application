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

## 🛠️ Tech Stack

**Backend:**
- FastAPI
- Python 3.13
- WebSocket
- Uvicorn

**Frontend:**
- React 19
- TypeScript
- Vite
- CSS3

## 📋 Prerequisites

- Python >= 3.13
- Node.js >= 24.13.1
- npm

## 🚀 Quick Start

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd real-time-chat-application
```

### 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
fastapi dev src/main.py
```

Backend runs on: `http://localhost:8000`

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on: `http://localhost:5173`

### 4️⃣ Start Chatting!

Open `http://localhost:5173` in your browser and start chatting! 🎉

Open multiple tabs to test multi-user functionality.

## 📁 Project Structure

```
real-time-chat-application/
├── backend/
│   ├── src/
│   │   ├── main.py              # FastAPI app & WebSocket endpoint
│   │   ├── connection_manager.py
│   │   └── logging.py
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/
    │   │   └── ChatApp.tsx      # Main chat component
    │   ├── App.tsx
    │   └── styles.css
    └── package.json
```

## ⚙️ Configuration

### Custom WebSocket URL

Create `.env` in the `frontend` directory:

```env
VITE_WS_URL=ws://localhost:8000
```

### CORS Settings

Edit `origins` in `backend/src/main.py` to add allowed origins.

## 🏗️ Building for Production

### Frontend
```bash
cd frontend
npm run build
```
Output: `frontend/dist/`

### Backend
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📝 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Your Name**
- GitHub: [@mouakos](https://github.com/mouakos)

---

⭐ Star this repo if you find it helpful!