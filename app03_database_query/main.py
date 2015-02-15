##encoding=UTF-8

import sqlite3
import bottle
import random
import datetime
def random_str():
    choice = list("abcdefghijklmnopqrstuvwxyz0123456789")
    return "".join([random.choice(choice) for i in range(10)])

connect = sqlite3.connect(":memory:")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE test (
    integer_type INTEGER,
    real_type REAL,
    text_type TEXT,
    date_type DATE,
    datetime_type DATETIME
    )""")


records = [(random.randint(1, 1000), 
            random.random(),
            random_str(),
            datetime.date(random.randint(1900, 2015), random.randint(1, 12), 1),
            datetime.datetime(random.randint(1900, 2015), random.randint(1, 12), 15, random.randint(0,23))
            ) for i in range(1000)]

cursor.executemany("INSERT INTO test VALUES (?,?,?,?,?);", records)

@bottle.route("/")
def index():
    integer_lowerbound = 0
    integer_upperbound = 1000
    real_lowerbound = 0.0
    real_upperbound = 999.9
    text_pattern = ""
    date_lowerbound = "1900-01-01"
    date_upperbound = "2020-01-01"
    datetime_lowerbound = "1900-01-01 00:00:00"
    datetime_upperbound = "2020-01-01 00:00:00"
    return bottle.template("index.tpl", {"integer_lowerbound": integer_lowerbound,
                                         "integer_upperbound": integer_upperbound,
                                         "real_lowerbound": real_lowerbound,
                                         "real_upperbound": real_upperbound,
                                         "text_pattern": text_pattern,
                                         "date_lowerbound": date_lowerbound,
                                         "date_upperbound": date_upperbound,
                                         "datetime_lowerbound": datetime_lowerbound,
                                         "datetime_upperbound": datetime_upperbound,})

@bottle.post("/")
def index_clear_all_box():
    integer_lowerbound = ""
    integer_upperbound = ""
    real_lowerbound = ""
    real_upperbound = ""
    text_pattern = ""
    date_lowerbound = ""
    date_upperbound = ""
    datetime_lowerbound = ""
    datetime_upperbound = ""
    
    return bottle.template("index.tpl", {"integer_lowerbound": integer_lowerbound,
                                         "integer_upperbound": integer_upperbound,
                                         "real_lowerbound": real_lowerbound,
                                         "real_upperbound": real_upperbound,
                                         "text_pattern": text_pattern,
                                         "date_lowerbound": date_lowerbound,
                                         "date_upperbound": date_upperbound,
                                         "datetime_lowerbound": datetime_lowerbound,
                                         "datetime_upperbound": datetime_upperbound,})

@bottle.post("/result")
def result():
    integer_lowerbound = bottle.request.forms.get("integer_lowerbound")
    integer_upperbound = bottle.request.forms.get("integer_upperbound")
    real_lowerbound = bottle.request.forms.get("real_lowerbound")
    real_upperbound = bottle.request.forms.get("real_upperbound")
    text_pattern = bottle.request.forms.get("text_pattern")
    date_lowerbound = bottle.request.forms.get("date_lowerbound")
    date_upperbound = bottle.request.forms.get("date_upperbound")
    datetime_lowerbound = bottle.request.forms.get("datetime_lowerbound")
    datetime_upperbound = bottle.request.forms.get("datetime_upperbound")

    
    if integer_lowerbound:
        integer_lowerbound = "integer_type >= %s" % integer_lowerbound
    if integer_upperbound:
        integer_upperbound = "integer_type <= %s" % integer_upperbound
    if real_lowerbound:
        real_lowerbound = "real_type >= %s" % real_lowerbound
    if real_upperbound:
        real_upperbound = "real_type <= %s" % real_upperbound
    if text_pattern:
        text_pattern = "text_type LIKE '%{}%'".format(text_pattern)
    if date_lowerbound:
        date_lowerbound = "date_type >= '%s'" % date_lowerbound
    if date_upperbound:
        date_upperbound = "date_type <= '%s'" % date_upperbound
    if datetime_lowerbound:
        datetime_lowerbound = "datetime_type >= '%s'" % datetime_lowerbound
    if datetime_upperbound:
        datetime_upperbound = "datetime_type <= '%s'" % datetime_upperbound
    where_clause = " AND ".join([i for i in [integer_lowerbound,
                                             integer_upperbound,
                                             real_lowerbound,
                                             real_upperbound,
                                             text_pattern,
                                             date_lowerbound,
                                             date_upperbound,
                                             datetime_lowerbound,
                                             datetime_upperbound,] if i])
    sqlcmd = "SELECT * FROM test WHERE %s" % where_clause
    records = cursor.execute(sqlcmd).fetchall()
        
    return bottle.template("result.tpl", {"records": records})

if __name__ == "__main__":
    bottle.run(host='localhost', port=7777, debug=True)