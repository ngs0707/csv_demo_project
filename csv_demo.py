import csv

# CSV file name (relative path in the project folder)
csv_file = 'countries.csv'

# Header and data
header = ['Country Name', 'Capital City', 'Population']
data = [
    ['UK', 'LONDON', 67736802],
    ['USA', 'WASHINGTON', 339996563],
    ['UAE', 'DUBAI', 9516871]
]

# Write CSV file
with open(csv_file, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)       # Write header
    writer.writerows(data)        # Write data

print(f"{csv_file} written successfully!")

# Read and display CSV content
with open(csv_file, mode='r', encoding='UTF8') as file:
    csv_reader = csv.reader(file)
    print("\nCSV Content:")
    for row in csv_reader:
        print(row)
