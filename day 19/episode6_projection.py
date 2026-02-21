from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

students = db["students"]
courses = db["courses"]

# 1️⃣ Show only student name and email
print("----- STUDENT NAME AND EMAIL ONLY -----")
for student in students.find(
    {},
    {"_id": 0, "name": 1, "email": 1}
):
    print(student)


# 2️⃣ Hide student_id field
print("\n----- HIDE student_id FIELD -----")
for student in students.find(
    {},
    {"student_id": 0}
):
    print(student)


# 3️⃣ Show only course name
print("\n----- COURSE NAME ONLY -----")
for course in courses.find(
    {},
    {"_id": 0, "course_name": 1}
):
    print(course)

print("\nProjection operations completed successfully.")