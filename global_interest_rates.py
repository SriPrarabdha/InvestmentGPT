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

FEDFUNDS=fred.get_series(series_id='FEDFUNDS')

#Market Yield on U.S. Treasury Securities at 2-Year Constant Maturity, Quoted on an Investment Basis
T2Y=fred.get_series(series_id='DGS2')

# Market Yield on U.S. Treasury Securities at 10-Year Constant Maturity, Quoted on an Investment Basis
T10Y=fred.get_series(series_id='DGS10')

#10-Year Treasury Constant Maturity Minus 2-Year Yield. This is a measure of the yield curve.
T10Y2Y=fred.get_series(series_id='T10Y2Y')

# Immediate Rates: Less than 24 Hours: Call Money/Interbank Rate for the United States 
US_INT=fred.get_series(series_id='IRSTCI01USM156N')

#Immediate Rates: Less than 24 Hours: Call Money/Interbank Rate for the United Kingdom
UK_INT=fred.get_series(series_id='IRSTCI01GBM156N')

#Immediate Rates: Less than 24 Hours: Call Money/Interbank Rate for Japan (IRSTCI01JPM156N)
JAP_INT=fred.get_series(series_id='IRSTCI01JPM156N')

#Immediate Rates: Less than 24 Hours: Call Money/Interbank Rate for India (IRSTCI01INM156N)
IND_INT=fred.get_series(series_id='IRSTCI01INM156N')

#Interest Rates: Immediate Rates (< 24 Hrs): Call Money/Interbank Rate: Total for Brazil (IRSTCI01BRM156N)
BRA_INT=fred.get_series(series_id='IRSTCI01BRM156N')

#Interest Rates: Immediate Rates (< 24 Hrs): Call Money/Interbank Rate: Total for Germany
GER_INT=fred.get_series(series_id='IRSTCI01DEM156N')

#Immediate Rates: Less than 24 Hours: Central Bank Rates for Poland
POL_INT=fred.get_series(series_id='IRSTCB01PLM156N')

#Immediate Rates: Less than 24 Hours: Central Bank Rates for South Africa
SA_INT=fred.get_series(series_id='IRSTCB01ZAM156N')

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot()

ax.plot(US_INT, lw=2,color='black')
ax.plot(UK_INT, lw=2,color='red')
ax.plot(GER_INT, lw=2,color='grey')
ax.plot(SA_INT,lw=2,color='green')
ax.plot(JAP_INT,lw=2,linestyle='dashed',color='red')
ax.plot(IND_INT,lw=2,color='orange')     
ax.plot(BRA_INT,lw=2,linestyle='dashed',color='limegreen')    

ax.set_title('Central Bank Interest Rates')
plt.legend(labels=['United States','United Kingdom','Germany (EURO)','South Africa','Japan','India','Brazil'])


ax.set_yticks(np.arange(-30, 52, 2))
plt.grid()

ax.set_xlim([10000, 19300])
ax.set_ylim([-2, 50]) 
ax.secondary_yaxis("left")

plt.savefig('global_interest_rates_1.png')