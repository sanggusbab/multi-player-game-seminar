# server/main.py
from .server import Server

def main():
    server = Server("127.0.0.1", 12345)
    server.start()

if __name__ == "__main__":
    main()
