import pytest 

# def add(a,b):
#     return a+b

def sub(a,b):
    return a-b

def multipuly(a,b):
    return a*b

def division(a,b):
    return a/b
def division(a,b):
    if b==0:
        raise ValueError("cant devide")
    return a/b

class calccc:
    def add(self,a,b):
        return a+b