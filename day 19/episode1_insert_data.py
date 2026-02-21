from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

students = db["students"]
courses = db["courses"]
departments = db["departments"]
instructors = db["instructors"]
enrollments = db["enrollments"]

# Insert Departments
departments.insert_many([
    {"department_id": 101, "department_name": "Computer Science"},
    {"department_id": 102, "department_name": "Electronics"},
    {"department_id": 103, "department_name": "Mechanical"},
    {"department_id": 104, "department_name": "Civil"},
    {"department_id": 105, "department_name": "Information Technology"}
])

# Insert Instructors
instructors.insert_many([
    {"instructor_id": 201, "name": "Dr. Rao"},
    {"instructor_id": 202, "name": "Dr. Mehta"},
    {"instructor_id": 203, "name": "Dr. Sharma"},
    {"instructor_id": 204, "name": "Dr. Gupta"},
    {"instructor_id": 205, "name": "Dr. Verma"}
])

# Insert Students
students.insert_many([
    {"student_id": 1, "name": "Asha", "age": 21, "email": "asha@gmail.com", "department_id": 101},
    {"student_id": 2, "name": "Ravi", "age": 19, "email": "ravi@gmail.com", "department_id": 102},
    {"student_id": 3, "name": "Neha", "age": 23, "email": "neha@gmail.com", "department_id": 101},
    {"student_id": 4, "name": "Kiran", "age": 22, "email": "kiran@gmail.com", "department_id": 103},
    {"student_id": 5, "name": "Sita", "age": 20, "email": "sita@gmail.com", "department_id": 105}
])

# Insert Courses
courses.insert_many([
    {"course_id": 301, "course_name": "DBMS", "credits": 4, "instructor_id": 201},
    {"course_id": 302, "course_name": "Artificial Intelligence", "credits": 3, "instructor_id": 202},
    {"course_id": 303, "course_name": "Machine Learning", "credits": 4, "instructor_id": 203},
    {"course_id": 304, "course_name": "Computer Networks", "credits": 3, "instructor_id": 204},
    {"course_id": 305, "course_name": "Operating Systems", "credits": 4, "instructor_id": 205}
])

# Insert Enrollments
enrollments.insert_many([
    {"enrollment_id": 1, "student_id": 1, "course_id": 301},
    {"enrollment_id": 2, "student_id": 1, "course_id": 302},
    {"enrollment_id": 3, "student_id": 2, "course_id": 303},
    {"enrollment_id": 4, "student_id": 3, "course_id": 304},
    {"enrollment_id": 5, "student_id": 4, "course_id": 305}
])

print("Episode 1 Completed: Data Inserted Successfully")