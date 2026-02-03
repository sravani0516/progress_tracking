from decorators.access import registration, login
from employee.details import show_employee
@registration
def register(name,email,phone,designation,salary):
    show_employee(name,email,phone,designation,salary)
@login
def user_login(username,login_status):
    print("Accessing Dashboard...")
register("sravani","sravani12@example.com",9658214730,"HR Manager",80000)
user_login("sravani", True)