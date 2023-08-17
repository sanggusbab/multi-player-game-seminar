# client/main.py
from .client import Client

def main():
    client = Client("127.0.0.1", 12345)
    client.connect()
    client.send("Hello from client!")
    client.disconnect()

if __name__ == "__main__":
    main()
