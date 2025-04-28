import csv

# Threshold define karo
threshold = 80

# CSV file ka naam
csv_file = 'students.csv'

# File ko read karo
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    
    print(f"Students with grade above {threshold}:")
    for row in reader:
        if int(row['grade']) > threshold:
            print(row['name'])
