#! /usr/bin/env python3
##
# Dynamic server mode
#
# This is useful for development because you can see the changes made
# in real time.
##

import j2static.main

from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver

PORT = 8082

_jinja = j2static.main.TemplateEngine()

class TemplateHTTPServer(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
        print("constructor called")

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        file_path = self.path
        if file_path == "/":
            file_path = "index.html"

        _jinja.load_data_dir("data/")

        data = _jinja.render(file_path)
        self.wfile.write(data.encode())


def serve():
    Handler = TemplateHTTPServer
    httpd = HTTPServer(('', PORT), Handler)
    httpd.serve_forever()
