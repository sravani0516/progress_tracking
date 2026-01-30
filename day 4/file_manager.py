import os
import shutil

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        return

    # Define file categories and their extensions
    extensions = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
        "Archives": [".zip", ".rar", ".7z", ".tar"],
        "Programs": [".exe", ".msi"],
        "Media": [".mp3", ".mp4", ".wav", ".mkv"]
    }

    report = f"--- File Management Report for: {folder_path} ---\n"
    moved_count = 0

    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                file_ext = os.path.splitext(filename)[1].lower()
                
                for category, exts in extensions.items():
                    if file_ext in exts:
                        # Create category folder if it doesn't exist
                        category_path = os.path.join(folder_path, category)
                        os.makedirs(category_path, exist_ok=True)
                        
                        # Move the file
                        shutil.move(file_path, os.path.join(category_path, filename))
                        report += f"Moved: {filename} -> {category}/\n"
                        moved_count += 1
                        break
        
        if moved_count == 0:
            report += "No files needed organizing.\n"
        
        report += f"Total files organized: {moved_count}\n"
        report += "Cleaned up text too\n"

    except Exception as e:
        report += f"Management Error: {e}\n"

    # Print to console and append to results.txt
    print(report.strip())
    with open('results.txt', 'a') as f:
        f.write(report + "\n")

if __name__ == "__main__":
    # Specify the folder you want to tidy up (e.g., Downloads)
    target = r"filess" 
    organize_files(target)