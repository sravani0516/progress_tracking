#square star pattern

n=int(input("enter the number of rows and colomns"))
for i in range(n):
    for j in range(n):
        print("*",end='')
    print()
    
#pattern 2
n=int(input("enter the number of rows and colomns"))
for i in range(n):
    if i==0 or i==n-1:
        print("*" *n,)
    else:
        print("*" +" "*(n-2)+"*")
    #print()
    
#return only initial letters of a name 

full_name="Britto Anand"
a=full_name.split(" ")[1]
res=f"{full_name[0]}{a[0]}"
print(res)

another="".join([word[0].upper() for word in full_name.split()])
print(another)

#remove unwanted spaces in a string
dirty ="   killll     "
cleaned=dirty.strip()
print(cleaned)

#total number words in a string

greet="hey how do u do today"
count=len(greet.split())
print(count)

user_name=input("enter the user name")
password=input("enter the user password")
if user_name=="admin" and password=="1234":
    print("login successfull")
else:
    print("invalid username or password")
    
#student eligibility   
marks=int(input("enter the marks obtained"))
att=int(input("enter the attendance"))
if marks >=50 and att>=75:
    print("eligible for the exam")
else:
    print("not eligible for the exam")
    
    
#recharge discount
recharge=int(input("enter the recharge amount"))
data=int(input("enter the data to recharge in GB "))
if recharge >=399 and data >=2:
    print("eligible for extra 2GB data offer")
else:
    print("Sorry , you are eligible for extra 2GB data offer")

#bill calculation
bill=int(input("enter your bill amount"))
gold=input("are you a gold pass holding member yes/no").lower()
day=input("is it a weekend yes/no").lower()
if "yes" in gold:
    if bill>1000 and day=="yes":
        amt=bill*0.2
        print(f"you got a discount of {amt}, so you need to pay only {bill-amt}")
    else:
        print("no discount applied")
  
  
#password       
n=3
for i in range(n):
    password=input("enter the password")
    if password=="4561":
        print("login successful")
    elif i!=n-1:
        print("wrong password")
        print(f"you have only {n-i-1} chances to try the password")
    else:
        print("try later")

#add to cart using list
lst=[]
while True:
    item=input("enter the item which u need to add to ur cart")
    if item.lower()=="done":
        break
    lst.append(item)
print("cart iems are",lst)    


#functions
def greet():
    print("welcome to uber")
greet()
    
def greet(name):
    print(f"welcome to {name}")
greet("uber")

def greet(a,b):
    return a+b
greet(5,10)
    
#sending multiple args
def greet(*args):#this works as a tuple
    sum=0;
    for i in args:
        sum+=i
    return sum
greet(5,6,1,2,3)


#when we have multiple types of args
def print_data(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_data(name="sweety",marks=46)

#profile generator
f_name=input("enter your first name").strip()
l_name=input("enter your last name").strip()
age=int(input("enter your age"))
email=input("enter your e-mail").strip()
phone=int(input("enter your phone number"))
def profile_generator(**kwargs):
    lst=[]
    for key,value in kwargs.items():
        lst.append(f"{key}:{value}")
    return lst


user=profile_generator(FIRST_NAME=f_name,LAST_NAME=l_name,AGE=age,E_MAIL=email,PHONE_NUMBER=phone)
for i in user:
    print(i)
    
    
def greet(name="sravani"):
    print(f"welcome {name}")
greet()

def greet(name="sravani"):
    print(f"welcome {name}")
greet()
greet("sweety")

#profile and total bill 

def profile_generator(**kwargs):
    lst=[]
    for key,value in kwargs.items():
        lst.append(f"{key}:{value}")
    return lst


def total(*args):
    sum=0
    for i in args:
        sum+=i
    return sum


#personal details
name=input("enter your name").strip()
age=int(input("enter your age"))
trip_location=input("enter the trip location").strip()
phone=input("enter the phone number").strip()
phone_no=f"{phone[0:2]}******{phone[-2:]}"
email=input("enter the email")
lst=[]
n=int(input("enter the no.of bills you have spent"))
print("enter the each bill cost you have spent")

for i in range (n):
    lst.append(int(input()))
    

bill_amt=total(*lst)

user=profile_generator(NAME=name,AGE=age,LOCATION=trip_location,E_MAIL=email,PHONE_NUMBER=phone_no,TOTAL_BILL=bill_amt)
for i in user:
    print(i)