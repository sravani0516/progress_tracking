from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

students = db["students"]
courses = db["courses"]

# 1️⃣ Find students aged between 18 and 25
print("----- STUDENTS AGE BETWEEN 18 AND 25 -----")
for student in students.find({
    "$and": [
        {"age": {"$gt": 18}},
        {"age": {"$lt": 25}}
    ]
}):
    print(student)


# 2️⃣ Find courses with credits 2, 3, or 4
print("\n----- COURSES WITH CREDITS 2, 3, OR 4 -----")
for course in courses.find({
    "credits": {"$in": [2, 3, 4]}
}):
    print(course)


# 3️⃣ Find students NOT in department 101
print("\n----- STUDENTS NOT IN DEPARTMENT 101 -----")
for student in students.find({
    "department_id": {"$ne": 101}
}):
    print(student)

print("\nQuery operator operations completed successfully.")