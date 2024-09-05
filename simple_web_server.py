
from http.server import SimpleHTTPRequestHandler, HTTPServer

hostName = "0.0.0.0"
serverPort = 8086

class MyServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Simple Web Server</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>This is a simple web server.</p></body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started at http://{hostName}:{serverPort}")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
