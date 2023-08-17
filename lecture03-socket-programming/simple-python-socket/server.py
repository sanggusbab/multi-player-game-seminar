import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen(5)

    print("Server listening on 127.0.0.1:12345")

    client_socket, client_address = server_socket.accept()
    print("Accepted connection from", client_address)

    data = client_socket.recv(1024)
    print("Received from client:", data.decode("utf-8"))

    client_socket.send(b"Hello from server!")
    client_socket.close()

    server_socket.close()

if __name__ == "__main__":
    main()
