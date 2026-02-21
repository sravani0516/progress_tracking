from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson import ObjectId

print("----- TRANSACTION TESTING STARTED -----")

MongoClient("mongodb://localhost:27017/")
db = client["universityDB"]

students = db["students"]
courses = db["courses"]
enrollments = db["enrollments"]

# Clear collections
students.delete_many({})
courses.delete_many({})
enrollments.delete_many({})

# Create a course with enrollment_count
course_id = courses.insert_one({
    "course_name": "Advanced MongoDB",
    "enrollment_count": 0
}).inserted_id

print("Course Created:", course_id)


# ==================================================
# SCENARIO 1 — SUCCESSFUL TRANSACTION
# ==================================================

print("\n--- SCENARIO 1: Successful Transaction ---")

with client.start_session() as session:
    try:
        with session.start_transaction():

            # 1️⃣ Insert Student
            student_id = students.insert_one(
                {"name": "Kiran", "email": "kiran@gmail.com", "age": 23},
                session=session
            ).inserted_id

            # 2️⃣ Insert Enrollment
            enrollments.insert_one(
                {"student_id": student_id, "course_id": course_id},
                session=session
            )

            # 3️⃣ Update Course Enrollment Count
            courses.update_one(
                {"_id": course_id},
                {"$inc": {"enrollment_count": 1}},
                session=session
            )

        print("Transaction Committed Successfully ✅")

    except PyMongoError as e:
        print("Transaction Failed ❌")
        print(e)


# Check result
print("Enrollment Count After Success:",
      courses.find_one({"_id": course_id})["enrollment_count"])


# ==================================================
# SCENARIO 2 — FAILED TRANSACTION (ROLLBACK)
# ==================================================

print("\n--- SCENARIO 2: Failed Transaction (Rollback) ---")

with client.start_session() as session:
    try:
        with session.start_transaction():

            # 1️⃣ Insert Student
            student_id = students.insert_one(
                {"name": "Arjun", "email": "arjun@gmail.com", "age": 24},
                session=session
            ).inserted_id

            # 2️⃣ Insert Enrollment
            enrollments.insert_one(
                {"student_id": student_id, "course_id": course_id},
                session=session
            )

            # 3️⃣ Force Error (simulate failure)
            raise Exception("Simulated Failure!")

            # 4️⃣ Update Course Count (won’t execute)
            courses.update_one(
                {"_id": course_id},
                {"$inc": {"enrollment_count": 1}},
                session=session
            )

    except Exception as e:
        print("Transaction Aborted ❌")
        print("Reason:", e)

# Check result again
print("Enrollment Count After Rollback:",
      courses.find_one({"_id": course_id})["enrollment_count"])

print("\n----- TRANSACTION TESTING COMPLETED -----")