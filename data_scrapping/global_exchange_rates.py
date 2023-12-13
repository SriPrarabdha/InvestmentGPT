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
import json

from fredapi import Fred

dotenv.load_dotenv()

fred_key = os.environ.get('FRED_API_KEY')
print("fred key ==== ",fred_key)

fred = Fred(api_key=fred_key)

US_EURO=fred.get_series(series_id='DEXUSEU')

#U.S. Dollars to United Kingdom Pound Spot Exchange Rate 
US_UK=fred.get_series(series_id='DEXUSUK')

#Swiss Francs to U.S. Dollar Spot Exchange Rate (DEXSZUS)
US_SWI=fred.get_series(series_id='DEXSZUS')

#U.S. Dollars to Australian Dollar Spot Exchange Rate (DEXUSAL)
US_AUS=fred.get_series(series_id='DEXUSAL')

#U.S. Dollars to New Zealand Dollar Spot Exchange Rate (DEXUSNZ)
US_NZ=fred.get_series(series_id='DEXUSNZ')

US_CHI=fred.get_series(series_id='DEXCHUS')

US_JAP=fred.get_series(series_id='DEXJPUS')

US_IND=fred.get_series(series_id='DEXINUS')

US_BRA=fred.get_series(series_id='DEXBZUS')

US_SA=fred.get_series(series_id='DEXSFUS')

#Swedish Kronor to U.S. Dollar Spot Exchange Rate (DEXSDUS)
US_SWE=fred.get_series(series_id='DEXSDUS')

US_SWI=1/US_SWI
US_JAP=US_JAP/10
US_IND=US_IND/10

US_IND.to_json('data/us_ind_exchange_rates.json'), 
US_EURO.to_json('data/us_euro_exchange_rates.json'), 
US_UK.to_json('data/us_uk_exchange_rates.json'), 
US_CHI.to_json('data/us_china_exchange_rates.json'), 
US_JAP.to_json('data/us_japan_exchange_rates.json'), 
US_BRA.to_json('data/us_brazil_exchange_rates.json'), 
US_SA.to_json('data/us_sa_exchange_rates.json'), 

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot()
US_1=(US_EURO*0)+1

ax.plot(US_EURO, lw=2,color='blue')
ax.plot(US_UK, lw=2,color='red')
ax.plot(US_SWI, lw=2,color='green')
ax.plot(US_AUS, lw=2,color='orange')
ax.plot(US_NZ, lw=2,color='grey')
ax.plot(US_1, lw=2,linestyle='dotted',color='black')

ax.set_title('Exchange Rates in US Dollar ($)')
plt.legend(labels=['Euro','Pound','Swiss Franc', 'Australia Dollar','New Zealand Dollar'])

ax.set_xlim([13000, 19300])
ax.set_ylim([0.5, 2.5]) 
ax.secondary_yaxis("right")
plt.grid()

plt.savefig('plots/global_exchange_rate.png')