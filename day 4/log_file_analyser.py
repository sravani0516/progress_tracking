import re

log_file = "sample.log"
report_file = "log_report.txt"

error_count = 0
warning_count = 0
info_count = 0

with open(log_file, "r") as file:
    for line in file:
        if re.search(r"ERROR", line):
            error_count += 1
        elif re.search(r"WARNING", line):
            warning_count += 1
        elif re.search(r"INFO", line):
            info_count += 1

print("LOG FILE ANALYSIS")
print("------------------")
print(f"ERROR count   : {error_count}")
print(f"WARNING count : {warning_count}")
print(f"INFO count    : {info_count}")

with open(report_file, "w") as report:
    report.write("LOG FILE ANALYSIS\n")
    report.write("------------------\n")
    report.write(f"ERROR count   : {error_count}\n")
    report.write(f"WARNING count : {warning_count}\n")
    report.write(f"INFO count    : {info_count}\n")

print("\nAnalysis saved to log_report.txt")
