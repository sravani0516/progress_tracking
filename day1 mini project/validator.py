email=input("enter the email")
password=input("enter the password")
name=input("enter your name")
#age=int(input("enter your age"))
if "@" not in email:
    print("invalid email")
elif len(password)<6:
    print("password is too short")
elif (name.isalpha())!=True:
    print("name must contain only alphabets only")
else:
    print("password submitted successfully")
    
    