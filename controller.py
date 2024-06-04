from mysql.connector import connect, Error

connection = None

try:
    connection = connect(
        host="localhost",
        user="root",
        password="",
        database="schedule_db",
        port="3306"
    )
    
    cursor = connection.cursor()
    print("Connected to the database!")

    #Login

    def checkUser(username, password=None):
        cmd = f"Select count(username) from users_account where username='{username}' and BINARY password='{password}'"
        cursor.execute(cmd)
        cmd = None
        a = cursor.fetchone()[0] >= 1
        return a
    
    # Add cleaners
    def add_cleaners(group_leader, members, schedule_day, cleaning):
        try:
            query = "INSERT INTO cleaners (group_leader, members, schedule_day, cleaning) VALUES (%s, %s, %s, %s)"
            values = (group_leader, members, schedule_day, cleaning)
            cursor.execute(query, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
    def get_cleaners():
        try:
            cmd = "SELECT cleaners_id, group_leader, members, schedule_day, cleaning FROM cleaners;"
            cursor.execute(cmd)

            # Fetch the results
            result = cursor.fetchall()
            print("data: ", result)

            # Return the results
            return result
            
        except Exception as e:
            print(f"Error: {e}")
            return []  # Return an empty list if there's an error or no results
     # update cleaners
    def update_cleaners(cleaners_id, group_leader, members, schedule_day, cleaning):
        cmd = f"update cleaners set group_leader ='{group_leader}',members='{members}', schedule_day ='{schedule_day}', cleaning ='{cleaning}' where cleaners_id = '{cleaners_id}';"
        cursor.execute(cmd)
        connection.commit()
        if cursor.rowcount == 0:
            return False
        return True

        # Delete a activity
    def delete_cleaners(cleaners_id):
        cmd = f"delete from cleaners where cleaners_id='{cleaners_id}';"
        cursor.execute(cmd)
        connection.commit() 
        if cursor.rowcount == 0:
            return False
        return True
    # Search cleaners
    def search_cleaners(query):
        try:
            cmd = f"SELECT cleaners_id, group_leader, members, schedule_day, cleaning FROM cleaners WHERE LOWER(group_leader) LIKE LOWER('%{query}%') OR LOWER(schedule_day) LIKE LOWER('%{query}%')"
            cursor.execute(cmd)

            # Fetch the results
            result = cursor.fetchall()
            print("data: ", result)

            # Return the results
            return result

        except Exception as e:
            print(f"Error: {e}")
            return []  # Return an empty list if there's an error or no results
   
    def get_group_leader(schedule_day):
        try:
            cursor.execute("SELECT group_leader FROM cleaners WHERE schedule_day = %s", (schedule_day,))
            names = [row[0] for row in cursor.fetchall()]
            return names
        except Error as e:
            print(f"Error: {e}")
            return []


    def get_day_cleaners(schedule_day):
        try:
            query = """
            SELECT COUNT(*) 
            FROM cleaners 
            WHERE schedule_day = %s AND group_leader IS NOT NULL
            """
            cursor.execute(query, (schedule_day,))
            count = cursor.fetchone()[0]
            return count
        except Error as e:
            print(f"Error: {e}")
            return 0


      
except Error as e:
    print(f"Error: {e}")