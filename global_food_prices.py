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

FOOD=fred.get_series(series_id='PFOODINDEXM')

#Global price of Wheat (PWHEAMTUSDM)
WHEAT=fred.get_series(series_id='PWHEAMTUSDM')

#Global price of Barley (PBARLUSDM)
BARLEY=fred.get_series(series_id='PBARLUSDM')

#Global price of Corn (PMAIZMTUSDM)
CORN=fred.get_series(series_id='PMAIZMTUSDM')


#Indexing for year "2000-01-01" == 100
FOOD=(FOOD/58)*100
WHEAT=(WHEAT/93)*100
BARLEY=(BARLEY/73)*100
CORN=(CORN/92)*100

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot()

ax.plot(FOOD, lw=1.5,color='black')
ax.plot(WHEAT, lw=1.5,color='red')
ax.plot(BARLEY, lw=1.5,linestyle='dashed',color='blue')
ax.plot(CORN, lw=1.5,linestyle='dashed',color='red')

ax.set_title('Graph 3: Global Food Prices')
plt.legend(labels=['All Food Prices','Wheat','Barley','Corn'])

plt.grid()
ax.secondary_yaxis("right")
ax.set_xlabel(xlabel='Year', size=12)
ax.set_ylabel(ylabel='Index 2000-01=100 ', size=12)

fig.show()
fig.savefig('global_food_prices.png')