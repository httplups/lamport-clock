#!/usr/bin/env python3

import socket
import urllib.request


def local_time(counter):
    return ' (LAMPORT_TIME={})'.format(counter)

def calc_recv_timestamp(recv_time_stamp, counter):
    return max(recv_time_stamp, counter) + 1

def event(ip, counter):
    counter += 1
    # print('Something happened in {} !'.\
    #       format(pid) + local_time(counter))
    print('Something happened in {} '.format(ip), local_time(counter))
    return counter

def send_message(ip, counter, sock):
    counter += 1
    data = 'Hello from {}'.format(ip)
    s.send((data,counter))
    print('Message sent from {}'.format(ip),local_time(counter))
    return counter

def recv_message(ip, counter, sock):
    message, timestamp = sock.recv(1024)
    counter = calc_recv_timestamp(timestamp, counter)
    print('Message received at {}'.format(ip),local_time(counter))
    return counter

if __name__ == '__main__': 

    HOST = '52.90.198.186'
    PORT = 8888        # The port used by the server
    counter = 0
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        counter = event(external_ip, counter)
        counter = event(external_ip, counter)
        counter = send_message(external_ip, counter, s)
        counter = recv_message(external_ip, counter, s)
        counter = event(external_ip, counter)
