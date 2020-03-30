import csv
with open("track.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(row['last_visit_date'])
