# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import stableDiffusion2


hostName = "localhost"
serverPort = 6969
imggen = stableDiffusion2.theAlgo()

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        stuff = self.path
        imggen.generate(stuff)
        print(stuff)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")