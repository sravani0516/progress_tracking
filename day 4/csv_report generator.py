import csv

data = [
    ["Name", "Department", "Salary"],  # header
    ["Alice", "HR", 50000],
    ["Bob", "IT", 60000],
    ["Charlie", "Finance", 55000]
]

csv_file = "employee_report.csv"

with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV report generated successfully: {csv_file}")
