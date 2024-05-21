# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Ryan Seng, 5/19/2024, Assignment06
# ------------------------------------------------------------------------------------------ #

# Importing JSON library to get json functions
import json

# This is the MENU users will be selecting from
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------
"""

# This are the other constants
FILE_NAME: str = "Enrollments.json"

# These are the variables
menu_choice: str = ""
students: list = []

class FileProcessor:
    """
    This function reads data in from the file in file_name and puts it into a list
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            with open(file_name, 'r') as file:
                student_data = json.load(file)
                print("File loaded")
        except FileNotFoundError as e:
            IO.output_error_messages("The text/json file could not be found when running this script", e)
        except ValueError as e:
            IO.output_error_messages("There are corruption issues in the file", e)
        except Exception as e:
            IO.output_error_messages("Unknown error.", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    """
    This function takes a file name and a list of student data and writes the student data into a file named in file_name
    """
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "w")
            for student in student_data:
                file.write(f"{student["First_Name"]},{student["Last_Name"]},{student["Course"]}\n")
            print(f"The following list was saved in {FILE_NAME}:")
            file.close()
        except TypeError as e:
            IO.output_error_messages("The data may not be in a valid format", e)
        except Exception as e:
            IO.output_error_messages("Unknown error.", e)
        finally:
            if file.closed == False:
                file.close()


class IO:
    """
    This function prints error messages out in a way that should be legible and understandable to 
    anyone working on this script.

    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(message)
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep='\n')

    """
    This function prints out a set of text that usually should be a menu that gives users an idea 
    of what to input for the input_menu_choice() function

    """
    @staticmethod
    def output_menu(menu: str):
        print(menu)
    
    """
    This function prompts the user to select an option. If they don't select 1, 2, 3, or 4, then 
    it prompts them to try to select one of those options again
    
    """
    @staticmethod
    def input_menu_choice():
        try:
            user_choice = input("Please select an option: ")
            if user_choice not in ("1","2","3","4"):
                raise Exception("Please select only 1, 2, 3, or 4.")
        except Exception as e:
            IO.output_error_messages("Unknown Error.",e.__str__())
        return user_choice

    """
    This function prints the current list of student data (including inputs from the user)
    
    """
    @staticmethod
    def output_student_courses(student_data: list):
        print("The current list of students is:")
        print("Name \t\tLast Name \tCourse")
        for student in student_data:
            print(f"{student["First_Name"]} \t\t {student["Last_Name"]} \t\t{student["Course"]}")

    """
    This function takes in users' inputs for a student's first name, last name, and course and adds that student to the dictionary of student data

    """
    @staticmethod
    def input_student_data(student_data: list):
        try:
            student_first_name = input("Please enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers or symbols")
            student_last_name = input("Please enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The first name and last name should not contain numbers or symbols")
            course_name = input("Please enter the course name: ")
            new_student = {
                    "First_Name": student_first_name,
                    "Last_Name": student_last_name,
                    "Course": course_name
                    }
            student_data.append(new_student)
        except ValueError as e:
            IO.output_error_messages("There is a incorrect value.", e)
        except Exception as e:
            IO.output_error_messages("Unknown error.", e)
        return student_data


# Actual program begins here
if __name__ == "__main__":

    # Reading in the file
    students = FileProcessor.read_data_from_file(file_name = FILE_NAME, student_data = students)

    # A While loop that facilitates the Menu and according actions
    while True:
        IO.output_menu(MENU)
        
        menu_choice = IO.input_menu_choice()

        match menu_choice:
            case "1":
                IO.input_student_data(student_data = students)
            case "2":
                IO.output_student_courses(student_data = students)
            case "3":
                FileProcessor.write_data_to_file(file_name = FILE_NAME, student_data = students)
            case "4":
                print("The program has ended.")
                exit()