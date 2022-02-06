# Bank manager.py
# Import all libraries: mysql.connector, tkinter, pickle

import mysql.connector as dbcon
from tkinter import *
import pickle

# init database
dbsel = dbcon.connect(user="root", passwd="admin", host="localhost", database="bank")
dbcurse = dbsel.cursor(Buffered=True)

# create db or except
def Create():
    try:
        dbcurse.execute('Create table bankacc(ACCNO varchar(10),NAME varchar(20),MOBILE varchar(10),EMAIL varchar(20),ADDRESS varchar(20))')

#creating required tables
# mycursor.execute("create table if not exists bank_master(acno char(4) primary key,name varchar(30),city char(20),mobileno char(10),balance int(6))")
# mycursor.execute("create table if not exists banktrans(acno char (4),amount int(6),dot date,ttype char(1),foreign key (acno) references bank_master(acno))")
# mydb.commit()
