from datetime import datetime
from multiprocessing import connection
import sqlite3

# Function to insert records in sql table
def insert_data(stock_name, trade_type, premium_amount, trade_date):
    connection = sqlite3.connect("stock.db")
    cursor = connection.cursor()
    #cursor.execute('''INSERT INTO stock (stock_name, trade_type, premium_amount, trade_date) VALUES ( 'TSLA', 'CALL',1000,'2022-06-02 10:00:00')''')   
    insert = f'''INSERT INTO stocks (stock_name, trade_type, premium_amount, trade_date) VALUES ('{stock_name}', '{trade_type}', '{premium_amount}', '{trade_date}')'''
    cursor.execute(insert)   
    connection.commit()
    print("Records have been saved")
    #cursor.execute("SELECT * FROM stock")
    #return cursor.fetchall()


# Function to get stock trading data
def get_data(month):
    connection = sqlite3.connect("stock.db")
    cursor = connection.cursor()
    #cursor.execute("SELECT * FROM stock")
    #cursor.execute("select * from stock where trade_date < date('now','-0 days')")
    cursor.execute(f"SELECT * FROM stocks WHERE strftime('%m', trade_date) = '{month}'")
    return cursor.fetchall()


# Choose month to see records
data = get_data('07')
print(data, len(data))
total = 0
for i in data:
    print(i[2])
    total += i[2]
print("Total:", total)

# Uncomment this line if u like to insert data
#insert_data('TSLA','CALL',1055,'2022-07-01 11:00:00')
