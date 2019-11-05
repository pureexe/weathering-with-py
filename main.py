# load library
import sqlite3
import os
import csv
from helper import sql,dataset

def database_intialize():
    connection = sqlite3.connect(sql.PATH)
    c = connection.cursor()
    c.execute(sql.CREATE_PROVINCE)
    c.execute(sql.CREATE_DISTRICT)
    c.execute(sql.CREATE_TOWN)
    c.execute(sql.CREATE_STATION)
    c.execute(sql.CREATE_RAIN)
    connection.commit()
    connection.close()

def main():
    if(not os.path.isfile(sql.PATH)):
        database_intialize()
    

if __name__ == '__main__':
    #main()
    #town, district, province = dataset.get_thailand()
    rain, station = dataset.get_rain()
    print(rain[:10])