# OSCAR Server Admin Dashboard

A lightweight, web-based administration panel for the [oscar-server](https://github.com/mk6i/open-oscar-server) (AIM/ICQ protocol emulator). This tool provides a clean UI to manage users, chat rooms, and active sessions without dealing with complex CLI commands or PowerShell scripts.



## ⚠️ Internal Testing Only
**DISCLAIMER:** This project is intended for **internal testing and development purposes only**. It is not designed for production environments. The proxy included here bypasses CORS for ease of use in local labs and does not implement additional authentication layers beyond what is provided by the base server. Use it within your trusted home lab or private network.

---

## 🚀 Features
* **User Management:** Create, delete, and list users (UIN/Screen Names).
* **Password Control:** Easily update user passwords via the UI.
* **Chat Room Management:** Create and monitor public chat rooms.
* **Session Tracking:** View real-time active sessions on the server.
* **Automatic Proxy:** Built-in Python proxy to handle CORS issues and serve the frontend seamlessly.
* **Persistent Config:** Remembers your API host settings using browser LocalStorage.

## 🛠️ Prerequisites
* **Python 3.x** installed on the server.
* An active instance of **oscar-server** running (defaulting to port 8080).

## 📥 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/maurognx/oscarserverdashboard.git](https://github.com/maurognx/oscarserverdashboard.git)
    cd oscarserverdashboard
    ```

2.  **Verify File Structure:**
    Ensure `admin.html` and `oscar_admin.py` are in the same directory.

3.  **Run the Dashboard:**
    ```bash
    python3 oscar_admin.py
    ```

## 🖥️ Usage

1.  Open your browser and navigate to `http://your-server-ip:9000/admin.html`.
2.  In the **API Host** field at the top, enter the proxy URL:
    `http://your-server-ip:9000/api`
3.  Click **Enter** (or tab out) to save. The "Saved!" message will appear.
4.  Start managing your ICQ/AIM users!



## 🔧 Architecture (The "CORS" Solution)
Modern browsers enforce strict **CORS (Cross-Origin Resource Sharing)** policies. Since the base `oscar-server` does not send CORS headers, a direct web-to-server connection usually fails. 

This project solves this by acting as a **Reverse Proxy**:
1.  The **Python Script** serves the static `admin.html` file.
2.  It creates an `/api` route that intercepts requests from the browser.
3.  The script then forwards these requests to the local `oscar-server` and injects the required `Access-Control-Allow-Origin` headers into the response.

## 🤝 Contributing
Contributions are welcome! If you want to add retro-style CSS skins (Win98/XP style) or new administrative features, feel free to open an Issue or a Pull Request.

## 📜 License
This project is open-source under the MIT License. Use it responsibly for your retro-computing labs!
