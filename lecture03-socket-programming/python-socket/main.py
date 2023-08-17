import sys
import signal
from client import main as client_main
from server import main as server_main

def signal_handler(sig, frame):
    print("\nExiting...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <client|server>")
        return

    mode = sys.argv[1]

    if mode == "client":
        client_main()
    elif mode == "server":
        server_main()
    else:
        print("Invalid mode. Use 'client' or 'server'.")

if __name__ == "__main__":
    main()
