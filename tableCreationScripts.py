"""
file: checkin.py
author: Aaron Turetsky
github: https://github.com/AaronTuretsky
date:8/28/18
"""
import sqlite3
import sys


connection = sqlite3.connect(str(sys.argv[1]))

cursor = connection.cursor()

sql_createMachine = '''
USING testdb
CREATE TABLE machine (
ID int NOT NULL PRIMARY KEY,
MAC_address VARCHAR(255) NOT NULL,
IP_address VARCHAR(255) NOT NULL,
last_updated DATETIME,
CONSTRAINT fields_unique UNIQUE(MAC_address, IP_address),
FOREIGN KEY(ID) REFERENCES hardware(ID))
'''

sql_createHardware ='''
USING testdb
CREATE TABLE hardware (
ID int NOT NULL PRIMARY KEY,
card_type VARCHAR(30),
core_clock int,
mem_clock int,
cards_active int,
hashrate REAL);
'''

cursor.execute(sql_createMachine)
cursor.execute(sql_createHardware)
connection.commit()
cursor.close()

