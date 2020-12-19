#!/usr/bin/env python3
import socket
import os
import _thread as thread
import time
import json
stop_loop = False

def local_time(counter):
    return ' (LAMPORT_TIME={})'.format(counter)

def calc_recv_timestamp(recv_time_stamp, counter):
    return max(recv_time_stamp, counter) + 1

def send_message(client_ip, counter, sock):
    counter += 1
    data = json.dumps({"message":"Oi", "timestamp":counter})
    sock.send(data.encode())
    print('Message sent to {} at {}'.format(client_ip,local_time(counter)))
    return counter

def recv_message(client_ip, counter, sock, stop_loop):
    data = sock.recv(1024)
    data = json.loads(data.decode())
    message = data.get("message")
    timestamp = data.get("timestamp")
    counter = calc_recv_timestamp(timestamp, counter)
    if not message: # Se não há bytes pra ler, para o loop
        stop_loop = True
    else:
        print('Message received from {} at {}'.format(client_ip,local_time(counter)))
    return [counter, stop_loop]

def handle_client(conn, client_ip):
    counter = 0
    stop_loop = False
    with conn:
        print('Connected by', client_ip)
        while not stop_loop:
            counter, stop_loop = recv_message(client_ip, counter, conn, stop_loop)
            if stop_loop:
                print('Sem bytes')
                break
            time.sleep(10)
            counter = send_message(client_ip, counter, conn)
        conn.close()
    
if __name__ == '__main__': 

    HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
    PORT = 8888        # Port to listen on (non-privileged ports are > 1023)

    file = open('ips.txt', 'r')
    Lines = file.readlines()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Server started!')
        print('Waiting for clients...')
        while True:
            conn, addr = s.accept()
            thread.start_new_thread(handle_client,(conn,addr))
        s.close()