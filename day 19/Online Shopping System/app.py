# episode14_online_shopping_case_study.py

from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

print("----- ONLINE SHOPPING CASE STUDY -----")

# 1️⃣ Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["shoppingDB"]

# 2️⃣ Create Collections
users = db["users"]
products = db["products"]
orders = db["orders"]
payments = db["payments"]
reviews = db["reviews"]

# 3️⃣ Clear old data (optional, for reruns)
users.delete_many({})
products.delete_many({})
orders.delete_many({})
payments.delete_many({})
reviews.delete_many({})

# =================================================
# 4️⃣ INSERT SAMPLE DATA
# =================================================

# Users
user1_id = users.insert_one({
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "address": "Hyderabad",
    "created_at": datetime.utcnow()
}).inserted_id

user2_id = users.insert_one({
    "name": "Anita",
    "email": "anita@gmail.com",
    "address": "Bangalore",
    "created_at": datetime.utcnow()
}).inserted_id

# Products
product1_id = products.insert_one({
    "name": "Laptop",
    "category": "Electronics",
    "price": 60000,
    "stock": 10,
    "total_sold": 0
}).inserted_id

product2_id = products.insert_one({
    "name": "Mobile",
    "category": "Electronics",
    "price": 20000,
    "stock": 20,
    "total_sold": 0
}).inserted_id

# Orders
order1_id = orders.insert_one({
    "user_id": user1_id,
    "items": [
        {"product_id": product1_id, "quantity": 1, "price": 60000}
    ],
    "total_amount": 60000,
    "order_date": datetime.utcnow(),
    "status": "Delivered"
}).inserted_id

order2_id = orders.insert_one({
    "user_id": user1_id,
    "items": [
        {"product_id": product2_id, "quantity": 2, "price": 20000}
    ],
    "total_amount": 40000,
    "order_date": datetime.utcnow(),
    "status": "Delivered"
}).inserted_id

# Update product sales
products.update_one({"_id": product1_id}, {"$inc": {"total_sold": 1}})
products.update_one({"_id": product2_id}, {"$inc": {"total_sold": 2}})

# Payments
payments.insert_one({
    "order_id": order1_id,
    "amount": 60000,
    "method": "UPI",
    "status": "Success"
})

payments.insert_one({
    "order_id": order2_id,
    "amount": 40000,
    "method": "Card",
    "status": "Success"
})

# Reviews
reviews.insert_one({
    "user_id": user1_id,
    "product_id": product1_id,
    "rating": 5,
    "comment": "Excellent Laptop"
})

print("Sample Data Inserted Successfully")

# =================================================
# 5️⃣ QUERY USER ORDERS
# =================================================

print("\n--- User Orders (Rahul) ---")
for order in orders.find({"user_id": user1_id}):
    print(order)

# =================================================
# 6️⃣ TOP SELLING PRODUCT
# =================================================

print("\n--- Top Selling Product ---")
top_product = products.find().sort("total_sold", -1).limit(1)
for p in top_product:
    print(p)

# =================================================
# 7️⃣ USERS WITH MOST ORDERS
# =================================================

print("\n--- Users With Most Orders ---")
pipeline = [
    {"$group": {"_id": "$user_id", "order_count": {"$sum": 1}}},
    {"$sort": {"order_count": -1}}
]

for result in orders.aggregate(pipeline):
    user = users.find_one({"_id": result["_id"]})
    print({
        "name": user["name"],
        "order_count": result["order_count"]
    })

print("\n----- CASE STUDY COMPLETED -----")