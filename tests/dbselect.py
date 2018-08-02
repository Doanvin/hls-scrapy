import psycopg2

hostname = 'localhost'
username = '' # your username 
password = '' # your password
database = '' # your database

def queryQuotes( conn ) :
    cur = conn.cursor()
    cur.execute( """select * from reports""" )
    rows = cur.fetchall()

    for row in rows :
        print (row[1], row[2], row[3], row[4])

conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
queryQuotes( conn )
conn.close()