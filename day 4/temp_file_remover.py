import os

folder_path = r"C:\Users\gsrav\OneDrive\Desktop\day 4\temp_files"

temp_extensions = [".tmp", ".temp", ".log", ".bak"]

deleted_files = 0
if os.path.exists(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        if os.path.isfile(file_path):
            for ext in temp_extensions:
                if file_name.lower().endswith(ext):
                    os.remove(file_path)
                    deleted_files += 1
                    break  

    print(f"Cleanup completed. {deleted_files} temp files removed.")
else:
    print("Folder not found:", folder_path)
