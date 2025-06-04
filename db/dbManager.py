import psycopg2
import os

from dotenv import load_dotenv
class DbManager:
    def __init__(self, host = None, port = None, database = None, user = None, password = None):
        
        # Load environment variables from .env file
        load_dotenv()
    
        hostEnv = os.getenv("DB_HOST", "localhost")     # Default to localhost if not set
        portEnv = int(os.getenv("DB_PORT", "5432"))     # Default PostgreSQL port is 5432
        databaseEnv = os.getenv("DB_NAME", "")          # Default to empty string if not set
        userEnv = os.getenv("DB_USER", "")              # Default to empty string if not set
        passwordEnv = os.getenv("DB_PASSWORD", "")      # Default to empty string if not set
        
        self.host = host or hostEnv
        self.port = port or int(portEnv)
        self.database = database or databaseEnv
        self.user = user or userEnv
        self.password = password or passwordEnv
        self.connection = None
        
        # Validate connection parameters
        if not all([self.host, self.port, self.database, self.user, self.password]):
            raise ValueError("Faltan datos de conexión a la base de datos.")
    
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
            
