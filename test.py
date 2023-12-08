# from datetime import datetime

# wpi_data_raw = {"Nov 14, 2023":	-0.52,	
# "Oct 16, 2023":		-0.26,
# "Sep 14, 2023":		-0.52,	
# "Aug 14, 2023":		-1.36,	
# "Jul 14, 2023":		-4.12,
# "Jun 14, 2023":		-3.48,
# "May 15, 2023":		-0.92,
# "Apr 17, 2023":		1.34,
# "Mar 14, 2023":		3.85,
# "Feb 14, 2023":		4.73,
# "Jan 16, 2023":		4.95,
# "Dec 14, 2022":		5.85,
# "Nov 14, 2022":		8.39,
# "Oct 14, 2022":		10.70,
# "Sep 14, 2022":		12.41,
# "Aug 16, 2022":		13.93,
# "Jul 14, 2022":		15.18,
# "Jun 14, 2022":		15.88,
# "May 17, 2022":		15.08,
# "Apr 18, 2022":		14.55,
# "Mar 14, 2022":		13.11,
# "Feb 14, 2022":		12.96,
# "Jan 14, 2022":		13.56,
# "Dec 14, 2021":		14.23,
# "Nov 15, 2021":		12.54,
# "Oct 14, 2021":		10.66,
# "Sep 14, 2021":		11.39,
# "Aug 16, 2021":		11.16,
# "Jul 14, 2021":		12.07,
# "Jun 14, 2021":		12.94,
# "May 17, 2021":		10.49,
# "Apr 15, 2021":		7.39,
# "Mar 15, 2021":		4.17,
# "Feb 15, 2021":		2.03,
# "Jan 14, 2021":		1.22,
# "Dec 14, 2020":		1.55,
# "Nov 16, 2020":	    1.48,
# "Oct 14, 2020":		1.32,
# "Sep 14, 2020":		0.16,
# "Aug 14, 2020":		-0.58,
# "Jul 14, 2020":		-1.81,
# "Jun 15, 2020":		-3.21,
# "May 14, 2020":		0.00,
# "Apr 15, 2020":		0.90,
# "Mar 16, 2020":		2.26,
# "Feb 14, 2020":		3.10,
# "Jan 14, 2020":		2.59,
# "Dec 16, 2019":		0.58,
# "Nov 14, 2019":		0.16,
# "Oct 14, 2019":		0.33,
# "Sep 16, 2019":		1.08,
# "Aug 14, 2019":		1.08,
# "Jul 15, 2019":		2.02,
# "Jun 14, 2019":		2.45,
# "May 14, 2019":		3.07,
# "Apr 15, 2019":		3.18,
# "Mar 14, 2019":		2.93,
# "Feb 14, 2019":		2.76,
# "Jan 14, 2019":		3.80,
# "Dec 14, 2018":		4.64,
# "Nov 14, 2018":		5.28,
# "Oct 15, 2018":		5.13,
# "Sep 14, 2018":		4.53,
# "Aug 14, 2018":		5.09,
# "Jul 16, 2018":		5.77,
# "Jun 14, 2018":		4.43,
# "May 14, 2018":		3.18,
# "Apr 16, 2018":		2.47,
# "Mar 14, 2018":		2.48,
# "Feb 15, 2018":		2.84,
# "Jan 15, 2018":		3.58,
# "Dec 14, 2017":		3.93,
# "Nov 14, 2017":		3.59,
# "Oct 16, 2017":		2.60,
# "Sep 14, 2017":		3.24,
# "Aug 14, 2017":		1.88,
# "Jul 14, 2017":  	0.90 ,
# "Jun 14, 2017":		2.17,
# "May 12, 2017":		3.85,
# "Apr 17, 2017":		5.70,
# "Mar 14, 2017":		6.55,
# "Feb 14, 2017":		5.25,
# "Jan 16, 2017":		3.39,
# "Dec 14, 2016":		3.15,
# "Nov 15, 2016":		3.39,
# "Oct 14, 2016":		3.57,
# "Sep 14, 2016":		3.74,
# "Aug 16, 2016"	:	3.55,
# "Jul 14, 2016"	:	1.62,
# "Jun 14, 2016"	:	0.79,  
# "May 16, 2016"	:	0.34,  	
# "Apr 18, 2016"	:	-0.85,  	
# "Mar 14, 2016"	:	-0.1,  	
# "Feb 15, 2016"	:	-0.90,  	
# "Jan 14, 2016"	:	-0.73,  	
# "Dec 14, 2015"	:	-1.99,  	
# "Nov 16, 2015"	:	-3.81,  	
# "Oct 14, 2015"	:	-4.54,  	
# "Sep 14, 2015"	:	-4.95,  	
# "Aug 14, 2015"	:	-4.05,  	
# "Jul 14, 2015"	:	-2.40,  	
# "Jun 15, 2015"	:	-2.36,  	
# "May 14, 2015"	:	-2.65,  	
# "Apr 15, 2015"	:	-2.33,  	
# "Mar 16, 2015"	:	-2.06,  	
# "Feb 16, 2015"	:	-0.39,  
# "Jan 14, 2015"	:	0.11,  
# "Dec 15, 2014"	:	0.00,  
# "Nov 14, 2014"	:	1.77,  
# "Oct 14, 2014"	:	2.38,  
# "Sep 15, 2014"	:	3.74,  
# "Aug 14, 2014"	:5.19,  
# "Jul 14, 2014"	:5.43,  
# "Jun 16, 2014"	:6.01,  
# "May 15, 2014"	:5.20,  
# "Apr 15, 2014"	:5.70,  
# "Mar 14, 2014"	:4.68,  
# "Feb 14, 2014"	:5.05,  
# "Jan 15, 2014"	:6.16,  
# "Dec 16, 2013"	:7.52,  
# "Nov 14, 2013"	:7.00,  
# "Oct 14, 2013"	:6.46,  
# "Sep 16, 2013"	:6.10,  
# "Aug 14, 2013"	:5.79,  
# "Jul 15, 2013"	:4.86,  
# "Jun 14, 2013"	:4.70,  
# "May 14, 2013"	:4.89,  
# "Apr 15, 2013"	:5.96,  
# "Mar 14, 2013"	:6.84,  
# "Feb 14, 2013"	:6.62,  
# "Jan 14, 2013"	:7.18,  
# "Dec 14, 2012"	:7.24,  
# "Nov 14, 2012"	:7.45,  
# "Oct 15, 2012"	:7.81,  
# "Sep 14, 2012"	:7.55,  
# "Aug 14, 2012"	:6.87,  
# "Jul 16, 2012"	:7.25,  
# "Jun 14, 2012"	:7.55,  
# "May 14, 2012" : 7.23,
# "Apr 16, 2012" : 6.89,
# "Mar 14, 2012" : 6.95,
# "Feb 14, 2012" : 6.60,
# "Jan 16, 2012" : 7.50,	
# "Dec 14, 2011" : 9.10,
# "Nov 14, 2011" : 9.70,
# "Oct 14, 2011" : 9.70,
# "Sep 14, 2011" : 9.80,
# "Aug 16, 2011" : 9.20,
# "Jul 14, 2011" : 9.40,
# "Jun 19, 2011" : 9.10,
# "May 01, 2011" : 9.74,
# "Apr 01, 2011" : 9.68,
# "Mar 01, 2011" : 9.54,
# "Feb 01, 2011" : 9.47,
# "Jan 01, 2011" : 9.45,
# "Dec 01, 2010" : 8.20,
# "Nov 01, 2010" : 9.08,
# "Oct 01, 2010" : 8.98,
# "Sep 01, 2010" : 8.87,
# "Aug 01, 2010" : 9.98,	
# "Jul 01, 2010"  : 0.25,	
# "Jun 01, 2010"  : 0.48,	
# "May 01, 2010"  : 0.88,	
# "Apr 01, 2010"  : 0.36,
# "Mar 01, 2010" : 9.65,
# "Feb 01, 2010" : 8.68,
# "Jan 01, 2010" : 7.15,
# "Dec 01, 2009" : 4.73,
# "Nov 01, 2009" : 1.79,
# "Oct 01, 2009" : 1.40,
# "Sep 01, 2009" : 0.54,	
# "Aug 01, 2009"  : 0.31,	
# "Jul 01, 2009"  : 0.39,
# "Jun 01, 2009" : 1.45,
# "May 01, 2009" : 1.21,
# "Apr 01, 2009" : 1.65,
# "Mar 01, 2009" : 3.61,
# "Feb 01, 2009" : 5.87,
# "Jan 01, 2009" : 6.68,
# "Dec 01, 2008" : 8.65,	
# "Nov 01, 2008"  : 0.66,	
# "Oct 01, 2008"  : 0.78,	
# "Sep 01, 2008" :	11.12,	
# "Aug 01, 2008" :	11.15,	
# "Jul 01, 2008" :	10.89,
# "Jun 01, 2008" :	8.20,
# "May 01, 2008" :	7.86,
# "Apr 01, 2008" :	7.71,
# "Mar 01, 2008" :	5.68,
# "Feb 01, 2008" :	4.54,
# "Jan 01, 2008" :	4.01,
# "Dec 01, 2007" :	3.73,
# "Nov 01, 2007" :	3.19,
# "Oct 01, 2007" :	3.39,
# "Sep 01, 2007" :	4.04,
# "Aug 01, 2007" :	4.42,
# "Jul 01, 2007" :	4.46,
# "Jun 01, 2007" :	5.52,
# "May 01, 2007" :	6.22,
# "Apr 01, 2007" :	6.72,
# "Mar 01, 2007" :	6.63,
# "Feb 01, 2007" :	6.64,
# "Jan 01, 2007" :	6.96,
# "Dec 01, 2006" :	6.73,
# "Nov 01, 2006" :	6.93,
# "Oct 01, 2006" :	6.96,
# "Sep 01, 2006" :	7.11,
# "Aug 01, 2006" :	6.54,
# "Jul 01, 2006" :	6.80,
# "Jun 01, 2006" :	6.05,
# "May 01, 2006" :	4.97,
# "Apr 01, 2006" :	4.24,
# "Mar 01, 2006" :	4.45,
# "Feb 01, 2006" :	4.36,
# "Jan 01, 2006" :	4.38,
# "Dec 01, 2005" :	3.94,
# "Nov 01, 2005" :	4.67,
# "Oct 01, 2005" :	4.38,
# "Sep 01, 2005" :	3.48,
# "Aug 01, 2005" :	4.84,
# "Jul 01, 2005" :	4.68,
# "Jun 01, 2005" :	4.59,
# "May 01, 2005" :	5.33,
# }

# final_wpi_data = {}

# # import datetime as dt
# for key in wpi_data_raw.keys():
#     # print(key)
#     date = datetime.strptime(key, "%b %d, %Y").date()
#     final_wpi_data[date] = wpi_data_raw[key]
# print("------------------------------------------------")
# print(final_wpi_data)

# print(len(final_wpi_data), len(wpi_data_raw))
import ast
import datetime
import re
import math
import plotly.graph_objects as go

with open("1.txt" , "r") as f:
    text = f.read()

# print(text)

pattern = r'datetime\.date\(\d{4}, \d{1,2}, \d{1,2}\): [0-9.-]+'
matches = re.findall(pattern, text)

# Create a dictionary with keys as datetime.date objects and values as floats
result_dict = {}
for match in matches:
    key, value = match.split(": ")
    # Extract year, month, and day using regex
    year, month, day = re.findall(r'\d{4}|\d{1,2}', key)
    key_date = datetime.date(int(year), int(month), int(day))
    result_dict[key_date] = float(value)

print(result_dict)

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

final_wpi_data = {}

for i in all_dates:
    if i in result_dict.keys():
        final_wpi_data[i] = result_dict[i]
    else:
        final_wpi_data[i] = math.inf

print(final_wpi_data)

val = 0
for i in range(len(all_dates)):
    if final_wpi_data[all_dates[i]] == math.inf:
        final_wpi_data[all_dates[i]] = val
    else:
        val = final_wpi_data[all_dates[i]]

print(final_wpi_data)

import plotly.graph_objects as go

dates = list(final_wpi_data.keys())
values = list(final_wpi_data.values())

negative_values = set()
for i, v in enumerate(values):
    if v < 0:
        negative_values.add(i)
        
fig = go.Figure()

for i in range(len(values)):
    fig.add_trace(go.Scatter(
        x = [dates[i]], 
        y = [values[i]],
        mode = 'lines+markers',
        name = str(i),
        line_color = 'rgb(255, 255, 0)' if i in negative_values else 'rgb(0, 0, 255)' 
    ))

fig.update_yaxes(
   showline=True,
   linecolor='rgb(0,0,0)',
   zerolinecolor='rgb(0,0,0)',
   zerolinewidth=2,
)

fig.show()