from multiprocessing import Process,pool
import time
# def worker():
#     print("Worker is running")

# if __name__ == "__main__":
#     p=Process(target=worker)
#     p.start()
#     p.join()
#     print("Main Process finished")


import time
from multiprocessing import Pool,Queue

# def square(n):
#     return n * n

# if __name__ == "__main__":
#     numbers = [10**7, 10**2, 10**3, 10**4, 10**5]

#     start = time.time()
#     with Pool() as p:
#         results = p.map(square, numbers)
#     end = time.time()

#     print("Results:", results)
#     print("Time taken:", end - start)

def worker(q):
    q.put('hello')
if __name__ == "__main__":
    q=Queue()
    p=Process(target=worker,args=(q,))
    p.start()
    p.join()
    result=q.get()
    print("Result from worker:",result)



    

    
