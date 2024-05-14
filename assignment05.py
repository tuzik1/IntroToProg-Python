# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: Advanced collections and error handling.
# Change Log: (Who, When, What)
#   Nicholas Smith, 5/13/2024, Created File
# ------------------------------------------------------------------------------------------ #

from sys import exit

import csv

FILE_NAME: str = "Enrollments.csv"

student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
file = None
menu_choice: str = ""
student_data: dict = {}
students: list = []

# Function for loading data with error handling for missing file.
try:
    with open(FILE_NAME, "r") as file:
        column_names = ("student_first_name","student_last_name","course_name")
        all_rows = csv.DictReader(file, fieldnames=column_names)
        for row in all_rows:
           students.append(row)
    print("\nINFO: all rows loaded from database file.")
except FileNotFoundError as e:
    print("ERROR: File not found.")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error.\n")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')


# if the file doesn't exist it will create it, otherwise it overwrites it.
def add_student():
    try:
        student_first_name = input("Enter the user's first name: ")
        if not student_first_name.isalpha():
            raise ValueError("The first name should not contain numbers.")
    
        student_last_name = input("enter the user's last name: ")
        if not student_last_name.isalpha():
            raise ValueError("The last name should not contain numbers.")
       
        course_name = input("Enter the course name: ")
        student_data = {
            "student_first_name": student_first_name,
            "student_last_name": student_last_name,
            "course_name": course_name
        }
        students.append(student_data)
        print("\nINFO: New user added.")

    except ValueError as e:
        print(e)  # Prints the custom message
        print("-- Technical Error Message -- ")
        print(e.__doc__)
        print(e.__str__())
    except Exception as e:
        print("There was a non-specific error!\n")
        print("-- Technical Error Message -- ")
        print(e, e.__doc__, type(e), sep='\n')


def current_data():
    print("\n")
    for row in students:
         print(f"{row["student_first_name"]},{row["student_last_name"]},{row["course_name"]}")


def save_to_file():
    try:
        column_names = ("student_first_name","student_last_name","course_name")
        with open(FILE_NAME, "w") as file:
            writer = csv.DictWriter(file, fieldnames=column_names, lineterminator="\n")
            for row in students:
                writer.writerow(row)
        print("INFO: All rows saved to database.")
        file.close()
        print(f"Added {students} to {FILE_NAME}")
    
    except Exception as e:
        print("-- Technical Error Message -- ")
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')
    
    finally:
        if file.closed == False:
            file.close()
    

def quit_program():
    print("Quitting program...")
    exit()


if __name__ == "__main__":
     MENU: str = """
        ---- Course Registration Program ----
        Select from the following menu:  
        1. Register a Student for a Course
        2. Show current data  
        3. Save data to a file
        4. Exit the program
        ----------------------------------------- 
        """
     
     while True:
        print(MENU)
        menu_choice = input("What would you like to do? ")

        match menu_choice:
            case "1":
                add_student()
            case "2":
                current_data()
            case "3":
                save_to_file()
            case "4":
                quit_program()
            case _:
                print("ERROR: Please select a valid option")