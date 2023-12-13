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

FEDFUNDS.to_json("data/fedfunds.json")
T2Y.to_json("data/treasurey_yield_2.json")
T10Y.to_json("data/treasurey_yield_10.json")
T10Y2Y.to_json("data/treasurey_yield_10-2.json")

# fig = plt.figure(figsize=(12, 6))
# ax = fig.add_subplot()

# ax.plot(T2Y, lw=2,color='black')
# ax.plot(T10Y, lw=2,color='red')
# ax.plot(T10Y2Y,lw=2,color='green')
# ax.plot(FEDFUNDS,lw=2,linestyle='dashed',color='red')
  

# ax.set_title('Central Bank Interest Rates')
# plt.legend(labels=["U.S. Treasury Securities at 2-Year Constant Maturity","U.S. Treasury Securities at 2-Year Constant Maturity","10-Year Treasury Constant Maturity Minus 2-Year Yield"])


# ax.set_yticks(np.arange(-10, 10, 2))
# plt.grid()

# ax.set_xlim([10000, 19300])
# ax.set_ylim([-2, 10]) 
# ax.secondary_yaxis("left")

# plt.savefig('us_treasurey_yield.png')