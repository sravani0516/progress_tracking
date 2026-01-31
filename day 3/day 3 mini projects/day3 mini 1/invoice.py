from datetime import datetime

def generate_invoice(customer, ride):
    with open("all_invoices.txt", "a", encoding="utf-8") as file:
        file.write("\n-------- UBER RIDE INVOICE --------\n")
        file.write(f"Date & Time  : {datetime.now()}\n")
        file.write(f"Customer    : {customer['name']}\n")
        file.write(f"Phone No    : {customer['phone']}\n")
        file.write(f"Source      : {ride['source']}\n")
        file.write(f"Destination : {ride['destination']}\n")
        file.write(f"Vehicle     : {ride['vehicle']}\n")
        file.write(f"Driver      : {ride['driver']}\n")
        file.write(f"Distance    : {ride['distance']} km\n")
        file.write(f"Fare        : ₹{ride['fare']}\n")
        file.write("Ride Status : Completed\n")
        if 'feedback_rating' in ride:
            file.write(f"Feedback Rating : {ride['feedback_rating']}\n")
        if 'feedback_comment' in ride:
            file.write(f"Comments        : {ride['feedback_comment']}\n")
        file.write("----------------------------------\n")
