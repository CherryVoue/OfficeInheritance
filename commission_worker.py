# imports necessary parent class
from worker import worker
# initializes default variables from object creation
class commission_worker(worker):
    def __init__(self, empNum, offNum, name, birthMonth, birthDay, commission, sales):
        super().__init__(empNum, offNum, name, birthMonth, birthDay)
        self.commission = commission
        self.sales = sales
    # function to add a given amount of sales
    def add_sales(self, sales):
        self.sales += sales
    # function returns the worker's salary based on sales performance
    def get_salary(self):
        if self.sales > 300000:
            return ((self.sales * (self.commission / 100)) + (self.sales * 0.03))
        return (self.sales * (self.commission / 100))
