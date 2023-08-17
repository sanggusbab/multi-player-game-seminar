import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))

    message = "Hello from client!"
    client_socket.send(message.encode("utf-8"))

    response = client_socket.recv(1024)
    print("Received from server:", response.decode("utf-8"))

    client_socket.close()

if __name__ == "__main__":
    main()
