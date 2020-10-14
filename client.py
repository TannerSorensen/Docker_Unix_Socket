#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time


def send(s):
    """send message on socket connection"""
    timestamp = time.time()
    msg = str(timestamp)
    s.sendall(bytes(msg, encoding="utf-8"))


if __name__ == "__main__":
    socket_addr = "/tmp/docker_socket.s"

    # initialize unix socket
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # connect to socket at address
    s.connect(socket_addr)

    # send messages over socket
    while True:
        send(s)
        time.sleep(0.1)
