import csv

def rename_values(file_name):
    # Define a mapping from old values to new values
    value_mapping = {'A': 'අ', 'B': 'ආ', 'C': 'ඇ', 'D': 'ඈ', 'E':'ඉ', 
}

    # Read the CSV file and replace values
    with open(file_name, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            new_row = {key: value_mapping.get(value, value) for key, value in row.items()}
            data.append(new_row)

    # Write the modified data back to the CSV file
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Values in '{file_name}' have been renamed successfully.")

# Specify the file name
file_name = r'C:\Users\DilThio\Desktop\reserach\OCR\OCR\version 2\numbers.csv'  # Replace 'your_csv_file.csv' with the path to your CSV file

# Call the function to rename values
rename_values(file_name)
