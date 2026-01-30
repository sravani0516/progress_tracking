import os  
servers = [
    "google.com",
    "8.8.8.8",
    "github.com",
    "localhost",
    "invalid.server"
]
for server in servers:
    response = os.system(f"ping -n 1 {server} > nul")  
    if response == 0:
        print(f"{server} is UP")
    else:
        print(f"{server} is DOWN")