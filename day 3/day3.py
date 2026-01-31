# Demonstration of list functions in Python

my_list = [10, 20, 30, 40, 20]
print("Initial List:", my_list)

my_list.append(50)
print("After append(50):", my_list)

my_list.insert(2, 25)
print("After insert(2, 25):", my_list)

my_list.extend([60, 70])
print("After extend([60, 70]):", my_list)

my_list.remove(20)
print("After remove(20):", my_list)

removed_element = my_list.pop()
print("After pop():", my_list)
print("Popped element:", removed_element)

print("Index of 30:", my_list.index(30))

print("Count of 20:", my_list.count(20))

my_list.sort()
print("After sort():", my_list)

my_list.reverse()
print("After reverse():", my_list)

print("Length of list:", len(my_list))
my_list.clear()
print("After clear():", my_list)


my_list = [10, 20, 30, 40, 20]
print(my_list[2])
my_list[2]=25
print(my_list[2])
#slicing
num=[10,20,50,40,6,104,8,6]
print(num[0:4])
print(num[-2:])
for n in num:
    print(n)

lst2=["sravani","kid","little","hello"]
if "kid" in lst2:
    print("yes kid is present in list")
 
lst2[1]="pranitha"
print(lst2)

order_summary=["pizza",2,600.00,True]
print(order_summary)
#index of each item in the list
for index,item in enumerate(order_summary):
    print(f"index:{index},item:{item}")



#tuples
tpl=("apple","guava","pomagranate","strawberry")
print(tpl)
print(tpl[2])
trip_summary=("uber","pomdicherry","chennai",3500.20,3500.20)
for item in trip_summary:
    print(item) 
print(len(trip_summary))
print(trip_summary)



#dictionary

mydict={"key1":"value1","key2":"value2"}
print(type(mydict))

trip={
    "provider":"uber",
    "source":"pondicherry",
    "destination":"chennai"
    #"distance":"55KM"
}
print(trip["provider"])#finding the value using key
print(trip.get("provider"))
print(trip.keys())
print(trip.values())

for key,value in trip.items():
    print(f"keys:{key},values:{value}")
#update and pop
trip["source"]="goa"
print(trip)

trip.pop("source")
print(trip)
for key in trip:
    print(key,"->",trip[key])
    
#set is an unordered collection

st={1,2,9,4,5,6,6}
print(st)

uber_cities={"chennai","hyderabad","bombay","goa"}
uber_cities2={"mumbai","chennai","karnataka"}
print(uber_cities)
uber_cities.add("delhi")
print(uber_cities)
lst_cities=list(uber_cities)
print(type(lst_cities))
print(uber_cities.union(uber_cities2))
print(uber_cities.intersection(uber_cities2))
print(uber_cities.difference(uber_cities2))

uber_cities.add("pune")
print(uber_cities)
uber_cities.remove("pune")
print(uber_cities)

#lambda function

add=lambda a ,b:a+b
print(add(8,9))
num=[1,2,3,4,5,6,7,8]
e_num=list(filter(lambda x:x%2==0,num))
print(e_num)

data=[
    {
        "name":"alice","age":30
    },
    { "name":"bob","age":10 }
]
youngest=min(data,key=lambda x:x["age"]<30)
print(youngest)

