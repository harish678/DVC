import csv
import dvc.api

with dvc.api.open(
    path="./iris.csv",
    repo="https://github.com/jbrownlee/Datasets"
) as file:
    reader = csv.reader(file)

print(len(reader))