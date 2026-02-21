from multiprocessing import Pool
import time

def analyzie_logs(chunk):
    print(f"analyzing chunk for  {chunk}...")
    time.sleep(2)  # Simulate time taken to compute
    return f"chunk {chunk} analyzed"

if __name__ == "__main__":
    chunks = [1, 2, 3, 4]

    with Pool(4) as p:
        results = p.map(analyzie_logs, chunks)

    print(results)

    
