#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *

HOST='46.244.106.52'
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)


tcpCLiSock=socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data=raw_input('>')
    if not data:
        break
    tcpCliSock.send(data)
    data=tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print data

tcpCliSock.close()

