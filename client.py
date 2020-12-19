#!/usr/bin/env python3

import socket
import urllib.request

def event(port, counter):
    counter += 1
    print('Something happened in {} !'.\
          format(pid) + local_time(counter))
    return counter

def send_message(port, counter):
    counter += 1
    pipe.send(('Empty shell', counter))
    print('Message sent from ' + str(pid) + local_time(counter))
    return counter

def recv_message(port, counter):
    message, timestamp = pipe.recv()
    counter = calc_recv_timestamp(timestamp, counter)
    print('Message received at ' + str(pid)  + local_time(counter))
    return counter

if __name__ == '__main__': 

    HOST = '143.106.219.143'  
    PORT = 65432        # The port used by the server


    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

    print(external_ip)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        event(port, counter)
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    print('Received', repr(data))
