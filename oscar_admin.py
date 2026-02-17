import http.server
import urllib.request
import urllib.error
import socketserver
import json

# ================= CONFIGURATION =================
# The address where your actual oscar-server is listening:
OSCAR_API_URL = "http://localhost:8080" 

# The port you will use to access the Dashboard in your browser:
PORTA_DASHBOARD = 9000
# ===============================================

class OscarProxy(http.server.SimpleHTTPRequestHandler):
    
    # 1. Enable OPTIONS support (CORS Pre-flight)
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    # 2. Method Routing
    def do_GET(self):
        if self.path.startswith('/api/'):
            self._proxy('GET')
        else:
            # Serve admin.html or other local static files
            super().do_GET()

    def do_POST(self): self._proxy('POST')
    def do_PUT(self): self._proxy('PUT')
    def do_DELETE(self): self._proxy('DELETE')

    # 3. Core Proxy Logic
    def _proxy(self, method):
        # Clean the URL (remove /api prefix and handle slashes)
        sub_path = self.path.replace('/api', '', 1)
        if not sub_path.startswith('/'): sub_path = '/' + sub_path
        
        target_url = OSCAR_API_URL + sub_path
        
        # Read request body sent by the Dashboard
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length) if content_length > 0 else None
        
        print(f"[PROXY] {method} request to {target_url}...")

        try:
            # Forward the request to the real oscar-server
            req = urllib.request.Request(target_url, data=body, method=method)
            req.add_header('Content-Type', 'application/json')
            
            with urllib.request.urlopen(req) as response:
                status = response.status
                response_data = response.read()
                self._send_response_to_browser(status, response_data)
                print(f"[SUCCESS] Status: {status}")

        except urllib.error.HTTPError as e:
            # Catch oscar-server errors (e.g., User already exists, Short password)
            status = e.code
            error_content = e.read().decode('utf-8')
            print(f"[OSCAR ERROR] {status}: {error_content}")
            self._send_response_to_browser(status, error_content, is_error=True)

        except Exception as e:
            # Catch network errors or offline server
            print(f"[NETWORK ERROR] {str(e)}")
            self._send_response_to_browser(500, {"error": "OSCAR Server unreachable", "details": str(e)})

    def _send_response_to_browser(self, status, data, is_error=False):
        self.send_response(status)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        if isinstance(data, dict):
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif isinstance(data, str):
            # If it's an error and not already JSON, wrap it in a JSON object
            if is_error and not data.startswith('{'):
                self.wfile.write(json.dumps({"msg": data}).encode('utf-8'))
            else:
                self.wfile.write(data.encode('utf-8'))
        else:
            self.wfile.write(data)

# Start the Server
print(f"\n--- OSCAR SERVER ADMIN DASHBOARD ---")
print(f"1. Ensure 'admin.html' is in the same folder as this script.")
print(f"2. Open your browser at: http://localhost:{PORTA_DASHBOARD}/admin.html")
print(f"3. In the Dashboard 'API Host' field, use: http://localhost:{PORTA_DASHBOARD}/api")
print(f"------------------------------------\n")

socketserver.TCPServer.allow_reuse_address = True
try:
    with socketserver.TCPServer(("0.0.0.0", PORTA_DASHBOARD), OscarProxy) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down proxy server...")
