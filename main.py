# load library
import sqlite3
import os
from helper import sql
def database_intialize():
    connection = sqlite3.connect('database/weather.db')
    c = connection.cursor()
    connection.commit()
    connection.close()

print(sql.create_tambon())

