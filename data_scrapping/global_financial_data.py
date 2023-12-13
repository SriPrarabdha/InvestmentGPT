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

EU_NG=fred.get_series(series_id='PNGASEUUSDM')

LNG_ASIA=fred.get_series(series_id='PNGASJPUSDM')

US_NG=fred.get_series(series_id='PNGASUSUSDM')

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot()

ax.plot(EU_NG, lw=1.5,color='black')
ax.plot(LNG_ASIA, lw=1.5,color='red')
ax.plot(US_NG, lw=1.5,linestyle='dashed',color='blue')


ax.set_title('Graph 1: Natural Gas Prices')
plt.legend(labels=['EU','LNG Asia','United States'])
plt.grid()

ax.set_xlim([12000, 19500])

ax.secondary_yaxis("right")
ax.set_xlabel(xlabel='Year', size=12)
ax.set_ylabel(ylabel='U.S. Dollars per Million Metric British Thermal Unit ', size=12)

fig.show()
fig.savefig('global_natural_gas.png')

GP_OIL=fred.get_series(series_id='POILWTIUSDM')

COM_IND=fred.get_series(series_id='PALLFNFINDEXQ')

GP_OIL.to_json("data/global_oil_prices.json")
COM_IND.to_json("data/global_commodity_prices.json")
GP_OIL.to_json("data/eu_natural_gas_prices.json")
GP_OIL.to_json("data/asia_natural_gas_prices.json")
GP_OIL.to_json("data/us_natural_gas_prices.json")

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot()

ax.plot(GP_OIL, lw=1.5,color='black')
ax.plot(COM_IND, lw=1.5,linestyle='dashed',color='red')


ax.set_title('Graph 2: Commodities Index and Oil')
plt.legend(labels=['WTI Crude','All Commodities'])

plt.grid()
ax.set_xlim([12000, 19500])

ax.secondary_yaxis("right")
ax.set_xlabel(xlabel='Year', size=12)

fig.show()
fig.savefig('oil_n_commodity.png')