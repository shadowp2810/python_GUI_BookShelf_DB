import psycopg2


def create_table():
    conn = psycopg2.connect( " dbname= 'database1' user= 'postgres' password= '<PASSWORD>' host= 'localhost' port= '5432' " )   #if db file does not already exist it is created here
    cur = conn.cursor()
    
    cur.execute( "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)" )      #Will not rerun if already exists
    
    conn.commit()
    conn.close()

def insert( item, quantity, price ):
    conn = psycopg2.connect( " dbname= 'database1' user= 'postgres' password= '<PASSWORD>' host= 'localhost' port= '5432' " )  
    cur = conn.cursor()
    
    # cur.execute( "INSERT INTO store VALUES ( ?, ?, ? )", ( item, quantity, price ) ) for sqlite
    # cur.execute( "INSERT INTO store VALUES ( '%s', '%s', '%s' )" % ( item, quantity, price ) )        is prone to SQL injections
    cur.execute( "INSERT INTO store VALUES ( %s, %s, %s )", ( item, quantity, price ) ) 

    
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect( " dbname= 'database1' user= 'postgres' password= '<PASSWORD>' host= 'localhost' port= '5432' " )  
    cur = conn.cursor()
    
    cur.execute( "SELECT * FROM store" )    # select all from store
    rows = cur.fetchall()
    
    conn.close()
    return rows

def delete( item ):
    conn = psycopg2.connect( " dbname= 'database1' user= 'postgres' password= '<PASSWORD>' host= 'localhost' port= '5432' " )  
    cur = conn.cursor()
    
    cur.execute( "DELETE FROM store WHERE item = %s ", ( item, ) )   # the , comma after item is required for sqlite
    
    conn.commit()
    conn.close()

def update( item, quantity, price ):
    conn = psycopg2.connect( " dbname= 'database1' user= 'postgres' password= '<PASSWORD>' host= 'localhost' port= '5432' " )   
    cur = conn.cursor()
    
    cur.execute( "UPDATE store SET quantity = %s, price = %s WHERE item = %s  ", ( quantity, price, item ) )  
    
    conn.commit()
    conn.close()

# insert( "Wine Glass", 11, 6 )
# update( 11, 7, "Wine Glass" )
# delete( "Wine Glass" )
create_table()
# insert("Apple", 11, 13)
# insert("Orange", 10, 15)
# insert("Kiwi", 11, 19)
# delete( "Apple" )
update("Apple", 17, 23)



print( view() )




# psycopg2 for sqlite
# psycopg2 for postgress sql
# 1. connect to a database 
# 2. create a cursor object
# 3. write a sql query
# 4. commit changes to database
# 5. close database connection

