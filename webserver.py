##  Example 4 - webservwere - server a simple html file
##  https://www.youtube.com/watch?v=hFNZ6kdBgO0
##  invoke in browser as http://localhost:8080/hello.html
from http.server import HTTPServer, BaseHTTPRequestHandler  

class Serv(BaseHTTPRequestHandler): 
  def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1: ]).read()
            self.send_response(200) 
        except:
            file_to_open = "404: File Not Found "
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()