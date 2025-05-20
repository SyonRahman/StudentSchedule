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

   return results



def get_student_schedule(student_id):
   statement = "CALL Get_Student_Schedule(" + str(student_id) + ")"
   return execute_statement(get_database_connection(), statement)

def student_operations(student_id, operation, schedule):
    if operation == "schedule":
        get_student_schedule(student_id)
    if operation == "class_grade":




#def get_student_grades(student_id):

#def teacher_operations(teacher_id, schedule):

logged_in = True
while logged_in == True:
    type = input("Welcome. Are you a \nStudent\nTeacher\nAdministrator\n")
    type.lower()
    if type == "student":
        student_id = input("What is your student id?")
        student_operations(student_id)
        operation = input("Which operation do you want to perform. Select one"
                          "\nschedule\nclass_grade\noverall_grade")
    elif type == "teacher":



# student_id = input("Enter Student ID: ")
# outputs = get_student_schedule(student_id)
#
#
# for result in outputs:
#    print("Period: " + str(result[0]))
#    print("Course: " + str(result[1]))
#    print("Room: " + str(result[2]))
#    print("Teacher: " + str(result[3]))
#    print()