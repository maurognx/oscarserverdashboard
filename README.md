# OSCAR Server Admin Dashboard

A lightweight, web-based administration panel for the [oscar-server]([(https://github.com/mk6i/open-oscar-server)) (AIM/ICQ protocol emulator). This tool provides a clean UI to manage users, chat rooms, and active sessions without dealing with complex CLI commands or PowerShell scripts.



## ⚠️ Internal Testing Only
**DISCLAIMER:** This project is intended for **internal testing and development purposes only**. It is not designed for production environments. The proxy included here bypasses CORS for ease of use in local labs and does not implement additional authentication layers beyond what is provided by the base server.

---

## 🚀 Features
* **User Management:** Create, delete, and list users (UIN/Screen Names).
* **Password Control:** Easily update user passwords via the UI.
* **Chat Room Management:** Create and monitor public chat rooms.
* **Session Tracking:** View real-time active sessions on the server.
* **Automatic Proxy:** Built-in Python proxy to handle CORS issues and serve the frontend seamlessly.

## 🛠️ Prerequisites
* **Python 3.x** installed on the server.
* An active instance of **oscar-server** running (defaulting to port 8080).

## 📥 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/maurognx/oscarserverdashboard/oscar-admin-dashboard.git](https://github.com/maurognx/oscarserverdashboard/oscar-admin-dashboard.git)
   cd oscar-admin-dashboard
