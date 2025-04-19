import csv

def create_csv():

    data = ['Emma Frost']
    
    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("CSV file 'output.csv' created successfully!")

create_csv()