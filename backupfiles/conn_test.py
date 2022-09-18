import mysql.connector as sql

def save():
    conn = sql.connect(host='localhost',user='root', passwd='admin', db='practical_progs')
    cur = conn.cursor()
    
    if conn.is_connected():
        print("established connection.")
    conn.close()

save()