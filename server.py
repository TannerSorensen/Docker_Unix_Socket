#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import socket


def receive(conn):
    """receive and print messages from connection"""
    msg = bytes.decode(conn.recv(1024))
    if msg:
        print(msg)


if __name__ == "__main__":
    socket_addr = "/tmp/docker_socket.s"

    # initialize unix socket
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # bind socket address
    if os.path.exists(socket_addr):
        os.unlink(socket_addr)
    s.bind(socket_addr)

    # accept connection
    s.listen(2)
    conn, addr = s.accept()
    print("connection accepted")
    
    # receive messages and print to terminal
    while True:
        receive(conn)
