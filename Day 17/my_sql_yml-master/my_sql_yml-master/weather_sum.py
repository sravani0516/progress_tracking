from multiprocessing import Pool
import time

def simulate_region(region):
    print(f"Calculating weather sum for {region}...")
    time.sleep(2)  # Simulate time taken to compute
    return f"region {region} complete"

if __name__ == "__main__":
    regions = ['North', 'South', 'East', 'West']

    with Pool(processes=4) as p:
        results = p.map(simulate_region, regions)

    print(results)
