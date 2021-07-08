import sqlite3

def create_table():
    conn = sqlite3.connect( "lite.db" )   #if db file does not already exist it is created here
    cur = conn.cursor()
    
    cur.execute( "CREATE TABLE IF NOT EXIST store (item TEXT, quantity INTEGER, price REAL)" )      #Will not rerun if already exists
    
    conn.commit()
    conn.close()

def insert( item, quantity, price ):
    conn = sqlite3.connect( "lite.db" )  
    cur = conn.cursor()
    
    # cur.execute( "INSERT INTO store VALUES ('Wine Glass', 8, 10.5)" )
    cur.execute( "INSERT INTO store VALUES ( ?, ?, ? )", ( item, quantity, price ) )
    
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect( "lite.db" )   
    cur = conn.cursor()
    
    cur.execute( "SELECT * FROM store" )    # select all from store
    rows = cur.fetchall()
    
    conn.close()
    return rows

def delete( item ):
    conn = sqlite3.connect( "lite.db" )  
    cur = conn.cursor()
    
    cur.execute( "DELETE FROM store WHERE item = ? ", ( item, ) )   # the , comma after item is required for sqlite
    
    conn.commit()
    conn.close()

def update( item, quantity, price ):
    conn = sqlite3.connect( "lite.db" )  
    cur = conn.cursor()
    
    cur.execute( "UPDATE store SET quantity = ?, price = ? WHERE item = ?  ", ( quantity, price, item ) )  
    
    conn.commit()
    conn.close()

# insert( "Wine Glass", 11, 6 )
# update( 11, 7, "Wine Glass" )
# delete( "Wine Glass" )

print( view() )




# sqlite3 for sqlite
# psycopg2 for postgress sql
# 1. connect to a database 
# 2. create a cursor object
# 3. write a sql query
# 4. commit changes to database
# 5. close database connection

