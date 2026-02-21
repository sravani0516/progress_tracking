from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

students = db["students"]
departments = db["departments"]
courses = db["courses"]
instructors = db["instructors"]
enrollments = db["enrollments"]

students.delete_many({})
departments.delete_many({})
courses.delete_many({})
instructors.delete_many({})
enrollments.delete_many({})

departments.insert_many([
    {"department_id": 101, "department_name": "Computer Science"},
    {"department_id": 102, "department_name": "Mechanical Engineering"},
    {"department_id": 103, "department_name": "Business Administration"}
])

instructors.insert_many([
    {"instructor_id": 9001, "name": "Dr. Smith"},
    {"instructor_id": 9002, "name": "Dr. Johnson"}
])

students.insert_many([
    {"student_id": 1, "name": "Asha", "age": 21, "email": "asha@gmail.com", "department_id": 101},
    {"student_id": 2, "name": "Ravi", "age": 23, "email": "ravi@gmail.com", "department_id": 102},
    {"student_id": 3, "name": "Meena", "age": 19, "email": "meena@gmail.com", "department_id": 101}
])

courses.insert_many([
    {"course_id": 201, "course_name": "Data Structures", "credits": 4, "instructor_id": 9001},
    {"course_id": 202, "course_name": "Thermodynamics", "credits": 3, "instructor_id": 9002}
])


enrollments.insert_many([
    {"enrollment_id": 1, "student_id": 1, "course_id": 201},
    {"enrollment_id": 2, "student_id": 2, "course_id": 202},
    {"enrollment_id": 3, "student_id": 1, "course_id": 202}
])

print("Referencing documents inserted successfully!")