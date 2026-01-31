import functions

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
    

bill_amt=functions.total(*lst)

user=functions.profile_generator(NAME=name,AGE=age,LOCATION=trip_location,E_MAIL=email,PHONE_NUMBER=phone_no,TOTAL_BILL=bill_amt)
for i in user:
    print(i)