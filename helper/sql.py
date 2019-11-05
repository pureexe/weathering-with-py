PATH = './database/weather.db'
CREATE_TOWN =  """
    CREATE TABLE town (
        id integer primary key,
        district integer,
        thai text,
        english text,
        latitude real,
        longtitude real
    )
    """

CREATE_DISTRICT = """
    CREATE TABLE city (
        id integer primary key,
        province integer,
        thai text,
        english text
    )
    """

CREATE_PROVINCE = """
    CREATE TABLE province (
        id integer primary key,
        thai text,
        english text
    )
"""

CREATE_STATION = """
    CREATE TABLE station (
        id integer primary key,
        town integer,
        address text,
        latitude real,
        longtitude real
    )
"""

CREATE_RAIN = """
    CREATE TABLE rain (
        station integer,
        time datetime,
        fall real
    )
"""