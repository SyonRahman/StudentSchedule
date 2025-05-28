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

def get_teacher_schedule(teacher_id):
   statement = "CALL Get_Teacher_Schedule(" + str(teacher_id) + ")"
   return execute_statement(get_database_connection(), statement)

def student_operations(student_id, operation):
    if operation == "1":
        get_student_schedule(student_id)
    elif operation == "2":
        get_student_schedule(student_id)
        class_id = input("Select which class you want grades from with the class_id\n")
        grade_statement = "CALL Get_Class_Grade(" + str(student_id) + "," + str(class_id) + ")"
        return execute_statement(get_database_connection(), grade_statement)
    elif operation == "3":
        print("So you want to check your total average for all classes. Here are the ways that your grade works")
        print("Minor Assignments are 30% of your grade."
              "\nMajor Assignments are 70% of your grade."
              "\nIf you course is an AP you get a 10% overall boost.")
        overall_grades = "CAll Get_All_Assignments(" + str(student_id) + ")"
        total_grade = get_grades(execute_statement(get_database_connection(), overall_grades))
        print("Your overall grade for all courses is " + str(total_grade))



def get_grades(assignments):
    overall_grade = 0
    for assignment in assignments:
        if assignment[3] == "minor":
            assignment_grade = 0.3 * assignment[2]
            if assignment[1] == "AP":
                assignment_grade *= 1.1
            overall_grade += assignment_grade
        elif assignment[3] == "major":
            assignment_grade = 0.7 * assignment[2]
            if assignment[1] == "AP":
                assignment_grade *= 1.1
        overall_grade += assignment_grade
    number_of_assignments = len(assignments)
    return overall_grade / number_of_assignments



def teacher_operations(teacher_id, operation):
    if operation == "1":
        get_teacher_schedule(teacher_id)
    elif operation == "2":
        get_teacher_schedule(teacher_id)
        class_id = input("Select which class you want to see assignment grades from!\n")
        assignment_id = input("Select which assignment you want to see the student grades from")
        grade_statement = "CALL Get_Student_Grades(" + str(class_id) + "," + str(assignment_id) + ")"
        return execute_statement(get_database_connection(), grade_statement)





logged_in = True
while logged_in == True:
    type = input("Welcome. Are you a \n1. Student"
                 "\n2. Teacher"
                 "\n3. Administrator\nEnter the Number that corresponds\n")
    if type == "1":
        student_id = input("What is your student id?\n")
        operation = input("Which operation do you want to perform? Select the number that corresponds with the operation"
                          "\n1. Schedule"
                          "\n2. Class Grade"
                          "\n3. Overall Grade\n")
        student_operations(student_id, operation)
    elif type == "2":
        teacher_id = input("What is your teacher id?")
        operation = input("Which operation do you want to perform? Select the number that corresponds with the operation"
                          "\n1. Schedule"
                          "\n2. Check All Student Grades\n")
        teacher_operations(teacher_id, operation)



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