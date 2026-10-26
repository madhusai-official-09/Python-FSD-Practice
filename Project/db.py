import mysql.connector

def connect_db():
    conn = None
    
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Madhusai@99",
            database = "employee_task_tracker"
        )
        
        if conn.is_connected():
            return conn
        
    except mysql.connector.Error as err:
        print("Database connection error:", err)
        
        if conn is not None and conn.is_connected():
            conn.close()
            
    return None
