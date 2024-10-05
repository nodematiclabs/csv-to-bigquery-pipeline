import csv
import random
from datetime import datetime, timedelta

def generate_data(num_rows):
    data = []
    start_date = datetime(2024, 1, 1)
    
    for _ in range(num_rows):
        date = start_date + timedelta(days=random.randint(0, 365))
        name = f"Person{random.randint(1, 100)}"
        age = random.randint(18, 80)
        salary = round(random.uniform(30000, 100000), 2)
        
        data.append([date.strftime("%Y-%m-%d"), name, age, salary])
    
    return data

def write_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Name', 'Age', 'Salary'])
        writer.writerows(data)

# Generate and write data
num_rows = 10000
filename = 'data.csv'
data = generate_data(num_rows)
write_csv(filename, data)

print(f"Generated {num_rows} rows of data in {filename}")