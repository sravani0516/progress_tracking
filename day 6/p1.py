from employee.employee import Employee

employees = [
    Employee(101, "Ravi", "9876543210", 45000, "HR", "ravi@company.com"),
    Employee(102, "Sravani", "9123456780", 55000, "IT", "sravani@company.com"),
    Employee(103, "Anil", "9988776655", 50000, "Finance", "anil@company.com")
]

name = input("Enter employee name: ")

for emp in employees:
    if emp.name.lower() == name.lower():
        print("\nEmployee Details:")
        emp.display()
        break
else:
    print("Employee not found.")
