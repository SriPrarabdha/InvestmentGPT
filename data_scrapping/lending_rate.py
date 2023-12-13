#Lending Rate

import datetime
import matplotlib.pyplot as plt
import plotly.graph_objects as go

lending_rates_raw = {"15.06.2023" : "14.85",
"15.03.2023" : "14.85",
"15.12.2022" : "14.15",
"15.09.2022" : "13.45",
"15.06.2022" : "12.75",
"15.03.2022" : "12.30",
"15.12.2021" : "12.30",
"15.09.2021" : "12.20",
"15.06.2021" : "12.25",
"10.03.2021" : "12.15",
"10.12.2020" : "12.05",
"10.09.2020" : "12.15",
"10.06.2020" : "12.15",
"10.03.2020" : "12.90",
"16.12.2019" : "13.20",
"10.09.2019" : "13.70",
"10.12.2018" : "13.80",
"01.10.2018" : "13.75",
"01.07.2018" : "13.70",
"01.04.2018" : "13.45",
"01.01.2018" : "13.40",
"01.10.2017" : "13.70",
"01.07.2017" : "13.75",
"01.04.2017" : "13.85",
"01.01.2017" : "14.00",
"05.10.2015" : "14.05",
"08.06.2015" : "14.45",
"10.04.2015" : "14.60",
"07.11.2013" : "14.75",
"19.09.2013" : "14.55",
"04.02.2013" : "14.45",
"27.09.2012" : "14.50",
"13.08.2011" : "14.75",
"11.07.2011" : "14.25",
"12.05.2011" : "14.00",
"25.04.2011" : "13.25",
"14.02.2011" : "13.00",
"03.01.2011" : "12.75",
"21.10.2010" : "12.50",
"17.08.2010" : "12.25",
"29.06.2009" : "11.75",
"01.01.2009" : "12.25",
"10.11.2008" : "13.00",
"12.08.2008" : "13.75",
"27.06.2008" : "12.75",
"27.02.2008" : "12.25",
"16.02.2008" : "12.50",
"09.04.2007" : "12.75",
"20.02.2007" : "12.25",
"27.12.2006" : "11.50",
"02.08.2006" : "11.00",
"01.05.2006" : "10.75",
"01.01.2004" : "10.25",
"05.05.2003" : "10.50",
"01.11.2002" : "10.75",
"01.04.2002" : "11.00",
"05.03.2001" : "11.50",
"12.08.2000" : "12.00",
"01.04.2000" : "11.25",
"01.03.1999" : "12.00",
"01.05.1998" : "13.00",
"02.04.1998" : "13.50",
"22.01.1998" : "14.00",
"01.11.1997" : "13.00",
"01.07.1997" : "13.50",
"16.04.1997" : "14.00",
"01.11.1996" : "14.50",
"06.09.1996" : "15.50",
"15.07.1996" : "16.00",
"10.11.1995" : "16.50",
"24.04.1995" : "15.50",
"15.02.1995" : "15.00",
"18.10.1994" : "14.00",
"02.09.1993" : "15.00",
"24.06.1993" : "16.00",
"01.03.1993" : "17.00",
"09.10.1992" : "18.00",
"02.03.1992" : "19.00",
"09.10.1991" : "20.00",
"04.07.1991" : "18.50",
"01.04.1991" : "17.00"}

import json

lending_rates = {}
for i in lending_rates_raw.keys():
    d = i.split(".")
    date = datetime.date(int(d[2]), int(d[1]), int(d[0]))
    lending_rates[date] = float(lending_rates_raw[i])

print(lending_rates)

start_year = 1991
end_year = 2023

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

converted_dict = {int(datetime.datetime.combine(key, datetime.datetime.min.time()).timestamp()): value for key, value in lending_rates_data.items()}

# Write JSON data to a file
with open('data/rbi_lending_rate.json', 'w') as file:
    json.dump(converted_dict, file)

# with open('data.json', 'r') as file:
#     loaded_data = json.load(file)

# # Convert Unix timestamps back to datetime.date objects
# converted_dates = {datetime.utcfromtimestamp(int(timestamp)).date(): value for timestamp, value in loaded_data.items()}

# print(converted_dates)


dates = list(lending_rates_data.keys())
values = list(lending_rates_data.values())

fig = go.Figure()

# Add a scatter trace for time series data
fig.add_trace(go.Scatter(x=dates, y=values, mode='lines+markers', name='Time Series'))

# Update layout with title and axis labels
fig.update_layout(
    title='RBI Lending Rates',
    xaxis=dict(title='Date'),
    yaxis=dict(title='Value')
)

# Show the interactive plot
fig.show()






