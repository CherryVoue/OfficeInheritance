# imports necessary parent class
from worker import worker
# initializes default variables from object creation
class hourly_worker(worker):
    def __init__(self, empNum, offNum, name, birthMonth, birthDay, hourlySalary, regHours, overHours):
        super().__init__(empNum, offNum, name, birthMonth, birthDay)
        self.hourlySalary = hourlySalary
        self.regHours = regHours
        self.overHours = overHours
    # function returns normal hours worked by the employee
    def get_hours_worked(self):
        return self.regHours
    # function appropriately divides a given amount of hours between regular hour and overtime hour variables
    def add_hours(self, hours):
        if hours > 9:
            self.regHours += 9
            self.overHours += (hours-9)
        else:
            self.regHours += hours
    # fucntion returns worker's overtime hours
    def get_hours_overtime(self):
        return self.overHours
    # calculates and returns the worker's salary based on hours worked
    def get_salary(self):
        return ((self.regHours * self.hourlySalary) + (self.overHours * (self.hourlySlary * 1.5)))
