"""
file: checkin.py
author: Aaron Turetsky
github: https://github.com/AaronTuretsky
date:8/28/18
"""
import sqlite3
import sys

connection = sqlite3.connect(sys.argv[1])
cursor = connection.cursor()

sql_createMachine = ""
sql_createMachine += "CREATE TABLE machine ("
sql_createMachine += "ID int NOT NULL PRIMARY KEY,"
sql_createMachine += "MAC_address VARCHAR(255) NOT NULL,"
sql_createMachine += "IP_address VARCHAR(255) NOT NULL,"
sql_createMachine += "last_updated DATETIME,"
sql_createMachine += "CONSTRAINT fields_unique (MAC_address, IP_address),"
sql_createMachine += "FOREIGN KEY(ID) REFERENCES hardware(ID));"


sql_createHardware = """
CREATE TABLE hardware (
ID int NOT NULL PRIMARY KEY,
card_type VARCHAR(30),
core_clock int,
mem_clock int,
cards_active int,
hashrate REAL);
"""

cursor.execute(sql_createMachine)
cursor.execute(sql_createHardware)

cursor.close()