error_lines = []
with open("app.log", "r") as log:
    for line in log:
        if "ERROR" in line:
            error_lines.append(line)
with open("error_log.txt", "w") as error_file:
    error_file.writelines(error_lines)
print("Error messages extracted successfully.")