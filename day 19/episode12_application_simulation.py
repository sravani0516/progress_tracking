from pymongo import MongoClient
from bson import ObjectId

print("----- APPLICATION INTEGRATION SIMULATION -----")

client = MongoClient("mongodb://localhost:27017/")
db = client["universityDB"]

students = db["students"]
instructors = db["instructors"]
courses = db["courses"]
enrollments = db["enrollments"]

students.delete_many({})
instructors.delete_many({})
courses.delete_many({})
enrollments.delete_many({})


print("\n--- SCENARIO 1 ---")

student = {
    "name": "Ravi",
    "email": "ravi@gmail.com",
    "age": 21
}
student_id = students.insert_one(student).inserted_id
print("Student Registered:", student_id)

course = {
    "course_name": "Database Systems",
    "course_code": "DB101"
}
course_id = courses.insert_one(course).inserted_id
print("Course Created:", course_id)

enrollment = {
    "student_id": student_id,
    "course_id": course_id,
    "status": "Enrolled"
}
enrollments.insert_one(enrollment)
print("Student Enrolled in Course")

students.update_one(
    {"_id": student_id},
    {"$set": {"age": 22}}
)
print("Student Profile Updated")

enrollments.delete_one({
    "student_id": student_id,
    "course_id": course_id
})
print("Course Dropped")



print("\n--- SCENARIO 2 ---")

instructor = {
    "name": "Dr. Sharma",
    "department": "Computer Science"
}
instructor_id = instructors.insert_one(instructor).inserted_id
print("Instructor Created:", instructor_id)

course2 = {
    "course_name": "Python Programming",
    "course_code": "PY101",
    "instructor_id": None
}
course2_id = courses.insert_one(course2).inserted_id
print("Course Created:", course2_id)

courses.update_one(
    {"_id": course2_id},
    {"$set": {"instructor_id": instructor_id}}
)
print("Instructor Assigned to Course")

student_ids = []

for i in range(3):
    new_student = {
        "name": f"Student{i+1}",
        "email": f"student{i+1}@gmail.com",
        "age": 20 + i
    }
    sid = students.insert_one(new_student).inserted_id
    student_ids.append(sid)

print("Students Created:", student_ids)

for sid in student_ids:
    enrollments.insert_one({
        "student_id": sid,
        "course_id": course2_id,
        "status": "Enrolled"
    })

print("All Students Enrolled in Course")

print("\n----- SIMULATION COMPLETED SUCCESSFULLY -----")