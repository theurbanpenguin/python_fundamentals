#!/usr/bin/env python3

import socket
import sys

def send_http_request(target_host, target_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    client.send(b"GET / HTTP/1.1\r\nHost: " + target_host.encode() + b"\r\n\r\n")

    response = client.recv(4096)

    print(response.decode("utf-8"))

    client.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <target_host> <target_port>")
    else:
        target_host = sys.argv[1]
        target_port = int(sys.argv[2])
        send_http_request(target_host, target_port)