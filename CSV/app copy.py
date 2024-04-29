import csv

def find_identity(file_name, number):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['FILENAME']) == number:
                return row['IDENTITY']
        return None

file_name = 'numbers.csv'  # Replace 'your_csv_file.csv' with the path to your CSV file
number = 0
while True:
    try:
        identity = find_identity(file_name, number)
        if identity:
            print(identity)
        else:
            print("Number not found in the file.")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != 'yes':
            break
