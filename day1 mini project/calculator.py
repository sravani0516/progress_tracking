def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def dev(a,b):
    return a/b
def modulo(a,b):
    return a%b

print("Enter 1-- for addition    2--for subtraction   3--multiplication  4-- for devision   5--for modulo")
choice=int(input("enter the operation that you wanted to perform "))
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
if choice==1:
    ans=add(a,b)
    print(ans)
elif choice==2: 
     ans=sub(a,b)
     print(ans)
elif choice==3: 
     ans=mul(a,b)
     print(ans)
elif choice==4: 
     ans=dev(a,b)
     print(ans)
else : 
     ans=modulo(a,b)
     print(ans)
    