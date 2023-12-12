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

METAL=fred.get_series(series_id='PMETAINDEXM')

#Global price of Coal, Australia (PCOALAUUSDM)
COAL=fred.get_series(series_id='PCOALAUUSDM')

#Global price of Copper (PCOPPUSDM)
COPPER=fred.get_series(series_id='PCOPPUSDM')

#Global price of Rubber (PRUBBUSDM)
RUBBER=fred.get_series(series_id='PBARLUSDM')

#Global price of Iron Ore (PIORECRUSDM)
IRON=fred.get_series(series_id='PIORECRUSDM')

# Global price of Aluminum (PALUMUSDM)
ALUM=fred.get_series(series_id='PALUMUSDM')


#Indexing for year "2000-01-01" == 100
METAL=(METAL/49)*100
COAL=(COAL/25)*100
COPPER=(COPPER/1843)*100
RUBBER=(RUBBER/73)*100
IRON=(IRON/12)*100
ALUM=(ALUM/1679)*100


fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot()

ax.plot(METAL, lw=1.5,color='black')
ax.plot(COAL, lw=1.5,color='red')
ax.plot(COPPER, lw=1.5,linestyle='dashed',color='blue')
ax.plot(RUBBER, lw=1.5,linestyle='dashed',color='red')
ax.plot(IRON, lw=1.5,linestyle='dashed',color='green')
ax.plot(ALUM, lw=1.5,linestyle='dashed',color='yellow')

ax.set_title('Graph 4: Global Metal and Coal Prices')
plt.legend(labels=['All Metals','Coal','Copper','Rubber','Iron','Aluminium'])


plt.grid()
ax.set_xlim([12000, 19500])

ax.secondary_yaxis("right")
ax.set_xlabel(xlabel='Year', size=12)
ax.set_ylabel(ylabel='Index 2000-01=100 ', size=12)

fig.show()
fig.savefig('global_coal_metal_prices.png')