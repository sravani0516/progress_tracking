import shutil
import os
from datetime import datetime
import subprocess
import sys

source_file = "source_file.txt"

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_file = f"backup_{timestamp}.txt"

shutil.copy2(source_file, backup_file)

task_name = "DailyFileBackup9AM"
python_path = sys.executable
script_path = os.path.abspath(__file__)

command = f'schtasks /create /sc daily /st 10:53 /tn "{task_name}" /tr "\\"{python_path}\\" \\"{script_path}\\"" /f'

subprocess.run(command, shell=True)

print("Backup done and daily 9:00 AM task created successfully")
