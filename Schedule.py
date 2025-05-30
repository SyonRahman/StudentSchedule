import math

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
   student_schedule = execute_statement(get_database_connection(), statement)
   for period in student_schedule:
       print("Class ID: " + str(period[0]))
       print("Period: " + str(period[1]))
       print("Course Name: " + str(period[2]))
       print("Room Number: " + str(period[3]))
       print("Name: " + str(period[4]))
       print()
   return student_schedule

def get_teacher_schedule(teacher_id):
   statement = "CALL Get_Teacher_Schedule(" + str(teacher_id) + ")"
   teacher_schedule = execute_statement(get_database_connection(), statement)
   for period in teacher_schedule:
       print("Class ID: " + str(period[0]))
       print("Period: " + str(period[1]))
       print("Course Name: " + str(period[2]))
       print("Room Number: " + str(period[3]))
       print("Name: " + str(period[4]))
       print()
   return teacher_schedule

def student_operations(student_id, operation):
    if operation == "1":
        get_student_schedule(student_id)
    elif operation == "2":
        get_student_schedule(student_id)
        class_id = input("Select which class you want grades from with the class_id\n")
        grade_statement = "CALL Get_Class_Grade(" + str(student_id) + "," + str(class_id) + ")"
        class_grades = execute_statement(get_database_connection(), grade_statement)
        for row in class_grades:
            print("Assignment ID: " + str(row[1]))
            print("Assignment Grade: " + str(row[2]))
            print()
    elif operation == "3":
        print("So you want to check your total average for all classes. Here are the ways that your grade works")
        print("Minor Assignments are 30% of your grade."
              "\nMajor Assignments are 70% of your grade."
              "\nIf you course is an AP you get a 10% overall boost.\n")
        overall_grades = "CAll Get_All_Assignments(" + str(student_id) + ")"
        total_grade = get_grades(execute_statement(get_database_connection(), overall_grades))
        print("Your overall grade rounded up for all courses is " + str(total_grade))



def get_grades(assignments):
    minor_grades = []
    major_grades = []
    minor_grade = 0
    major_grade = 0
    for assignment in assignments:
        if assignment[3] == "minor":
            assignment_grade = assignment[2]
            if assignment[1] == "AP":
                assignment_grade *= 1.1
            minor_grade += assignment_grade
            minor_grades.append(assignment)
        elif assignment[3] == "major":
            assignment_grade = assignment[2]
            if assignment[1] == "AP":
                assignment_grade *= 1.1
            major_grade += assignment_grade
            major_grades.append(assignment)
    minor_grade *= 0.3
    minor_grade /= len(minor_grades)
    major_grade *= 0.7
    major_grade /= len(major_grades)
    overall_grade = major_grade + minor_grade
    return math.ceil(overall_grade)



def teacher_operations(teacher_id, operation):
    if operation == "1":
        get_teacher_schedule(teacher_id)
    elif operation == "2":
        get_teacher_schedule(teacher_id)
        class_id = input("Select which class ID you want to see assignment grades from!\n")
        print("Here are a list of Assignment IDS from the class.")
        assignment_query = "CALL Get_Assignment_IDS(" + str(class_id) + ")"
        assignment_ids = execute_statement(get_database_connection(), assignment_query)
        for assignment_id in assignment_ids:
            print("Assignment ID: " + str(assignment_id[0]))
            print()
        assignment_id = input("Select which assignment ID you want to see the student grades from\n")
        grade_statement = "CALL Get_Student_Grades(" + str(class_id) + "," + str(assignment_id) + ")"
        student_grades = execute_statement(get_database_connection(), grade_statement)
        for row in student_grades:
            print("Student ID: " + str(row[0]))
            print("Grade: " + str(row[1]))
            print()
        return student_grades





logged_in = True
while logged_in == True:
    type = input("\nWelcome. Are you a \n1. Student"
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
        print("Here are all valid teacher ids.")
        teacher_valid = "SELECT teacher_id FROM TeacherSchedule WHERE classid_1 IS NOT NULL OR classid_6 IS NOT NULL;"
        teacher_ids = execute_statement(get_database_connection(), teacher_valid)
        valid_teacher_ids = []
        for id in teacher_ids:
            print("Valid Teacher ID: " + str(id[0]))
            valid_teacher_ids.append(str(id[0]))
            print()
        teacher_id = input("What is your teacher id?\n")
        if teacher_id in valid_teacher_ids:
            operation = input("Which operation do you want to perform? Select the number that corresponds with the operation"
                              "\n1. Schedule"
                              "\n2. Check All Student Grades\n")
            teacher_operations(teacher_id, operation)
        else:
            print("Teacher ID is not a valid ID.")


