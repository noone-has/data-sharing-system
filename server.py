from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import utils
from ast import literal_eval

# get msg history
msg_history = open("msg_history.txt", "r").read()
msg_history = utils.remove_from_string(msg_history, "\n")
msg_history = literal_eval(msg_history)
# -
print(f"history:{msg_history}")
class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(str(msg_history).encode('utf-8'))

    def do_POST(self):
        self.send_response(200)
        self.end_headers()

        request = self.rfile
        data = request.read()
        data = json.loads(data)

        msg_history.update(data)
        open("msg_history.txt", "w").write(str(msg_history).replace("'", "\""))
        print(data)


def create_server(host, port):
    server = HTTPServer((host, port), Server)
    return server


server = create_server("192.168.2.14", 8000)
server.serve_forever()
