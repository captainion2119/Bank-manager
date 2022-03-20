import mysql.connector as sql
conn = sql.connect(host='localhost',user='root', passwd='admin', db='practical_progs')
cur = conn.cursor()

if conn.is_connected():
    print("connection successful!")

cursor = conn.cursor()
cursor.execute("Select * from loan_accounts")
result = cursor.fetchall()
for row in result:
    print(row)
print("query 1 success!")

query1 = 'update loan_accounts set start_date="2021-01-10" where accno="4"'
cursor.execute(query1)
conn.commit()
cursor.execute("Select * from loan_accounts")
result = cursor.fetchall()
for row in result:
    print(row)
print("query 2 success!")

query2 = 'delete from loan_accounts where cust_name="M.P.YADAV"'
cursor.execute(query2)
conn.commit()
cursor.execute("Select * from loan_accounts")
result = cursor.fetchall()
for row in result:
    print(row)
print("query 3 success!")

cursor.execute('insert into loan_accounts values(4,"M.P.YADAV",800000,60,10.00,"2008-12-06")')
conn.commit()
cursor.execute("Select * from loan_accounts")
result = cursor.fetchall()
for row in result:
    print(row)
print("query 4 success!")

cursor.execute('select * from loan_accounts where not Int_rate="Null"')
result = cursor.fetchall()
for row in result:
    print(row)
print("query 5 success!")

cursor.execute('select * from loan_accounts where int_rate is NULL')
result = cursor.fetchall()
for row in result:
    print(row)
print("query 6 success!")

