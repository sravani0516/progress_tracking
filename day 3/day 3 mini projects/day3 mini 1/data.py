vehicles = {
    "Auto": {"rate": 10, "drivers": ["Ravi", "Kiran"]},
    "Bike": {"rate": 8, "drivers": ["Suresh", "Amit"]},
    "Car": {"rate": 15, "drivers": ["Rahul", "Vikas"]}
}

service_locations = [
    "Uppal",
    "MGBS",
    "JBS",
    "Secunderabad",
    "Medchal",
    "Kandlakoya"
]

locations_distance = {
    ("Uppal", "MGBS"): 14,
    ("MGBS", "Uppal"): 14,

    ("JBS", "Secunderabad"): 3,
    ("Secunderabad", "JBS"): 3,

    ("Secunderabad", "Medchal"): 25,
    ("Medchal", "Secunderabad"): 25,

    ("Medchal", "Kandlakoya"): 6,
    ("Kandlakoya", "Medchal"): 6,

    ("Uppal", "JBS"): 10,
    ("JBS", "Uppal"): 10
}
