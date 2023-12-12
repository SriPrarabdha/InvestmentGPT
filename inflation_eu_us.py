import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
sns.set_style("white")
import pandas as pd
import numpy as np
import os
import dotenv

from fredapi import Fred

dotenv.load_dotenv()

fred_key = os.environ.get('FRED_API_KEY')
print("fred key ==== ",fred_key)

fred = Fred(api_key=fred_key)

GER_PPI=fred.get_series(series_id='PIEATI01DEM661N')
GER_PPI=GER_PPI.to_frame(name='PPI')
GER_PPI=((GER_PPI-GER_PPI.shift(12))/GER_PPI.shift(12))*100


#Producer Prices Index: Economic Activities: Industrial Activities: Total for the Euro Area (19 Countries)
#PIEATI01EZM661N
EURO_PPI=fred.get_series(series_id='PIEATI01EZM661N')
EURO_PPI=EURO_PPI.to_frame(name='PPI')
EURO_PPI=((EURO_PPI-EURO_PPI.shift(12))/EURO_PPI.shift(12))*100

#Producer Prices Index: Economic activities: Industrial activities: Total for Poland (Growth)
#POLPIEATI01GYM
POL_PPI=fred.get_series(series_id='POLPIEATI01GYM')
POL_PPI=POL_PPI.to_frame(name='PPI')

#Producer Price Index by Industry: Total Manufacturing Industries US
#PCUOMFGOMFG
US_PPI=fred.get_series(series_id='PCUOMFGOMFG')
US_PPI=US_PPI.to_frame(name='PPI')
US_PPI=((US_PPI-US_PPI.shift(12))/US_PPI.shift(12))*100

#Producer Prices Index: Economic Activities: Total Industrial Activities for the United Kingdom
#PIEATI01GBM661N
UK_PPI=fred.get_series(series_id='PIEATI01GBM661N')
UK_PPI=UK_PPI.to_frame(name='PPI')
UK_PPI=((UK_PPI-UK_PPI.shift(12))/UK_PPI.shift(12))*100

US_inf_targ=US_PPI
US_inf_targ['Inflation_Target'] =2
From = '1990-01-01'
#Date chosen given that inflation targeting was first attempted by New Zealand around this date.
df_Z = US_inf_targ.loc[From:,:]

#Drop variables to each dataframe.
df_Z = df_Z.drop ('PPI',axis=1)
US_PPI = US_PPI.drop ('Inflation_Target',axis=1)

US_PPI.to_json('data/us_inflation.json')
GER_PPI.to_json('data/german_inflation.json')
EURO_PPI.to_json('data/EURO_inflation.json')
POL_PPI.to_json('data/polish_inflation.json')
UK_PPI.to_json('data/uk_inflation.json')

plt.figure(figsize=(12,7))
ax = sns.lineplot(data=US_PPI, x=US_PPI.index, y=US_PPI['PPI'],color='blue')
ax = sns.lineplot(data=GER_PPI, x=GER_PPI.index, y=GER_PPI['PPI'],linestyle='dashed',color='black')
ax = sns.lineplot(data=EURO_PPI, x=EURO_PPI.index, y=EURO_PPI['PPI'],color='black')
ax = sns.lineplot(data=POL_PPI, x=POL_PPI.index, y=POL_PPI['PPI'],color='red')
ax = sns.lineplot(data=UK_PPI, x=UK_PPI.index, y=UK_PPI['PPI'],color='orange')
ax = sns.lineplot(data=df_Z, x=df_Z.index, linestyle = 'dashed', y=df_Z['Inflation_Target'],color='green')
plt.legend(labels=[ 'United States','Germany','Euro Zone','Poland','United Kingdom', '2% Inflation Target',])

ax.set_ylim(bottom=-10, top=35)
ax.set_xlabel(xlabel='Year', size=12)
ax.set_ylabel(ylabel='Inflation (%)', size=12)
ax.set_title('Graph 5: Producer Inflation (%) in Europe and the US', size=20)
ax.secondary_yaxis("right")
ax.set_xlim([12000, 19500])
plt.grid()

# plt.savefig('inflation_eu_us')
