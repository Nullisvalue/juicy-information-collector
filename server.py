import http.server 

host = '192.168.1.120'
port = 80

class postreader(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
                self.send_response(200)
                self.end_headers()
                data = int(self.headers['Content-length'])
                post = self.rfile.read(data)
                
                print(post.decode())
                
runserver = http.server.HTTPServer
server0 = runserver((host,port),postreader)
server0.serve_forever()