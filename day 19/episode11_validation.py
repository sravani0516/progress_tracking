from pymongo import MongoClient
from pymongo.errors import WriteError

print("----- DATA VALIDATION TESTING STARTED -----")

client = MongoClient("mongodb://localhost:27017/")
db = client["universityDB"]

db.drop_collection("students")

db.create_collection(
    "students",
    validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "email", "age"],
            "properties": {
                "name": {
                    "bsonType": "string",
                    "description": "Name must be a string"
                },
                "email": {
                    "bsonType": "string",
                    "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
                    "description": "Email must be valid format"
                },
                "age": {
                    "bsonType": "int",
                    "minimum": 16,
                    "maximum": 60,
                    "description": "Age must be between 16 and 60"
                }
            }
        }
    }
)

students = db["students"]



def test_insert(test_name, document):
    try:
        students.insert_one(document)
        print(f"{test_name}: PASS (Inserted)")
    except WriteError as e:
        print(f"{test_name}: FAIL (Validation Error)")
        print("Reason:", e.details["errmsg"])


test_insert("TC1 - Valid Student", {
    "name": "Anita",
    "email": "anita@gmail.com",
    "age": 22
})

test_insert("TC2 - Invalid Name", {
    "name": 12345,
    "email": "num@gmail.com",
    "age": 25
})

test_insert("TC3 - Invalid Email", {
    "name": "InvalidEmail",
    "email": "wrongemailformat",
    "age": 30
})

test_insert("TC4 - Age Below 16", {
    "name": "YoungStudent",
    "email": "young@gmail.com",
    "age": 12
})

test_insert("TC5 - Age Above 60", {
    "name": "OldStudent",
    "email": "old@gmail.com",
    "age": 75
})

print("\n----- DATA VALIDATION TESTING COMPLETED -----")