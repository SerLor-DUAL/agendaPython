import psycopg2

# Connects the application to the postgres database
def connect_to_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            port = "5433",
            database="i.SERGIO.2025.0",
            user="sergio",
            password="sergio"
        )
        #return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        #return None
    
    cur = connection.cursor()
    cur.execute('SELECT doh_id FROM "DOCHEADER_DOH" LIMIT 1;')
    print("ID:", cur.fetchone()[0])
    cur.close()
    connection.close()
    
connect_to_db()