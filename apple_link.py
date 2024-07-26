import http.server
import socketserver
import os

PORT = 8001

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        if self.path == '/apple-app-site-association':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            with open('apple-app-site-association', 'rb') as file:
                self.wfile.write(file.read())
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

