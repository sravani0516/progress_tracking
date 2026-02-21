from pymongo import MongoClient
import time

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

students = db["students"]
courses = db["courses"]

print("----- TEST PERFORMANCE BEFORE INDEX -----")

start = time.time()
students.find_one({"email": "asha@gmail.com"})
end = time.time()

print("Time BEFORE index:", end - start)




print("\n----- CREATING INDEXES -----")

students.create_index("email")
courses.create_index("course_id")
students.create_index("department_id")

print("Indexes created successfully!")



print("\n----- TEST PERFORMANCE AFTER INDEX -----")

start = time.time()
students.find_one({"email": "asha@gmail.com"})
end = time.time()

print("Time AFTER index:", end - start)

print("\nIndexing test completed successfully!")