# Real-Time Notification System with WebSockets

A lightweight, real-time notification engine built with **FastAPI** and **WebSockets**. This application allows users to establish persistent WebSocket connections and receive instant notification updates.

---

## 🏗️ Architecture

- **Backend**: FastAPI manages WebSocket lifecycle connections and handles asynchronous message routing.
- **Connection Manager**: A custom class (`ConnectionManager`) tracks active client connections by `user_id`.
- **Frontend**: A minimal HTML/JS client (`index1.html`) connects to the WebSocket server and dynamically renders notifications upon receipt.

---

## 📁 File Structure

```text
.
├── connection_manager.py  # WebSocket connection manager logic
├── main.py                # FastAPI server and WebSocket endpoint routes
├── index1.html            # Client-side HTML interface
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation