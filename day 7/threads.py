# import threading

# def say_hello():
#     print("Hello from thread")
# t = threading.Thread(target=say_hello)
# t.start()
# t.join()

# print("task finished")

# import time
# def task():
#     print("task started")
#     time.sleep(2)
#     print("task completed")
# task()
# print("program finished")


# import threading
# def greet(name):
#     print(f"hello.{name}")
    
# t=threading.Thread(target=greet,args=("Alice",))
# t.start()

# def greet(name):
#     print(f"hello.{name}")

# greet("Alice")
# import threading
# import time
# def worker(num):
#     print(f"worker {num} is running")
#     time.sleep(2)
#     print(f"worker {num} is stoped")
    
# for i in range(5):
#     t=threading.Thread(target=worker,args=(i,))
#     t.start()
# import urllib.request
# import threading
# import urllib.request

# def download_file():
#     url = 'http://localhost:5500/jk.txt'
#     file_name = "test.txt"
#     print("starting the downloading of file")
#     urllib.request.urlretrieve(url, 'file_name')
#     print("completed the downloading of file")

# t = threading.Thread(target=download_file)
# t.start()
# print("main thread continuous execution")

# import urllib.request
# import threading
# import urllib.request

# def download_file():
#     url = 'http://localhost:5500/jk.txt'
#     file_name = "test.txt"
#     print("starting the downloading of file")
#     urllib.request.urlretrieve(url, 'file_name')
#     print("completed the downloading of file")

# download_file()
# print("main thread continuous execution")

# import ssl
# import json

# import time 
# import threading
# import requests
# import json

# def download_file():
#     url = "https://fakestoreapi.com/products/1"
#     file = "posts.json"

#     time.sleep(1)
#     response = requests.get(url)
#     posts = response.json()   
#     with open(file, "w") as f:
#         json.dump(posts, f, indent=5)
#     print("Download complete!")

# t1 = threading.Thread(target=download_file)
# t1.start()

# print("Main thread continues to run while download is in progress.")
# import urllib.request
# import threading
# import time
# import json
# import ssl
# def download_json():
#     try:
#         print("connecting to api..")
#         time.sleep(2)
#         url="https://fakestoreapi.com/products"
#         headers={
#             "User-Agent": "Mozilla/5.0"
#         }
#         req=urllib.request.Request(url, headers=headers)
#         context=ssl._create_unverified_context()
#         with urllib.request.urlopen(req, context=context) as response:
#             data=response.read()
#         print("Data downloaded")
#         posts=json.loads(data)
#         with open('posts.json','w')as f:
#             json.dump(posts,f,indent=4)
#         print("starting download complete")
#     except Exception as e:
#         print("Error:", e)
# t=threading.Thread(target=download_json)
# t.start()
# print("Main thread continues execution")


#Without threading
import urllib.request
import time
import json
import ssl

def download_json():
    try:
        print("connecting to api..")
        time.sleep(2)
        url="https://fakestoreapi.com/products"
        headers={"User-Agent":"Mozilla/5.0"}
        req=urllib.request.Request(url,headers=headers)
        context=ssl._create_unverified_context()
        with urllib.request.urlopen(req,context=context) as response:
            data=response.read()
        print("Data downloaded")
        posts=json.loads(data)
        with open('posts.json','w') as f:
            json.dump(posts,f,indent=4)
        print("starting download complete")
    except Exception as e:
        print("Error:",e)

download_json()
print("Main thread continues execution")