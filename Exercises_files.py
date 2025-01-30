import csv 

file_Path: str = "example.csv"
data_csv: list = []

with open(file_Path, mode='r', encoding='utf-8') as file:
  # Create a object to read cvs
  read_csv = csv.DictReader(file)

  for line in read_csv:
    data_csv.append(line)
  
print(data_csv)



