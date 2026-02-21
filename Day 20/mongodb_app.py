from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# 1. Create database and collection
db = client["school"]
students = db["students"]

# Clear old data (optional)
students.delete_many({})

# 2 & 3. Insert documents
students.insert_many([
    {"name": "Ravi", "age": 20, "course": "Python"},
    {"name": "Ram", "age": 21, "course": "Java"},
    {"name": "Sita", "age": 22, "course": "Python"},
    {"name": "Arjun", "age": 19, "course": "C++"},
    {"name": "Meena", "age": 23, "course": "Python"}
])

# 4. Find all
print("All Students:")
for s in students.find():
    print(s)

# 5. Age > 20
print("\nAge > 20:")
for s in students.find({"age": {"$gt": 20}}):
    print(s)

# 6. Specific fields
print("\nName and Course:")
for s in students.find({}, {"_id": 0, "name": 1, "course": 1}):
    print(s)

# 7. Find one
print("\nFind Ravi:")
print(students.find_one({"name": "Ravi"}))

# 8. Update one
students.update_one({"name": "Ravi"}, {"$set": {"course": "MongoDB"}})

# 9. Update many
students.update_many({"course": "Python"}, {"$set": {"course": "Full Stack"}})

# 10. Delete one
students.delete_one({"name": "Ram"})

# 11. Delete many
students.delete_many({"age": {"$lt": 20}})

# 12. Sort
print("\nSorted by age:")
for s in students.find().sort("age", 1):
    print(s)

# 13. Limit
print("\nLimit 3:")
for s in students.find().limit(3):
    print(s)

# 14. Count
print("\nTotal Students:", students.count_documents({}))

# 15. AND condition
print("\nAND condition:")
for s in students.find({
    "$and": [{"age": {"$gt": 20}}, {"course": "Full Stack"}]
}):
    print(s)

# 16. OR condition
print("\nOR condition:")
for s in students.find({
    "$or": [{"course": "Full Stack"}, {"course": "Java"}]
}):
    print(s)

# 17. Aggregation - count per course
print("\nStudents per course:")
pipeline = [{"$group": {"_id": "$course", "total": {"$sum": 1}}}]
for s in students.aggregate(pipeline):
    print(s)

# 18. Aggregation - average age
print("\nAverage age:")
pipeline = [{"$group": {"_id": None, "avgAge": {"$avg": "$age"}}}]
for s in students.aggregate(pipeline):
    print(s)

# 19. Create index
students.create_index("name")

# 20. Embedded document
students.insert_one({
    "name": "Krishna",
    "age": 23,
    "address": {
        "city": "Hyderabad",
        "state": "Telangana"
    }
})

print("\nNested query:")
for s in students.find({"address.city": "Hyderabad"}):
    print(s)