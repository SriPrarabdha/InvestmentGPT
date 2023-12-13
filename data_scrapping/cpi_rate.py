import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datetime
import math
from typing import List, Dict
import json
import seaborn as sns
sns.set_style("white")

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
    # print(list_dict[0].values())
    # print(list_dict[1].values())
    print(list_dict[2])
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

def imputer(d: dict):
    keys = list(d.keys())
    values = list(d.values())

    prev_valid = float('nan')  # Store the previous valid value

    for index, key in enumerate(keys):
        if math.isnan(values[index]):
            if index == 0:
                # If the first value is NaN, replace it with the mean of non-NaN values
                non_nan_values = [val for val in values if not math.isnan(val)]
                mean = sum(non_nan_values) / len(non_nan_values) if non_nan_values else float('nan')
                d[key] = mean
            else:
                # Impute the NaN value with the previous valid value
                d[key] = prev_valid
        else:
            # Update prev_valid with the current valid value
            prev_valid = values[index]

    # Print the mean of non-NaN values after imputation
    non_nan_values = [val for val in values if not math.isnan(val)]
    mean = sum(non_nan_values) / len(non_nan_values)
    print("Mean of non-NaN values after imputation:", mean)

    return d

Fruits_cpi_data = imputer(Fruits[2])
Vegetables_cpi_data = imputer(Vegetables[2])
Oils_fats_cpi_data = imputer(Oils_fats[2])
Milk_products_cpi_data = imputer(Milk_products[2])
Meat_fish_cpi_data = imputer(Meat_fish[2])
Cereals_products_cpi_data = imputer(Cereals_products[2])
Spices_cpi_data = imputer(Spices[2])
Recreation_amusement_cpi_data = imputer(Recreation_amusement[2]) 
Sugar_Confectionery_cpi_data = imputer(Sugar_Confectionery[2])
Pulses_products_cpi_data = imputer(Pulses_products[2])
Prepared_meals_snacks_cpi_data = imputer(Prepared_meals_snacks[2])
Food_beverages_cpi_data = imputer(Food_beverages[2])
Non_alcoholic_beverages_cpi_data = imputer(Non_alcoholic_beverages[2])
Pan_tobacco_intoxicants_cpi_data = imputer(Pan_tobacco_intoxicants[2])
personal_care_cpi_data = imputer(personal_care[2])
Miscellaneous_cpi_data = imputer(Miscellaneous[2])
general_index_cpi_data = imputer(general_index[2])
Footwear_cpi_data = imputer(Footwear[2])
Clothing_cpi_data = imputer(Clothing[2])
Housing_cpi_data = imputer(Housing[2])
fuel_light_cpi_data = imputer(fuel_light[2])
health_cpi_data = imputer(health[2])
good_n_service_cpi_data = imputer(good_n_service[2])
Education_cpi_data = imputer(Education[2])
transport_n_communication_cpi_data = imputer(transport_n_communication[2])


def get_all_dates(start_year: int, end_year: int, start_month: int, end_month: int):
    all_dates = []

    for year in range(start_year, end_year + 1):
        # Define start and end months for each year to iterate
        if year == start_year:
            start_m = start_month
        else:
            start_m = 1
        
        if year == end_year:
            end_m = end_month
        else:
            end_m = 12
        
        for month in range(start_m, end_m + 1):
            if month == 12 and year != end_year:
                days_in_month = (datetime.datetime(year + 1, 1, 1) - datetime.datetime(year, month, 1)).days
            else:
                days_in_month = (datetime.datetime(year, month % 12 + 1, 1) - datetime.datetime(year, month, 1)).days
            
            for day in range(1, days_in_month + 1):
                all_dates.append(datetime.datetime(year, month, day).date())

    return all_dates
    # print(all_dates)


def get_complete_data(data:Dict, name:str):
    keys = list(data.keys())
    all_dates = get_all_dates(keys[0].year, keys[-1].year, keys[0].month, keys[-1].month)
    print("*****************************************************************")
    print(all_dates)

    data_new = {}

    for i in all_dates:
        if i in data.keys():
            data_new[i] = data[i]
        else:
            data_new[i] = math.inf

    # print(repo_rates_data)

    val = list(data.values())[0]
    for i in range(len(all_dates)):
        if data_new[all_dates[i]] ==  math.inf:
            data_new[all_dates[i]] = val
        else:
            val = data_new[all_dates[i]]

    print(data_new)

    # converted_dict = {int(datetime.datetime.combine(key, datetime.datetime.min.time()).timestamp()): value for key, value in data_new.items()}

    # with open(f"data2/{name}.json", 'w') as file:
    #     json.dump(converted_dict, file)

    return data_new


transport_n_communication_cpi_data = get_complete_data(transport_n_communication_cpi_data, "transport_n_communication_cpi_data")
Education_cpi_data = get_complete_data(Education_cpi_data, "Education_cpi_data")
good_n_service_cpi_data = get_complete_data(good_n_service_cpi_data, "good_n_service_cpi_data")
health_data = get_complete_data(health_cpi_data, "health_data")
Clothing_cpi_data = get_complete_data(Clothing_cpi_data, "Clothing_cpi_data")
Footwear_cpi_data = get_complete_data(Footwear_cpi_data, "Footwear_cpi_data")
general_index_cpi_data = get_complete_data(general_index_cpi_data, "general_index_cpi_data")
# Miscellaneous_cpi_data = get_complete_data(Miscellaneous_cpi_data, "Miscellaneous_cpi_data")
# get_complete_data(personal_care_cpi_data, "personal_care_cpi_data")
# get_complete_data(Pan_tobacco_intoxicants_cpi_data, "Pan_tobacco_intoxicants_cpi_data")
# get_complete_data(Non_alcoholic_beverages_cpi_data, "Non_alcoholic_beverages_cpi_data")
# get_complete_data(Food_beverages_cpi_data, "Food_beverages_cpi_data")
# get_complete_data(Prepared_meals_snacks_cpi_data, "Prepared_meals_snacks_cpi_data")
# get_complete_data(Pulses_products_cpi_data, "Pulses_products_cpi_data")
# get_complete_data(Sugar_Confectionery_cpi_data, "Sugar_Confectionery_cpi_data")
# get_complete_data(Recreation_amusement_cpi_data, "Recreation_amusement_cpi_data")
# get_complete_data(Spices_cpi_data, "Spices_cpi_data")
# get_complete_data(Cereals_products_cpi_data, "Cereals_products_cpi_data")
# get_complete_data(Meat_fish_cpi_data, "Meat_fish_cpi_data")
# get_complete_data(Milk_products_cpi_data, "Milk_products_cpi_data")
# get_complete_data(Oils_fats_cpi_data, "Oils_fats_cpi_data")
# get_complete_data(Fruits_cpi_data, "Fruits_cpi_data")
# get_complete_data(Vegetables_cpi_data, "Vegetables_cpi_data")
# get_complete_data(fuel_light_cpi_data, "fuel_light_cpi_data")
# get_complete_data(Housing_cpi_data, "Housing_cpi_data")


fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot()

ax.plot(list(general_index_cpi_data.keys()),list(general_index_cpi_data.values()), lw=2,color='black')
ax.plot(list(transport_n_communication_cpi_data.keys()),list(transport_n_communication_cpi_data.values()) , lw=2,color='pink')
ax.plot(list(Education_cpi_data.keys()),list(Education_cpi_data.values()),  lw=2,color='red')
ax.plot(list(good_n_service_cpi_data.keys()),list(good_n_service_cpi_data.values()),  lw=2,color='grey')
ax.plot(list(health_data.keys()), list(health_data.values()),color='green')
ax.plot(list(Clothing_cpi_data.keys()),list(Clothing_cpi_data.values()), lw=2,color='blue')
ax.plot(list(Footwear_cpi_data.keys()),list(Footwear_cpi_data.values()), lw=2,color='orange')         

ax.set_title('Indian Markets CPI Rates')
plt.legend(labels=['Overall CPI Rate','Transport & Communication Sector','Education Sector','General Goods & Service','Health Sector','Clothing Sector','Footwear Sector'])


ax.set_yticks(np.arange(100, 180, 2))
plt.grid()

# ax.set_xlim([10000, 19300])
# ax.set_ylim([0, 400]) 
ax.secondary_yaxis("left")
print("work")
plt.savefig('cpi.png')