# client/client.py
from . import utils
import socket

class Client:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.client_socket = None

    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_address, self.server_port))
        utils.log("Connected to server.")

    def send(self, message):
        self.client_socket.send(message.encode("utf-8"))
        utils.log(f"Sent: {message}")

        data = self.client_socket.recv(1024)
        data_str = data.decode("utf-8")
        utils.log(f"Received: {data_str}")

    def disconnect(self):
        self.client_socket.close()
        utils.log("Disconnected from server.")