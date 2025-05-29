import psycopg2

# Connects the application to the postgres database
def connect_to_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="i.SERGIO.2025.0",
            user="postgres",
            port = "5433"
        )
        #return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        #return None
    
    cur = connection.cursor()
    cur.execute("SELECT version();")
    print("Database version:", cur.fetchone()[0])
    cur.close()
    connection.close()
    