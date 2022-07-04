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
