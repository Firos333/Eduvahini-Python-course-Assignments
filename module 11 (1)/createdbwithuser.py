
#am using postgres as db SYSTEM BECAUSE I could'nt install MYSQL in my pc (some dll issue related to current OS windows 8.1-)
#connect to postgres sql as user postgres and create anew user called firos and then alter user previleges
#then create DB pet_store .. this db now can be used in django


import psycopg2

conn = psycopg2.connect(
    dbname="postgres", user="postgres", password="3442", host="127.0.0.1", port= '5432'
)

conn.autocommit = True
cur = conn.cursor()

DATA_PROD_USER_PWD = "changeme"
DATA_VIEW_USER_PWD = "changeme"

cur.execute(f"""
CREATE USER firos WITH PASSWORD '1234';
ALTER USER firos CREATEDB;
""")

cur.execute("CREATE DATABASE pet_store OWNER firos")

conn.commit()
conn.close()