import sqlite3


# Function to get stock trading data
def get_monthly_data(month):
    connection = sqlite3.connect("stock.db")
    cursor = connection.cursor()
    #cursor.execute("SELECT * FROM stock")
    #cursor.execute("select * from stock where trade_date < date('now','-0 days')")
    cursor.execute(f"SELECT * FROM stocks WHERE strftime('%m', trade_date) = '{month}'")
    return cursor.fetchall()
