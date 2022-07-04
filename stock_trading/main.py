from datetime import datetime
from insert_data import insert_data
from get_monthly_data import get_monthly_data
from multiprocessing import connection
import sqlite3


# Choose month to see records
data = get_monthly_data('06')
print(data, len(data))
total = 0
for i in data:
    print(i[2])
    total += i[2]
print("Total:", total)

# Uncomment this line if u like to run the  'insert data' function
#insert_data('TSLA','CALL',1055,'2022-07-01 11:00:00')
