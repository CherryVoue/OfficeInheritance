# initializes default variables from object creation
class worker():
    def __init__(self, empNum, offNum, name, birthMonth, birthDay):
        self.empNum = empNum
        self.offNum = offNum
        self.name = name
        self.birthdate = {"month": birthMonth, "day": birthDay}
    # function returns the employee's number
    def get_employee_number(self):
        return self.empNum
    # function sets the employee's number to a given number
    def set_employee_number(self, num):
        self.empNum = num
    # function returns the number of the employee's office
    def get_office_number(self):
        return self.offNum
    # function sets the employee's office to a given number between 100 and 500, returns boolean based on that condition
    def set_office_number(self, num):
        if num < 100 or num > 500:
            return False
        self.offNum = num
        return True
    # function returns the employee's name
    def get_name(self):
        return self.name
    # function sets the employee's name to a given string
    def set_name(self, name):
        self.name = name
    # function sets the employees birthdate to a given date and month, returns boolean determining whether the date is valid
    def set_birthdate(self, month, day):
        if month > 12 or month < 1 or day > 31 or day < 1:
            return False
        self.birthdate = {"month": month, "day": day}
        return True
    # returns boolean based on whether the given month and day match that of the employee's birthdate
    def is_birthday(self, currMonth, currDay):
        return (self.birthdate["month"] == currMonth and self.birthdate["day"] == currDay)

