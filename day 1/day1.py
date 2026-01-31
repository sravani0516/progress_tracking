import shutil
import os
import datetime
source="/Users/gsrav/OneDrive/Desktop/data & AI/BA 1.jpeg"
os.mkdir("/Users/gsrav/OneDrive/Desktop/data & AI/copyyy")
back=f"/Users/gsrav/OneDrive/Desktop/data & AI/aaa/data.backup_{datetime.date.today()}.jpeg"
shutil.copy(source,back)
print(f"back up of{source} created at {back}")


import sys
print("program name:", sys.argv[0])
for i in range (1,len(sys.argv)):
    print(f"arg {i}:",sys.argv[i])
    
    
#is a number prime or not using recursion
def is_prime_recursive(n, i=2):
    if n <= 1:
        return False
    if n == i:
        return True
    if n % i == 0:
        return False
    return is_prime_recursive(n, i + 1)
num1 = int(input("enter anumber"))
if is_prime_recursive(num1):
    print(f"{num1} is a prime number")
else:
    print(f"{num1} is not a prime number")



#files reading and writing

import os

filename = input("Enter the file name: ")

print("\nChoose an option:")
print("1. View file contents")
print("2. Add content to the file")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    if os.path.exists(filename):
        file = open(filename, "r")
        print("\nContents of the file:")
        print(file.read())
        file.close()
    else:
        print("\nFile does not exist.")

elif choice == 2:
    content = input("\nEnter the content to add into the file: ")
    file = open(filename, "a")   
    file.write(content + "\n")
    file.close()
    print("\nContent added successfully.")

else:
    print("\nInvalid choice.")
