from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["collegeDB"]

students = db["students"]
departments = db["departments"]
courses = db["courses"]
enrollments = db["enrollments"]

print("----- STUDENTS PER DEPARTMENT -----")

pipeline = [
    {
        "$group": {
            "_id": "$department_id",
            "total_students": {"$sum": 1}
        }
    }
]

for result in students.aggregate(pipeline):
    print(result)



print("\n----- ENROLLMENTS PER COURSE -----")

pipeline = [
    {
        "$group": {
            "_id": "$course_id",
            "total_enrollments": {"$sum": 1}
        }
    }
]

for result in enrollments.aggregate(pipeline):
    print(result)



print("\n----- AVERAGE AGE OF STUDENTS -----")

pipeline = [
    {
        "$group": {
            "_id": None,
            "average_age": {"$avg": "$age"}
        }
    }
]

for result in students.aggregate(pipeline):
    print(result)



print("\n----- COURSE WITH MAX ENROLLMENTS -----")

pipeline = [
    {
        "$group": {
            "_id": "$course_id",
            "total_enrollments": {"$sum": 1}
        }
    },
    {
        "$sort": {"total_enrollments": -1}
    },
    {
        "$limit": 1
    }
]

for result in enrollments.aggregate(pipeline):
    print(result)



print("\n----- STUDENTS WITH DEPARTMENT DETAILS -----")

pipeline = [
    {
        "$lookup": {
            "from": "departments",
            "localField": "department_id",
            "foreignField": "department_id",
            "as": "department_info"
        }
    },
    {
        "$project": {
            "_id": 0,
            "name": 1,
            "department_info.department_name": 1
        }
    }
]

for result in students.aggregate(pipeline):
    print(result)

print("\nAggregation operations completed successfully!")