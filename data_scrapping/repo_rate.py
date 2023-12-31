# RBI Repo rate

import datetime
import matplotlib.pyplot as plt
import plotly.graph_objects as go

repo_rates_raw = {"10-08-2023":	"6.50",
"08-06-2023":	"6.50",
"06-04-2023":	"6.50",
"08-01-2023":	"6.50",
"07-12-2022":	"6.25",
"30-09-2022":	"5.90",
"05-08-2022":	"5.40",
"08-06-2022":	"4.90",
"04-05-2022":	"4.40",
"08-04-2022":	"4.00",
"10-02-2022":	"4.00",
"08-12-2021":	"4.00",
"09-10-2021":	"4.00",
"06-08-2021":	"4.00",
"04-06-2021":	"4.00",
"07-04-2021":	"4.00",
"05-02-2021":	"4.00",
"04-12-2020":	"4.00",
"09-10-2020":	"4.00",
"06-08-2020":	"4.00",
"22-05-2020":	"4.00",
"27-03-2020":	"4.40",
"06-02-2020":	"5.15",
"05-12-2019":	"5.15",
"04-10-2019":	"5.15",
"07-08-2019":	"5.40",
"06-06-2019":	"5.75",
"04-04-2019":	"6",
"07-02-2019":	"6.25",
"01-08-2018":	"6.50",
"06-06-2018":	"6.25",
"07-02-2018":	"6.00",
"02-08-2017":	"6.00",
"04-10-2016":	"6.25",
"05-04-2016":	"6.50",
"29-09-2015":	"6.75",
"02-06-2015":	"7.25",
"04-03-2015":	"7.50",
"15-01-2015":	"7.75",
"28-01-2014":	"8.00",
"29-10-2013":	"7.75",
"20-09-2013":	"7.50",
"03-05-2013":	"7.25",
"17-03-2011":	"6.75",
"25-01-2011":	"6.50",
"02-11-2010":	"6.25",
"16-09-2010":	"6.00",
"27-07-2010":	"5.75",
"02-07-2010":	"5.50",
"20-04-2010":	"5.25",
"19-03-2010":	"5.00",
"21-04-2009":	"4.75",
"05-03-2009":	"5.00",
"05-01-2009":	"5.50",
"08-12-2008":	"6.50",
"03-11-2008":	"7.50",
"20-10-2008":	"8.00",
"30-07-2008":	"9.00",
"25-06-2008":	"8.50",
"12-06-2008":	"8.00",
"30-03-2007":	"7.75",
"31-01-2007":	"7.50",
"30-10-2006":	"7.25",
"25-07-2006":	"7.00",
"24-01-2006":	"6.50",
"24-01-2006":	"6.50",
"26-10-2005":	"6.25",
"26-10-2005":	"6.25",
"31-03-2004":	"6.00",
"19-03-2003":	"7.00",
"07-03-2003":	"7.10",
"12-11-2002":	"7.50",
"28-03-2002":	"8.00",
"07-06-2001":	"8.50",
"30-04-2001":	"8.75",
"09-03-2001":	"9.00",
"06-11-2000": "10.00",
"13-10-2000": "10.25",
"06-09-2000": "13.50",
"30-08-2000": "15.00",
"09-08-2000": "16.00",
"21-07-2000": "10.00",
"13-07-2000":	"9.00",
"28-06-2000": "12.25",
"27-06-2000": "12.60",
"23-06-2000": "13.05",
"22-06-2000": "13.00",
"21-06-2000": "13.50",
"20-06-2000": "14.00",
"19-06-2000": "13.50",
"14-06-2000": "10.85",
"13-06-2000":	"9.55",
"12-06-2000":	"9.25",
"09-06-2000":	"9.05",
"07-06-2000":	"9.00",
"05-06-2000":	"9.05",}

repo_rates = {}
for i in repo_rates_raw.keys():
    d = i.split("-")
    date = datetime.date(int(d[2]), int(d[1]), int(d[0]))
    repo_rates[date] = float(repo_rates_raw[i])

print(repo_rates)

start_year = 2000
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

repo_rates_data = {}

for i in all_dates:
    if i in repo_rates.keys():
        repo_rates_data[i] = repo_rates[i]
    else:
        repo_rates_data[i] = 0

# print(repo_rates_data)

val = 9.05
for i in range(len(all_dates)):
    if repo_rates_data[all_dates[i]] == 0:
        repo_rates_data[all_dates[i]] = val
    else:
        val = repo_rates_data[all_dates[i]]

print(repo_rates_data)

import json

converted_dict = {int(datetime.datetime.combine(key, datetime.datetime.min.time()).timestamp()): value for key, value in repo_rates_data.items()}

# Write JSON data to a file
with open('data/rbi_repo_rate.json', 'w') as file:
    json.dump(converted_dict, file)

dates = list(repo_rates_data.keys())
values = list(repo_rates_data.values())

fig = go.Figure()

# Add a scatter trace for time series data
fig.add_trace(go.Scatter(x=dates, y=values, mode='lines+markers', name='Time Series'))

# Update layout with title and axis labels
fig.update_layout(
    title='RBI Repo Rate',
    xaxis=dict(title='Date'),
    yaxis=dict(title='Value')
)

# Show the interactive plot
fig.show()