import psutil
import shutil

cpu_usage = psutil.cpu_percent(interval=1)

memory = psutil.virtual_memory()
total_memory = memory.total / (1024 ** 3)
used_memory = memory.used / (1024 ** 3)
free_memory = memory.available / (1024 ** 3)

total, used, free = shutil.disk_usage("/")
total /= (1024 ** 3)
used /= (1024 ** 3)
free /= (1024 ** 3)

print("SYSTEM RESOURCE STATUS")
print("----------------------")
print(f"CPU Usage        : {cpu_usage:.2f} %")
print(f"Total Memory     : {total_memory:.2f} GB")
print(f"Used Memory      : {used_memory:.2f} GB")
print(f"Free Memory      : {free_memory:.2f} GB")
print(f"Total Disk       : {total:.2f} GB")
print(f"Used Disk        : {used:.2f} GB")
print(f"Free Disk        : {free:.2f} GB")

with open("system_usage.txt", "w") as file:
    file.write(f"CPU Usage        : {cpu_usage:.2f} %")
    file.write(f"Total Memory     : {total_memory:.2f} GB")
    file.write(f"Used Memory      : {used_memory:.2f} GB")
    file.write(f"Free Memory      : {free_memory:.2f} GB")
    file.write(f"Total Disk       : {total:.2f} GB")
    file.write(f"Used Disk        : {used:.2f} GB")
    file.write(f"Free Disk        : {free:.2f} GB")

