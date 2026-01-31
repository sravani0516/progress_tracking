import random

def assign_driver(*drivers):
    return random.choice(drivers)

def create_ride(**kwargs):
    return kwargs

def get_distance(source, destination, distance_map):
    return distance_map.get((source, destination), 10)  
def calculate_fare(distance, rate):
    return distance * rate
