import os

old_file = r"C:\Users\gsrav\OneDrive\Desktop\day 4\important_file.txt"
new_file = os.path.join(os.path.dirname(old_file), "renamed_file.txt")
os.rename(old_file, new_file)

print("File renamed successfully!")
