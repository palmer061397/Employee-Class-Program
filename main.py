import csv
import sys

FILENAME = "employees.csv"

# Exiting the program
def exit_program():
  print("Terminating program.")
  sys.exit()

# Read the employees from the file
def read_employees():
  try:
      employees = []
      with open(FILENAME, newline="") as file:
          reader = csv.reader(file)
          for row in reader:
              employees.append(row)
      return employees
  except FileNotFoundError as error:
      print(f"Could not find {FILENAME} file.")
      exit_program()
  except Exception as e:
      print(type(e), e)
      exit_program()

# Write employees to files
def write_employees(employees):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(employees)
    except Exception as e:
        print(type(e), e)
        exit_program()

# Updates salary
def update_salary(employees):
    empid = input("Enter the employee ID: ")
    new_sal = input("Enter the new salary of the employee: ")

    found = False
    for i in range(0,len(employees)):
        if employees[i][0] == empid:
            found = True
            employees[i][1] = new_sal
            write_employees(employees)
            print("Employee salary updated.")
            break

# Add employee to the list
def add_employee(employees):
    empid = input("Enter the employee ID: ")
    sal = input("Enter the salary of the employee: ")
    employee = [empid,sal]
    employees.append(employee)
    write_employees(employees)
    print(f"Employee {empid}: {sal} was added. \n")

# Display the list of employees
def list_employees(employees):
    for i, employee in enumerate(employees, start=1):
        print(f"{i} Employee ID: {employee[0]} (${employee[1]})")
    print()

# Delete an employee based on ID
def delete_employee(employees):
    found = False
    number = input("Enter in the employee ID: ")
    for i, employee in enumerate(employees, start=0):
        if (employee[0] == number):
            print(f"Employee was deleted.\n")
            employee = employees.pop(i)
            found = True

    if (found == False):
        print("Employee was not found.\n")
    else:
        write_employees(employees)

# Menu
def display_menu():
    print("The Employee Salary List program")
    print()
    print("LIST OF COMMANDS")
    print("list - List all employees")
    print("add - Add an employee")
    print("updsal - Update employee salary")
    print("del - Delete and employee")
    print("exit - Exit program")
    print()

display_menu()
employees = read_employees()
while True:
    command = input("Command: ")
    if command.lower() == "list":
        list_employees(employees)
    elif command.lower() == "add":
        add_employee(employees)
    elif command.lower() == "del":
        delete_employee(employees)
    elif command.lower() == "updsal":
        update_salary(employees)
    elif command.lower() == "exit":
        break
    else:
        print("Not a valid command. Please try agian.\n")
print("Ending Salary Program")
