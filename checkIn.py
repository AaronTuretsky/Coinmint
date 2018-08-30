"""
file: checkin.py
author: Aaron Turetsky
github: https://github.com/AaronTuretsky
date:8/28/18
"""
import sqlite3
import machineQueries
import socket
import sys
from uuid import getnode as get_mac

def main():
    print("running")
    connection = sqlite3.connect(str(sys.argv[1]))
    cursor = connection.cursor()
    print("connection opened")
    MAC_address = str(get_mac())
    hostname = socket.gethostname()
    IP_address = socket.gethostbyname(hostname)

    if not machineQueries.present(MAC_address,cursor):
        machineQueries.newMachine(MAC_address, IP_address,cursor)
    machineQueries.machineUpdate(MAC_address,cursor)
    cursor.commit()
    cursor.close()
    print("finished")
main()