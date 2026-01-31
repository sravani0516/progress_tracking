class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name:{self.name},age: {self.age}")
        
s1=Student(name="john",age=12)
s1.display()

class Employee:
        
    def display(self,*args):
        self.id=id
        self.name=name
        self.department=department
        if len(args)==2:
            print(f"employee ID : {self.id}")
            print(f"employee Name : {self.name}")
        elif len(args)==1:
            print(f"employee department : {self.department}")


id=input("enter the employee id :")  
name=input("enter the employee name :")    
department=input("enter the employee department :")
s1=Employee()
s2=Employee()
s1.display(id,name)
s2.display(department)


                  
                  
#run time poly
class Animal:
    def sound(self):
        print("some generic sound")
        
class Cat(Animal):
    def sound(self):
        print("meowwwww")
class Dog(Animal):
    def sound(self):
        print("bowww")

#polymorphic behaviour
for animal in[Dog(),Cat()]:
    animal.sound()
    
#duck typing

class Pycharm:
    def execute(self):
        print("compiling + Running")
        
class VScode:
    def execute(self):
        print("Running + Linting")
        
def code(editor):
    editor.execute()
    
code(Pycharm())
code(VScode())

# inheritance
# single inheritance


class Father:
    def drive(self):
        print("father can drive")
class Son(Father):
    def play(self):
        print("son can play")
        
        
s=Son()
s.drive()
s.play()

# multi level inheritance
class Father:
    def drive(self):
        print("father can drive")
class Son(Father):
    def play(self):
        print("son can play")
        
class Gson(Son):
    def smile(self):
        print("Grand son can smile")
        
s=Gson()
s.drive()
s.play()
s.smile()

# heirarchial 
class Father:
    def drive(self):
        print("father can drive")
class Son(Father):
    def play(self):
        print("son can play")
        
class Daughter(Father):
    def smile(self):
        print("Daughter can dance")
  
  
s1=Son()      
s1.drive()  
s1.play()        
s=Daughter()
s.drive()
s.smile()

#multiple inheritance
class Father:
    def drive(self):
        print("father can drive")
class Mother:
    def cook(self):
        print("mom can cook")
        
class Daughter(Father,Mother):
    def dance(self):
        print("Daughter can dance")
  
         
s=Daughter()
s.drive()
s.cook()
s.dance()

#hybrid

class Father:
    def drive(self):
        print("father can drive")
class Son(Father):
    def play(self):
        print("son can play")
        
class Daughter(Father):
    def dance(self):
        print("Daughter can dance")
        
class Gson(Son,Daughter):
    def smile(self):
        print("Grand son can smile")
    
  
  
s=Gson()
s.drive()
s.play()
s.dance()
s.smile()

from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
        
class Car(Vehicle):
    def start_engine(self):
        print("hellloooooo")
s=Car()
s.start_engine()


# private, public and protected
class Parent:
    def __init__(self):
        self.public_var = "Public"
        self._protected_var = "Protected"
        self.__private_var = "Private"

    def access_from_same_class(self):
        print("Inside Parent class:")
        print("Public     :", self.public_var)
        print("Protected  :", self._protected_var)
        print("Private    :", self.__private_var)


class Child(Parent):
    def access_from_subclass(self):
        print("Inside Child class (Subclass):")
        print("Public     :", self.public_var)
        print("Protected  :", self._protected_var)

        print("Private    :", self._Parent__private_var)

c = Child()

c.access_from_same_class()
print()
c.access_from_subclass()

class Stranger:
    def access_from_other_class(self, obj):
        print("Inside Stranger class (Unrelated):")
        print("Public:", obj.public_var)
        print("Protected:", obj._protected_var)  # ⚠️ Not recommended
        try:
            print("Private:", obj.__private_var)
        except AttributeError:
            print("Private: ❌ Cannot access (AttributeError)")

