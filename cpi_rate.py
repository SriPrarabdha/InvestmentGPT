import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datetime
import math


df = pd.read_csv("cpi.csv")

print(df.head())

print(df.columns)
columns = ['Sector', 'Year', 'Month', 'Cereals and products', 'Meat and fish','Egg', 'Milk and products', 'Oils and fats', 'Fruits', 'Vegetables','Pulses and products', 'Sugar and Confectionery', 'Spices','Non-alcoholic beverages', 'Prepared meals, snacks, sweets etc.','Food and beverages', 'Pan, tobacco and intoxicants', 'Clothing','Footwear', 'Clothing and footwear', 'Housing', 'Fuel and light','Household goods and services', 'Health', 'Transport and communication','Recreation and amusement', 'Education', 'Personal care and effects','Miscellaneous', 'General index']

# spelling_mistake = []
# print(df.iloc[44]['Month'])
df.loc[44, 'Month'] = 'March'

Fruits=[{},{},{}]
Vegetables=[{},{},{}]
Oils_fats=[{},{},{}]
Milk_products=[{},{},{}]
Meat_fish = [{},{},{}]
Cereals_products = [{},{},{}]
Spices=[{},{},{}]
Recreation_amusement = [{},{},{}] 
Sugar_Confectionery = [{},{},{}]
Pulses_products = [{},{},{}]
Prepared_meals_snacks = [{},{},{}]
Food_beverages = [{},{},{}]
Non_alcoholic_beverages = [{},{},{}]
Pan_tobacco_intoxicants = [{},{},{}]
personal_care = [{},{},{}]
Miscellaneous = [{},{},{}]
general_index =[{},{},{}]
Footwear = [{},{},{}]
Clothing = [{},{},{}]
Housing = [{},{},{}]
fuel_light = [{},{},{}]
health = [{},{},{}]
good_n_service = [{},{},{}]
Education = [{},{},{}]
transport_n_communication = [{},{},{}]

print(df.shape)
print(df.isnull().sum())
print(df.isna().sum())

mapping = {"Rural":0 , "Urban" : 1 , "Rural+Urban" : 2}

for index, row in df.iterrows():
    date_string = f"1 {row['Month']} {row['Year']}"
    date = datetime.datetime.strptime(date_string, "%d %B %Y").date()
    
    sector_map = mapping[row['Sector']]

    Fruits[sector_map][date] = row['Fruits'] 
    Vegetables[sector_map][date] = row['Vegetables']
    Oils_fats[sector_map][date] = row['Oils and fats']
    Milk_products[sector_map][date] = row['Milk and products']
    Meat_fish[sector_map][date] = row['Meat and fish']
    Cereals_products[sector_map][date] = row['Cereals and products']
    Spices[sector_map][date] = row['Spices']
    Recreation_amusement[sector_map][date] = row['Recreation and amusement']
    Sugar_Confectionery[sector_map][date] = row['Sugar and Confectionery']
    Pulses_products[sector_map][date] = row['Pulses and products']
    Prepared_meals_snacks[sector_map][date] = row['Prepared meals, snacks, sweets etc.']
    Food_beverages[sector_map][date] = row['Food and beverages']
    Non_alcoholic_beverages[sector_map][date] = row['Non-alcoholic beverages']
    Pan_tobacco_intoxicants[sector_map][date] = row['Pan, tobacco and intoxicants']
    personal_care[sector_map][date] = row['Personal care and effects']
    Miscellaneous[sector_map][date] = row['Miscellaneous']
    general_index[sector_map][date] = row['General index']
    Footwear[sector_map][date] = row['Footwear']
    Clothing[sector_map][date] = row['Clothing']
    health[sector_map][date] = row['Health']
    Housing[sector_map][date] = row['Housing']
    fuel_light[sector_map][date] = row['Fuel and light']
    good_n_service[sector_map][date] = row['Household goods and services']
    Education[sector_map][date] = row['Education']
    transport_n_communication[sector_map][date] = row['Transport and communication']
    

def printing(list_dict):
    print("lenghts ==== ", len(list_dict[0].values()), len(list_dict[1].values()) , len(list_dict[2].values()))

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(list_dict[0].values())
    print(list_dict[1].values())
    print(list_dict[2])
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

def imputer(d:dict):
    prev = d[list(d.keys())[0]]
    for index, key in d.keys():
        if d[key] == math.nan:
            if index == 0:
                d[key] = sum(list(d.values()))/len(d.values())
            else:
                d[key] = prev
                prev = d[key]

# print(spelling_mistake)
print(df.iloc[44]['Month'])

printing(Housing)
print("88************************************************************************")
printing(transport_n_communication)

start_year = 2013
end_year = 2020

all_dates = []

for year in range(start_year, end_year + 1):
    for month in range(1, 13):
        if month==12:
            days_in_month = (datetime.datetime(year+1, 1, 1) - datetime.datetime(year, month, 1)).days
        else:    
            days_in_month = (datetime.datetime(year, month % 12 + 1, 1) - datetime.datetime(year, month % 12, 1)).days

        for day in range(1, days_in_month + 1):
            all_dates.append(datetime.date(year, month, day))

# print(all_dates)

lending_rates_data = {}

for i in all_dates:
    if i in lending_rates.keys():
        lending_rates_data[i] = lending_rates[i]
    else:
        lending_rates_data[i] = 0

# print(repo_rates_data)

val = 17.0
for i in range(len(all_dates)):
    if lending_rates_data[all_dates[i]] == 0:
        lending_rates_data[all_dates[i]] = val
    else:
        val = lending_rates_data[all_dates[i]]

print(lending_rates_data)
