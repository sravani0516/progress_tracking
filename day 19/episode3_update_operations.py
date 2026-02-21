from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

students = db["students"]
courses = db["courses"]
departments = db["departments"]

print("----- UPDATE STUDENT EMAIL -----")
result = students.update_one(
    {"email": "asha@gmail.com"},   # old email
    {"$set": {"email": "asha_new@gmail.com"}}
)
print("Modified count:", result.modified_count)


print("\n----- INCREASE COURSE CREDITS -----")
result = courses.update_one(
    {"course_id": 201},
    {"$inc": {"credits": 1}}
)
print("Modified count:", result.modified_count)


print("\n----- CHANGE INSTRUCTOR -----")
result = courses.update_one(
    {"course_id": 202},
    {"$set": {"instructor_id": 9002}}
)
print("Modified count:", result.modified_count)


print("\n----- UPDATE DEPARTMENT NAME -----")
result = departments.update_one(
    {"department_id": 101},
    {"$set": {"department_name": "Computer Engineering"}}
)
print("Modified count:", result.modified_count)

print("\nUpdate operations completed successfully.")