#!/usr/bin/env python3
import socket
import os
import thread
import time

def local_time(counter):
    return ' (LAMPORT_TIME={})'.format(counter)

def calc_recv_timestamp(recv_time_stamp, counter):
    return max(recv_time_stamp, counter) + 1

def handle_client(conn, addr):
    counter = 0
    with conn:
        print('Connected by', addr)
        while True:
            message, timestamp = conn.recv(1024)
            if not message:
                break
            time.sleep(10)
            counter += 1
            conn.send((message, counter))
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