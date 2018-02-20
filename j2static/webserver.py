#! /usr/bin/env python3
##
# Dynamic server mode
#
# This is useful for development because you can see the changes made
# in real time.
##

import main

from http.server import BaseHTTPRequestHandler
import socketserver

PORT = 8082


class TemplateHTTPServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        data = main.render('index.html')
        self.wfile.write(data.encode())


Handler = TemplateHTTPServer
httpd = socketserver.TCPServer(("", PORT), Handler)
httpd.serve_forever()
httpd.close()
