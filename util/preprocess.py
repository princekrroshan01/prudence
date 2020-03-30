import csv
from datetime import datetime
with open("track.csv", 'r') as file:
	csv_file = csv.DictReader(file)
	for row in csv_file:
		try:
			l=datetime.fromtimestamp(float(int(row['last_visit_date'])//1000000))
		except ValueError:
			pass   

