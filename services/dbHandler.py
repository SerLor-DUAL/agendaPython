import psycopg2

class DBHandler:
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
            

#---------------------#
#   CRUD for Event    #
#---------------------#

    # Function to create a new event for a user in the database
    def createEvent(self, event):
        
        # Prepare the insert query
        insertQuery = """ INSERT INTO EVENTS_NEV (nev_title, nev_description, nev_startTime, nev_endTime)
                          VALUES (%s, %s, %s, %s) RETURNING nev_id """
        params = (self.title, self.description, self.startTime, self.endTime)
        
        # Execute the query and get the new event ID
        newEventId = dbHandler.executeQuery(insertQuery, params)
        self.id = newEventId[0][0]

#---------------------------------------------------------------------------------------------------------------------#

    # Function to read an event's details from the database
    def readEvent(self):

        # Check if the database handler is provided
        if dbHandler is None:
            raise ValueError("Database handler is required to read an event.")
        
        # Prepare the select query
        selectQuery = """ SELECT nev_id, nev_title, nev_description, nev_startTime, nev_endTime
                            FROM EVENTS_NEV 
                           WHERE nev_id = %s """
        params = self.id
        
        result = dbHandler.executeQuery(selectQuery, params)
        
        # If no result is found, raise an error
        if not result:
            raise ValueError("Event not found.")
        
        # Update the event's attributes with the retrieved data
        self.id, self.title, self.description, self.startTime, self.endTime = result[0]

#---------------------------------------------------------------------------------------------------------------------#

    # Function to edit an event's details in the database
    def updateEvent(self, dbHandler, title = None, description = None, start_time = None, end_time = None):
        
        #  Checks if parameters are provided and if they are valid
        if dbHandler is None:
            raise ValueError("Database handler is required to edit the event.")
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        
        # Prepare the update query and parameters
        updateQuery = """ UPDATE EVENTS_NEV
                             SET nev_title = %s, nev_description = %s, nev_startTime = %s, nev_endTime = %s
                           WHERE nev_id = %s """
        
        # Prepare the parameters
        params = (self.title, self.description, self.start_time, self.end_time, self.id)
        
        # Execute the query
        dbHandler.executeQuery(updateQuery, params)

#---------------------------------------------------------------------------------------------------------------------#

    # Function to delete an event from the database
    def deleteEvent(self, dbHandler):
        
        # Check if the database handler is provided
        if dbHandler is None:
            raise ValueError("Database handler is required to delete an event.")
        
        # Prepare the delete query
        deleteQuery = """ DELETE FROM EVENTS_NEV WHERE nev_id = %s """
        
        # Prepare the parameters
        params = (self.id)
        
        # Execute the query with the event ID
        dbHandler.executeQuery(deleteQuery, params)