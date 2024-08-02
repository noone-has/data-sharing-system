import requests
import json
class Client():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def post(self, data):
        try:
            requests.post(url=f"http://{self.ip}:{self.port}", json=data, timeout=1)
        except requests.exceptions.ConnectionError:
            pass

    def get(self):
        r = requests.get(url=f"http://{self.ip}:{self.port}")
        string = r.content.decode('utf-8').replace("'", "\"")
        data = json.loads(string)
        return data
