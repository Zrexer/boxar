#!/usr/bin/env python3

import os
os.system('')
import socket
import time
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) <= 1:
    dateXZ = time.strftime('%H:%M:%S')
    raise ValueError(f"\033[97m[\033[96m{dateXZ}\033[97m] [\033[91merror\033[97m]::\033[93musage -> python3 serverSide.py --ip 127.0.0.1 --port 1231\033[97m")

ip = str(sys.argv[sys.argv.index('--ip')+1])
port = int(sys.argv[sys.argv.index('--port')+1])

server.bind((ip, port))
t1 = time.strftime('%H:%M:%S')
try:
    server.listen()
except KeyboardInterrupt or Exception as KIE1:
    print(f'\033[97m[\033[96m{t1}\033[97m] [\033[92minfo\033[97m]::\033[93mexit')
    exit()

while 1:
    try:
        listenTime = time.strftime('%H:%M:%S')
        print(f'\r\033[97m[\033[96m{listenTime}\033[97m] [\033[92minfo\033[97m]::\033[93mserver on listener mode ...\033[97m\n', end="", flush=False)
        time.sleep(1)
        if server.accept:
            client, address = server.accept()
            newTime = time.strftime('%H:%M:%S')
            data = client.recv(1024).decode('ascii')
            print(f"\033[97m[\033[96m{newTime}\033[97m] [\033[92minfo\033[97m]::\033[93mclient connected\033[97m")
            print(f"\033[97m[\033[96m{newTime}\033[97m] [\033[92maddress\033[97m]::\033[93m{address[0]}\033[97m")
            print(f"\033[97m[\033[96m{newTime}\033[97m] [\033[92mport\033[97m]::\033[93m{address[1]}\033[97m")
            print(data)
        else:pass
    except KeyboardInterrupt or Exception as KIE:
        print(f'\033[97m[\033[96m{listenTime}\033[97m] [\033[92minfo\033[97m]::\033[93mexit\033[97m')
        exit()

afterWhile = time.strftime('%H:%M:%S')
print(f"\033[97m[\033[96m{afterWhile}\033[97m] [\033[92minfo\033[97m]::\033[93mtry to execute values ...\033[97m\n")

