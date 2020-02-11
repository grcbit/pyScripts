#---------------------------------------------------------
#Ejecuta un servidor HTTP sencillo que responde con 
#Hello World ante una peticion GET /
#---------------------------------------------------------
from http.server import HTTPServer, BaseHTTPRequestHandler

class handler_class(BaseHTTPRequestHandler):
  def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Hello world!"
        self.wfile.write(bytes(message))

#def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
def run(server_class=HTTPServer):
    server_address = ('', 8003)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

def hello():
    return

if __name__ == "__main__":
    run()
