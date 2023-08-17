# client/utils.py

import time

def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def log(message):
    current_time = get_current_time()
    print(f"[{current_time}] {message}\n")
    with open("client_log.txt", "a") as log_file:
        log_file.write(f"[{current_time}] {message}\n")
