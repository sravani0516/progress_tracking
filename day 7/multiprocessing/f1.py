from multiprocessing import Pool,Process
# import time

# def square(n):
#     return n * n

# if __name__ == "__main__":
#     numbers = [10**7, 10**2, 10**3, 10**4, 10**5]

#     start = time.time()
#     with Pool() as p:
#         p.map(square, numbers)
#     print("time taken:")
#     print(time.time() - start)
# from multiprocessing import Process
# def worker():
#     print("worker is running")

# if __name__ == "__main__":
#     p=Process(target=worker)
#     p.start()
#     p.join()
# #     print("main process finished")
# import time
# from multiprocessing import Pool
# def simulate_region(region):
#     print(f"calculating weather sum for {region}")
#     time.sleep(2)
#     return f"region {region} weather sum calculated"
# if __name__ == "__main__":
#     regions = ["north", "south", "east", "west"]
#     with Pool() as p:
#         results = p.map(simulate_region, regions)
#     print(results)

import time
from multiprocessing import Pool
def analyze_logs(chunk):
    print(f"analysing chunk for {chunk}")
    time.sleep(2)
    return f"chunk {chunk} analyzed"
if __name__ == "__main__":
    chunks=[1,2,3,4]
    with Pool(4) as p:
        results=p.map(analyze_logs,chunks)

    print(results)