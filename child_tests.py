from hourly_worker import hourly_worker
from commission_worker import commission_worker
# Import child classes of worker

x = hourly_worker(1, 101, "John Doe", 3, 3, 12, 6, 0)
y = commission_worker(2, 102, "John Doe", 3, 3, 5, 100)

print("Hourly worker tests:")
print("Employee number test:")
print(x.get_employee_number()) # Default 1
x.set_employee_number(6)
print(x.get_employee_number()) # Now 6
print("Office number test:")
print(x.get_office_number()) # Default 101
print(x.set_office_number(99)) # False
print(x.set_office_number(602)) # False
print(x.set_office_number(378)) # True (valid office number)
print(x.get_office_number()) # Now 378
print("Name test:")
print(x.get_name()) # Default John Doe
x.set_name("Blake Parley")
print(x.get_name()) # Now Blake Parley
print("Birthdate test:")
print(x.is_birthday(3,3)) # Default True
print(x.is_birthday(7,2)) # Default False
print(x.set_birthdate(7,2)) # True (valid birthdate)
print(x.set_birthdate(11,40)) # False (invalid birthdate)
print(x.is_birthday(3,3)) # Now False
print(x.is_birthday(7,2)) # Now True
print("Hours test:")
print("Regular: " + str(x.get_hours_worked())) # Default 6
print("Overtime: " + str(x.get_hours_overtime())) # Default 0
x.add_hours(18)
print("Regular: " + str(x.get_hours_worked())) # Now 15
print("Overtime: " + str(x.get_hours_overtime())) # Now 9
x.add_hours(6)
print("Regular: " + str(x.get_hours_worked())) # Now 21
print("Overtime: " + str(x.get_hours_overtime())) # Now 9


print("\nCommission worker tests:")
print("Employee number test:")
print(y.get_employee_number()) # Default 2
y.set_employee_number(6)
print(y.get_employee_number()) # Now 6
print("Office number test:")
print(y.get_office_number()) # Default 102
print(y.set_office_number(99)) # False
print(y.set_office_number(602)) # False
print(y.set_office_number(378)) # True (valid office number)
print(y.get_office_number()) # Now 378
print("Name test:")
print(y.get_name()) # Default John Doe
y.set_name("Blake Parley")
print(y.get_name()) # Now Blake Parley
print("Birthdate test:")
print(y.is_birthday(3,3)) # Default True
print(y.is_birthday(7,2)) # Default False
print(y.set_birthdate(7,2)) # True (valid birthdate)
print(y.set_birthdate(11,40)) # False (invalid birthdate)
print(y.is_birthday(3,3)) # Now False
print(y.is_birthday(7,2)) # Now True
print("Salary test:")
print(y.get_salary()) # Default 5.0
y.add_sales(299900)
print(y.get_salary()) # Now 15000
y.add_sales(1)
print(y.get_salary()) # Now 24000.08
