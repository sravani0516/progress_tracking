from pymongo import MongoClient, errors

print("----- FUNCTIONAL TESTING STARTED -----")

client = MongoClient("mongodb://localhost:27017/")
db = client["universityDB"]
students = db["students"]


try:
    students.drop_index("email_1")
except:
    pass

students.create_index("email", unique=True)


def print_result(tc, description, expected, actual):
    status = "PASS" if expected == actual else "FAIL"
    print("\n----------------------------------")
    print(f"Test Case: {tc}")
    print(f"Description: {description}")
    print(f"Expected Result: {expected}")
    print(f"Actual Result: {actual}")
    print(f"Status: {status}")
    print("----------------------------------")

students.delete_many({})

try:
    students.insert_one({
        "name": "Rahul",
        "email": "rahul@gmail.com",
        "age": 20
    })
    print_result("TC1", "Insert valid student", "Inserted", "Inserted")
except:
    print_result("TC1", "Insert valid student", "Inserted", "Error")

try:
    students.insert_one({
        "name": "MissingEmail"
    })
    print_result("TC2", "Insert student with missing fields", "Error", "Inserted")
except:
    print_result("TC2", "Insert student with missing fields", "Error", "Error")

try:
    students.insert_one({
        "name": "Rahul2",
        "email": "rahul@gmail.com",
        "age": 22
    })
    print_result("TC3", "Insert duplicate email", "Duplicate Error", "Inserted")
except errors.DuplicateKeyError:
    print_result("TC3", "Insert duplicate email", "Duplicate Error", "Duplicate Error")

result = students.update_one(
    {"email": "notfound@gmail.com"},
    {"$set": {"age": 30}}
)

if result.matched_count == 0:
    print_result("TC4", "Update non-existing student", "No Update", "No Update")
else:
    print_result("TC4", "Update non-existing student", "No Update", "Updated")


result = students.delete_one({"email": "rahul@gmail.com"})

if result.deleted_count == 1:
    print_result("TC5", "Delete existing student", "Deleted", "Deleted")
else:
    print_result("TC5", "Delete existing student", "Deleted", "Not Deleted")

print("\n----- FUNCTIONAL TESTING COMPLETED -----")