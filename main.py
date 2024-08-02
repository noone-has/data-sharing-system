from client import Client
import time
import utils

SERVER_IP = "77.167.223.13"
PORT = 8000

client = Client(SERVER_IP, PORT)
msg_history = {}

user_name = input("user name pls:")

print("starting loop")
while True:
    print("------------------------------")
    msg_history = client.get()
    msg_history = utils.process_messages(msg_history)
    print(msg_history)
    msg = input("Message(leave empty to skip):")
    if msg != '':
        client.post({user_name: msg})
