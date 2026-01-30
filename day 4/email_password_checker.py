import re

email = input("Enter email: ")
password = input("Enter password: ")

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

length_pattern = r'.{8,}'
uppercase_pattern = r'[A-Z]'
lowercase_pattern = r'[a-z]'
digit_pattern = r'\d'
special_pattern = r'[!@#$%^&*(),.?":{}|<>]'

if re.match(email_pattern, email):
    print("Email is valid ✅")
else:
    print("Email is invalid ❌")

strength = 0

if re.search(length_pattern, password):
    strength += 1
if re.search(uppercase_pattern, password):
    strength += 1
if re.search(lowercase_pattern, password):
    strength += 1
if re.search(digit_pattern, password):
    strength += 1
if re.search(special_pattern, password):
    strength += 1

if strength == 5:
    print("Password strength: Strong 💪")
elif strength >= 3:
    print("Password strength: Medium 🙂")
else:
    print("Password strength: Weak ⚠️")
