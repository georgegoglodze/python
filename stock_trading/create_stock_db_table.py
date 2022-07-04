import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('stock.db')
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

sql ='''CREATE TABLE stocks(
   stock_name CHAR(20) NOT NULL,
   trade_type CHAR(20) NOT NULL,
   premium_amount INT NOT NULL,
   trade_date DATE NOT NULL
   
)'''

cursor.execute(sql)
conn.commit()
