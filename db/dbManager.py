import psycopg2

class DbManager:
    def __init__(self, host, port, database, user, password):
        """ Give the database connection parameters to the class """
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None  
    
    # Close the database connection if it exists      
    def closeConnection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None
    
    # Open connection to the database if it is not already open
    def openConnection(self):
        """Open the database connection if it is not already open."""
        if self.connection is None:
            try:
                self.connection = psycopg2.connect(
                    host=self.host,
                    port=self.port,
                    database=self.database,
                    user=self.user,
                    password=self.password
                )
            except Exception as e:
                print(f"Error connecting to the database: {e}")
                self.connection = None
    
    # Execute a query with optional parameters  
    def executeQuery(self, query, params=None):
        """Execute a query with optional parameters."""
        
        # Execute the query and return the result
        try:
            self.openConnection()                                   # Ensure the connection is open
            with self.connection.cursor() as cursor:                # Create a cursor to execute the query
                
                cursor.execute(query, params)                       # Execute the query with parameters if provided
                
                if (query.strip().lower().startswith("select")):                                          
                    result = cursor.fetchall()                      # Fetch all results from a SELECT query
                else:
                    self.connection.commit()                        # Commit the transaction for non-SELECT queries
                    result = cursor.rowcount                        # For non-SELECT queries, return the number of affected rows 
            return result

        except Exception as e:
            print(f"Error executing query: {e}")
            raise  # O usar logging

        finally:
            self.closeConnection()                                  # Ensure the connection is closed after execution
            
