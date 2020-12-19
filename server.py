#!/usr/bin/env python3
import socket
import os
import _thread as thread
import time
import json
import sys

stop_loop = False
global counter
counter = 0 # global var

def local_time():
    return ' (LAMPORT_TIME={})'.format(counter)

def calc_recv_timestamp(recv_time_stamp):
    return max(recv_time_stamp, counter) + 1

def send_message(client_ip, sock):
    global counter
    counter += 1
    data = json.dumps({"message":"Oi", "timestamp":counter})
    sock.send(data.encode())
    time.sleep(10)
    print('Message sent to {} at {}'.format(client_ip,local_time()))

def recv_message(client_ip, sock, stop_loop):
    try:
        data = sock.recv(1024)
        data = json.loads(data.decode())
        # message = data.get("message")
        timestamp = data.get("timestamp")
        print('timestamp:', timestamp)

        global counter
        counter = calc_recv_timestamp(timestamp)
        print('Message received from {} at {}'.format(client_ip,local_time()))
    except ValueError:
        # acabou os bytes
        stop_loop = True
    return stop_loop

# usa counter como uma variavel global
def handle_client(conn, client_ip):
    stop_loop = False
    with conn:
        global counter
        counter += 1
        print('Connected by {} at {}'.format(client_ip,local_time()))
        while not stop_loop:
            stop_loop = recv_message(client_ip, conn, stop_loop)
            if stop_loop:
                break
            send_message(client_ip, conn)
        conn.close()
    
def main():
    HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
    PORT = 8888        # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Server started!')
        print('Waiting for clients...')
        while True:
            conn, addr = s.accept()
            thread.start_new_thread(handle_client,(conn,addr))
        s.close()

if __name__ == '__main__': 

    try:
        main()
    except KeyboardInterrupt:
        print('Bye bye...')
        sys.exit(0)

    