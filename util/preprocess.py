import csv
import numpy as np
from datetime import datetime
# with open("track.csv", 'r') as file:
# 	csv_file = csv.DictReader(file)
# 	for row in csv_file:
# 		row['url']
# 		try:
# 			'''count of visit of a paticular url'''	
# 			l=datetime.fromtimestamp(float(int(row['last_visit_date'])//1000000))
# 		except ValueError:
# 			pass   
reader = csv.reader(open("track.csv"))
sortedlist = sorted(reader, key=lambda row: row[4], reverse=True)

csv_file = csv.DictReader(open("track.csv"))

for row in csv_file:
    print(row['id'])
    if row['id']=='11989':
        print(row['url'])



print(sortedlist[1])

'''id,url,title,rev_host,visit_count,hidden,
typed,frecency,last_visit_date,guid,foreign_count,url_hash,description,preview_image_url,origin_id'''

reader = csv.reader(open("track1.csv"))
sortedlist1 = sorted(reader, key=lambda row: row[3], reverse=True)

'''id,from_visit,place_id,visit_date,visit_type,session'''

print(sortedlist1[1])

