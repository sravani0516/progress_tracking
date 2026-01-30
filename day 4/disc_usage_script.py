import shutil

total, used, free = shutil.disk_usage("/")

tgb = total / (1024 ** 3)
ugb = used / (1024 ** 3)
fgb = free / (1024 ** 3)

print(f"Total Storage : {tgb:.2f} GB")
print(f"Used Storage  : {ugb:.2f} GB")
print(f"Free Space    : {fgb:.2f} GB")

pgb = (ugb / tgb) * 100
print(f"Used Percentage : {pgb:.2f} %")

with open("disc_usage.txt", "w") as file:
    file.write(f"Total Storage : {tgb:.2f} GB\n")
    file.write(f"Used Storage  : {ugb:.2f} GB\n")
    file.write(f"Free Space    : {fgb:.2f} GB\n")
    file.write(f"Used Percent  : {pgb:.2f} %\n")
