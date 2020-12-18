#!/usr/bin/env python3
import socket
import os

HOST = '143.106.219.143'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

file = open('ips.txt', 'r') 
Lines = file.readlines() 
  
count = 0
# Strips the newline character 
# for line in Lines: 
#     ip, name = line.split()
#     print(ip)
#     print(name)
    #print("Line{}: {}".format(count, line.strip())) 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)