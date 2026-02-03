# def my_decorator(func):
#     def wrapper():
#         print("Before the func")
#         func()
#         print("After the func")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("Hello")
# say_hello()


#decorator with arguments
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("Before the func")
#         res=func(*args,**kwargs)
#         print("After the func")
#         return res
#     return wrapper
# @decorator
# def add(a,b):
#     return a+b
# print(add(11,8))

#decorator with parameters

# def repeat(n):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             for _ in range (n):
#                 func(*args,**kwargs)
#         return wrapper
#     return decorator

# @repeat(3)

# def greet():
#     print("heyyy")
    
# greet()

# class Mathutils:
#     @staticmethod
#     def add(a,b):
#         return a+b
    
    
# print(Mathutils.add(14,15))

# class Mathutils:
#     @staticmethod
#     def add(a,b):
#         return a+b
    
# ob=Mathutils()
# print(ob.add(14,15))

# def designation(func):
#     def wrapper():
#         print("designation: lawyer.")
#         func()
#     return wrapper
        


# def salary(func):
#     def wrapper():
#         print("salary : rs500000.")
#         func()
#     return wrapper
# @designation
# @salary
# def emp():
#     print("information")
    
# emp()
# login=True

# def login_info(func):
#     def wrapper():
#         if login:
#             print("Login successful")
#             #print("Salary: Rs 500000")
#             func()
#         else:
#             print("Login failed")
#     return wrapper


# @login_info
# def emp():
#     print("Employee Information")


# emp()
# registration details (change to test validation)
name = "Sravani"
username = "sravani123"
email = "sravani@gmail.com"

# login status
login = True


def validate_registration(func):
    def wrapper():
        if not name.isalpha():
            print("Invalid name")
            return

        if len(username) < 5:
            print("Invalid username")
            return

        if "@" not in email or "." not in email:
            print("Invalid email")
            return

        print("Registration validated successfully")
        func()
    return wrapper


def salary(func):
    def wrapper():
        if login:
            print("Login successful")
            print("Salary: Rs 500000")
            func()
        else:
            print("Login failed")
    return wrapper


@validate_registration
@salary
def emp():
    print("Employee Information")


emp()
