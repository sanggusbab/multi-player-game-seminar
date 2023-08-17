# server/server.py
from . import utils
import socket
import signal
import sys

class Server:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.server_socket = None
        self.running = True

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.address, self.port))
        self.server_socket.listen(5)

        utils.log(f"Server listening on {self.address}:{self.port}")

        def signal_handler(sig, frame):
            self.running = False
            self.server_socket.close()
            utils.log("Server stopped.")
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)

        try:
            while self.running:
                client_socket, client_address = self.server_socket.accept()
                utils.log(f"Accepted connection from {client_address}")
                
                client_socket.send(b"Welcome to the server!")

                data = client_socket.recv(1024)
                data_str = data.decode("utf-8")
                utils.log(f"Received data from client: {data_str}")

                client_socket.send(data)  # Echo back the received data

                client_socket.close()

        except KeyboardInterrupt:
            self.running = False
            self.server_socket.close()
            utils.log("Server stopped.")

def main():
    server = Server("127.0.0.1", 12345)
    server.start()

if __name__ == "__main__":
    main()
