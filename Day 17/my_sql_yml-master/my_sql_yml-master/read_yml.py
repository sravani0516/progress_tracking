import yaml

with open("da.yml", "r") as file:
    data = yaml.safe_load(file)

print(data)
