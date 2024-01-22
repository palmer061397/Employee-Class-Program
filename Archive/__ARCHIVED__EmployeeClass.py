import datetime

class Person:
  def __init__(self, fname: str, lname: str, title: str):
    self.firstname = fname 
    self.lastname = lname
    self.jobtitle = title

    self.hiredate = datetime.date.today()

  # Returns first name
  def get_firstname(self) -> object:
    return self.firstname

  # Sets firstname if fname isn't an empty string
  def set_firstname(self,fname: str) -> None:
    if len(fname) > 0:
      self.firstname = fname

  # returns last name
  def get_lastname(self) -> object:
    return self.lastname

  # Sets last name if lname isn't an empty string
  def set_lastname(self,lname: str) -> None:
    if len(lname) > 0:
      self.lastname = lname

  # returns job title
  def get_jobtitle(self) -> object:
    return self.jobtitle

  # Sets job title if job title isn't an empty string
  def set_jobtitle(self,title: str) -> None:
    if len(title) > 0:
      self.jobtitle = title
      
class Employee(Person):
  def __init__(self,fname: str,lname: str,title: str,sal: int,empid: int):
    super().__init__(fname,lname,title)
    self.employeeid = empid
    self.salary = sal
    self.vacationdaysperyear = 14
    self.vacationdays = self.vacationdaysperyear

  # Return employee id
  def get_employeeid(self) -> str:
    return "Employee ID: " + str(self.employeeid)

  # Returns salary
  def get_salary(self) -> str:
    return "{:,.2f}".format(self.salary)

  # Sets salary if salary isn't an empty string
  def set_salary(self, sal: int) -> None:
    if sal > 0:
      self.salary = sal

  # Increase salary
  def increase_salary(self,percent: float) -> None:
    if percent > 0:
      self.set_salary(self.salary + self.salary * percent)
    else:
      print("Increase of salary must be greater than 0.")

  # Increase vacation days per year
  def increase_vacation_days_per_year(self,days: int) -> None:
    if days > 0:
      self.vacationdaysperyear += days

  # Increase vacation days
  def increase_vacation_days(self,days: int) -> None:
    if days > 0:
      self.vacationdays += days

  # Increase vacation days by year
  def increase_vacation_days_yearly(self) -> None:
    self.vacationdays += self.vacationdaysperyear

  # Take some vacation days
  def take_vacation_days(self,days: int) -> None:
    if days > 0 and self.vacationdays - days >= 0:
      self.vacationdays -= days
    elif days <= 0:
      print("Vacation days taken must be greater than 0.")
    elif self.vacationdays - days < 0:
      print(f"Employee does not have enough vacation days to take off {days} days.")

  # Return vacation days
  def get_vacation_days(self) -> str:
    return "Vacation Days: " + str(self.vacationdays)

class Contracter(Person):
  def __init__(self, fname: str, lname: str,title: str, wage: int, contractorid: int):
    super().__init__(fname,lname,title)
    self.contractorid = contractorid
    self.hourlywage = wage

  # Return contractor ID
  def get_contractorid(self) -> str:
    return "Contractor ID: " + str(self.contractorid)

  # Set hourly wage
  def set_hourlywage(self, wage: str) -> None:
    if wage > 0:
      self.hourlywage = wage

  # returns wage
  def get_hourlywage(self) -> str:
    return "${:,.2f}".format(self.hourlywage)

  # Sets job wage if wage is greater than 0
  def set_get_hourlywage(self,get_hourlywage: object) -> None:
    if get_hourlywage > 0:
      self.wage = get_hourlywage


# Testing Class and Subclass

con1 = Contracter('Temp','Emp','Developer',60,2)
print(con1.get_firstname())
print(con1.get_lastname())
print(con1.get_contractorid())
print(con1.get_jobtitle())
print(con1.get_hourlywage())
print(con1.set_hourlywage(50))
print(con1.get_hourlywage())