from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

students = db["students"]
courses = db["courses"]
enrollments = db["enrollments"]

# 1️⃣ Delete a student
print("----- DELETE STUDENT -----")
result = students.delete_one({"email": "asha_new@gmail.com"})
print("Deleted count:", result.deleted_count)


# 2️⃣ Delete courses with 0 credits
print("\n----- DELETE COURSES WITH 0 CREDITS -----")
result = courses.delete_many({"credits": 0})
print("Deleted count:", result.deleted_count)


# 3️⃣ Delete enrollments of a specific student
print("\n----- DELETE ENROLLMENTS OF STUDENT -----")
result = enrollments.delete_many({"student_id": 1})
print("Deleted count:", result.deleted_count)

print("\nDelete operations completed successfully.")