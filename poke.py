import urllib.request
import os
import csv
import re

names = []
# Open file 
with open('names1.csv') as file_obj:
      
    # Create reader object by passing the file 
    # object to reader method
    reader_obj = csv.reader(file_obj)
      
    # Iterate over each row in the csv 
    # file using reader object
    for row in reader_obj:
        name = row[1]
        pattern = r'[^A-Za-z0-9]+'
        name = re.sub(pattern, '', name)
        names.append(name)


for x in range(1, 899):
    url = f"https://poketwo.s3.object1.us-east-1.tswcloud.com/data/images/{x}.png"
    file = f"Pictures/{names[x-1]}.png"

    urllib.request.urlretrieve(url, file)

    print(f"{file} download successful")
