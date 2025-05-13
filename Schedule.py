import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(user='syonr',
                                         password='232887372',
                                         host='10.8.37.226',
                                         database='syonr_db')
    return connection

def execute_statement(connection, statement):
    cursor = connection.cursor()
    cursor.execute(statement)
    results = []

    for row in cursor:
        results.append(row)

    cursor.close()
    connection.close()

def get_student_schedule(student_id):
    statement = "CALL Get_Student_Schedule(" + student_id + ")"
    return execute_statement(get_database_connection(), statement)

student_id = input("Enter Student ID: ")
output = get_student_schedule(student_id)

for result in output:

