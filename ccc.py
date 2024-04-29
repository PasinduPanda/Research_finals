import csv

# Define the file name
file_name = 'example.csv'

# Define the data to be written to the CSV file
data = []

# Generate data for IDs 4 to 454
for i in range(1, 455):
    data.append({'ID': i, 'Character': 'අ'})

# Write the data to the CSV file
with open(file_name, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['ID', 'Name', 'Character'])
    writer.writeheader()
    writer.writerows(data)

print(f"Data has been written to '{file_name}' successfully.")
