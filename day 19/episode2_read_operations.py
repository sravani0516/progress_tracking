from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

students = db["students"]
courses = db["courses"]

print("----- ALL STUDENTS -----")
for student in students.find():
    print(student)


print("\n----- STUDENTS OLDER THAN 20 -----")
for student in students.find({"age": {"$gt": 20}}):
    print(student)


print("\n----- FIND STUDENT BY EMAIL -----")
result = students.find_one({"email": "asha@gmail.com"})
print(result)


print("\n----- COURSES WITH CREDITS > 3 -----")
for course in courses.find({"credits": {"$gt": 3}}):
    print(course)


print("\n----- STUDENTS FROM DEPARTMENT 101 -----")
for student in students.find({"department_id": 101}):
    print(student)