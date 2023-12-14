import json
import csv
from datetime import datetime
import os
from typing import Dict

def handle_null(value):
    if value is None or value == "null":
        return None
    return value

def convert(json_data:Dict, csv_file:str):
    # print(json_data)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(['Timestamp', 'Value'])
        
        # Write data to CSV file
        for key, value in json_data.items():
            if value== None:
                writer.writerow([key, "None"])
            else:
                writer.writerow([key, value])

    print(f"Data has been converted and saved to {csv_file}")


files = os.listdir("C:/Users/Prarabdha/Desktop/projects/se_mini_project/data")

for file in files:
    json_file = f"data/{file}"
    data = {}
    with open(json_file, 'r') as f:
    # Load the JSON data into a dictionary
        raw_data = json.load(f)
    
    # print(raw_data)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(file)
    for key, values in raw_data.items():
        data[int(key)] = values

    print(data)
    # Handle 'None' values if needed
    # for key,value in raw_data.items():
    #     data[key] = handle_null(value)
    # data = {key: handle_null(value) for key, value in raw_data.items()}
    
    # print(data)  
    

    convert(data, f"data_csv/{file[:-5]}.csv")





