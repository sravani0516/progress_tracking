from data import vehicles, service_locations, locations_distance
from ride import assign_driver, create_ride, get_distance, calculate_fare
from invoice import generate_invoice
import time

print("------ Welcome to Uber App ------")

customer = {
    "name": input("Enter your name: "),
    "phone": input("Enter your phone number: ")
}

while True:
    print("\nAvailable Service Locations:")
    for loc in service_locations:
        print("-", loc)

    source = input("Select source location: ").title()
    destination = input("Select destination location: ").title()

    print("\nAvailable Vehicle Types:")
    for v in vehicles:
        print("-", v)
    vehicle = input("Select vehicle type: ").title()

    distance = get_distance(source, destination, locations_distance)
    rate = vehicles[vehicle]["rate"]
    fare = calculate_fare(distance, rate)

    driver = assign_driver(*vehicles[vehicle]["drivers"])

    print("\n Driver Assigned:", driver)
    time.sleep(2)
    print(" Ride Started...")
    time.sleep(3)
    print(" On the way...")
    time.sleep(4)
    print(" Ride Completed!")

    ride = create_ride(
        source=source,
        destination=destination,
        vehicle=vehicle,
        driver=driver,
        distance=distance,
        fare=fare
    )

    print("\n--- Ride Summary ---")
    print("Distance:", distance, "km")
    print("Total Fare: ₹", fare)

    print("\n--- Ride Feedback ---")
    rating = input("Rate your ride (1-5): ")
    comment = input("Any comments about your ride? ")

    ride['feedback_rating'] = rating
    ride['feedback_comment'] = comment

    generate_invoice(customer, ride)
    print("\nInvoice recorded in all_invoices.txt")

    another = input("\nDo you want to start another ride? (yes/no): ").lower()
    if another != "yes":
        print("\nThank you for using Uber App! Goodbye ")
        break
