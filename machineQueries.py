"""
file: checkin.py
author: Aaron Turetsky
github: https://github.com/AaronTuretsky
date:8/28/18
"""
import sqlite3
from subprocess import call

def present(MAC_address,cursor):
    cursor.execute("""
        SELECT 
         count(*)
        FROM machine
        WHERE
         MAC_address =
        """ + MAC_address + ";" )

    if cursor.fetchall() == 0:
        return False
    return True

def newMachine(MAC_address,IP_address,cursor):
    cursor.execute("""
        SELECT 
         max(ID)
        FROM machine;
        """)

    newID = cursor.fetchall().pop() + 1

    cursor.execute("""
        INSERT INTO machine (
        newID,""" + MAC_address + "," + IP_address + """, GETDATE;);
        """)

    cursor.execute("""
        INSERT INTO machine (
        newID, NULL, NULL, NULL, NULL, NULL);
        """)

def machineUpdate(MAC_address,cursor):
    cursor.execute("""
        UPDATE machine
        SET last_updated = GETDATE;
        WHERE MAC_address = """ + MAC_address + ";")

    id = getID(MAC_address)
    data = str(call(["aticonfig –odgc –adapter=all"]))

    start = 0
    end = 0
    index = 0
    for c in data:
        if c == "-":
            start = index + 2
        if c == "\n":
            end = index - 1
            break
        index += 1
    card_type = data[start:end]

    lines = data.replace("\n" , " ").split(" ")
    core_clock = 0
    mem_clock = 0
    cards_active = 0
    hashrate = 0
    for text in lines:
        if text == "adapter":
            cards_active += 1
            if cards_active == 7:
                break



    cursor.execute("""
            UPDATE hardware 
            SET card_type = """ + card_type + """,
                cards_active = """ + cards_active + """
                hashrate= 0;
            WHERE ID = """ + id + ";")

def getID(MAC_address,cursor):
    cursor.execute("""
        SELECT ID
        FROM machine
        WHERE MAC_address = """ + MAC_address + ";")
    return cursor.fetchall().pop()