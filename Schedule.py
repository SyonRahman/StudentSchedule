import mysql.connector


def get_database_connection():
   connection = mysql.connector.connect(user='syonr',
                                        password='232887372',
                                        host='10.8.37.226',
                                        database='syonr_db')
   return connection


def execute_statement(connection, statement, starting_index):
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

def get_student_schedule(teacher_id):
   statement = "CALL Get_Student_Schedule(" + str(teacher_id) + ")"
   return execute_statement(get_database_connection(), statement)

def student_operations(student_id, operation, schedule):
    if operation == "schedule":
        get_student_schedule(student_id)
    elif operation == "class_grade":
        class_statement = "CALL Get_Student_Schedule_With_Class_ID(" + str(student_id) + ")"
        execute_statement(get_database_connection(), class_statement)
        class_id = input("\nSelect which class you want grades from with the class_id\n")
        grade_statement = "CALL Get_Class_Grade(" + str(student_id) + "," + str(class_id) + ")"
        return execute_statement(get_database_connection(), grade_statement)

def teacher_operations(teacher_id, operation):
    if operation == "schedule":







#def get_student_grades(student_id):

#def teacher_operations(teacher_id, schedule):

logged_in = True
while logged_in == True:
    type = input("Welcome. Are you a \nStudent\nTeacher\nAdministrator\n")
    type.lower()
    if type == "student":
        student_id = input("What is your student id?\n")
        operation = input("Which operation do you want to perform. Select one"
                          "\nschedule\nclass_grade\noverall_grade")
        student_operations(student_id, operation)
    elif type == "teacher":
        teacher_id = input("What is your teacher id?")
        teacher_operations(teacher_id)



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