import csv

# Define the file name
file_name = 'example.csv'

# Define the data to be written to the CSV file
data = [
    {'ID': 1, 'Name': 'John', 'Character': 'අ'},
    {'ID': 2, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 3, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 4, 'Name': 'John', 'Character': 'අ'},
    {'ID': 5, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 6, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 7, 'Name': 'John', 'Character': 'අ'},
    {'ID': 8, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 9, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 10, 'Name': 'John', 'Character': 'අ'},
    {'ID': 11, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 12, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 13, 'Name': 'John', 'Character': 'අ'},
    {'ID': 14, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 15, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 16, 'Name': 'John', 'Character': 'අ'},
    {'ID': 17, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 18, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 19, 'Name': 'John', 'Character': 'අ'},
    {'ID': 20, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 21, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 22, 'Name': 'John', 'Character': 'අ'},
    {'ID': 23, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 24, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 25, 'Name': 'John', 'Character': 'අ'},
    {'ID': 26, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 27, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 28, 'Name': 'John', 'Character': 'අ'},
    {'ID': 29, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 30, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 31, 'Name': 'John', 'Character': 'අ'},
    {'ID': 32, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 33, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 34, 'Name': 'John', 'Character': 'අ'},
    {'ID': 35, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 36, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 37, 'Name': 'John', 'Character': 'අ'},
    {'ID': 38, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 39, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 40, 'Name': 'John', 'Character': 'අ'},
    {'ID': 41, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 42, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 43, 'Name': 'John', 'Character': 'අ'},
    {'ID': 44, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 45, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 46, 'Name': 'John', 'Character': 'අ'},
    {'ID': 47, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 48, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 49, 'Name': 'John', 'Character': 'අ'},
    {'ID': 50, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 51, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 52, 'Name': 'John', 'Character': 'අ'},
    {'ID': 53, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 54, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 55, 'Name': 'John', 'Character': 'අ'},
    {'ID': 56, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 57, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 58, 'Name': 'John', 'Character': 'අ'},
    {'ID': 59, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 60, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 61, 'Name': 'John', 'Character': 'අ'},
    {'ID': 62, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 63, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 64, 'Name': 'John', 'Character': 'අ'},
    {'ID': 65, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 66, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 67, 'Name': 'John', 'Character': 'අ'},
    {'ID': 68, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 69, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 70, 'Name': 'John', 'Character': 'අ'},
    {'ID': 71, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 72, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 73, 'Name': 'John', 'Character': 'අ'},
    {'ID': 74, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 75, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 76, 'Name': 'John', 'Character': 'අ'},
    {'ID': 77, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 78, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 79, 'Name': 'John', 'Character': 'අ'},
    {'ID': 80, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 81, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 82, 'Name': 'John', 'Character': 'අ'},
    {'ID': 83, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 84, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 85, 'Name': 'John', 'Character': 'අ'},
    {'ID': 86, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 87, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 88, 'Name': 'John', 'Character': 'අ'},
    {'ID': 89, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 90, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 91, 'Name': 'John', 'Character': 'අ'},
    {'ID': 92, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 93, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 94, 'Name': 'John', 'Character': 'අ'},
    {'ID': 95, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 96, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 97, 'Name': 'John', 'Character': 'අ'},
    {'ID': 98, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 99, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 100, 'Name': 'John', 'Character': 'අ'},
    {'ID': 101, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 102, 'Name': 'Doe', 'Character': 'අ'}
    {'ID': 103, 'Name': 'John', 'Character': 'අ'},
    {'ID': 104, 'Name': 'Jane', 'Character': 'අ'},
    {'ID': 105, 'Name': 'Doe', 'Character': 'අ'}
    
]

# Write the data to the CSV file
with open(file_name, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['ID', 'Name', 'Character'])
    writer.writeheader()
    writer.writerows(data)

print(f"Data has been written to '{file_name}' successfully.")
