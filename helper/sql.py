def create_tambon():
    return """
    CREATE TABLE rain (
        id integer primary key,
        city integer,
        thai text,
        english text,
        latitude real,
        longtitude real
    )
    """
def create_city():
    return """
    CREATE TABLE rain (
        id integer primary key,
        city integer,
        thai text,
        english text,
        latitude real,
        longtitude real
    )
    """