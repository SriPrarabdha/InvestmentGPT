import pandas as pd
# from fbprophet import Prophet
from statsmodels.tsa.arima.model import ARIMA
from pandas import DataFrame
import matplotlib.pyplot as plt
import json

# model = ARIMA()

with open('C:/Users/Prarabdha/Desktop/projects/se_mini_project/data/asia_natural_gas_prices.json', 'r') as file:
    data = json.load(file)

# Convert JSON data to a pandas DataFrame
df = pd.DataFrame.from_dict(data, orient='index', columns=['Value'])
df.index = pd.to_datetime(df.index, unit='ms')  # Convert timestamp to datetime

# Fit ARIMA model to the data
# Replace p, d, q values with appropriate parameters
# For example, p=1, d=1, q=1 represents an ARIMA(1,1,1) model
model = ARIMA(df['Value'], order=(1, 2, 3))
results = model.fit()
print(df.tail(10))
# Forecast future values
forecast = results.forecast(steps=40)  # Change the steps according to how many future steps you want to forecast
print(forecast)
print(type(forecast))

forecast_index = pd.date_range(start=df.index[-1], periods=41, freq='M')[1:]

# Plot the original time series data and forecasted values in the same figure
plt.figure(figsize=(10, 6))

# Plot original data in blue
plt.plot(df.index, df['Value'], label='Original Data', color='blue')

# Plot forecasted data in red
plt.plot(forecast_index, forecast, label='Forecasted Data', color='red')

plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Original Time Series Data and Forecast')
plt.legend()
plt.show()

# df = pd.read_csv("C:/Users/Prarabdha/Desktop/projects/se_mini_project/data_csv/Housing_cpi_data.csv")
# print(int(0.5*df.shape[0]))
# df_ = df.tail(int(0.5*df.shape[0]))
# print(df_)

# model = ARIMA(df_['Value'], order=(1, 1, 1))
# results = model.fit()

# # Forecast future values
# forecast = results.forecast(steps=10)  # Change the steps according to how many future steps you want to forecast

# print("Forecasted values:", forecast)

# plt.figure(figsize=(10, 6))

# # Plot original data
# print(df.index)
# plt.plot(df['Timestamp'], df['Value'], label='Original Data', color='blue')

# # Plot forecasted data
# forecast_index = pd.date_range(start=df.index[-1], periods=11, closed='left')
# plt.plot(forecast_index[1:], forecast, label='Forecasted Data', color='red')

# plt.xlabel('Date')
# plt.ylabel('Value')
# plt.title('Time Series Data and Forecast')

# plt.legend()
# plt.show()
# model = ARIMA(df_, order=(5,1,0))
# model_fit = model.fit()
# # summary of fit model
# print(model_fit.summary())
# # line plot of residuals
# residuals = DataFrame(results.resid)
# residuals.plot()
# pyplot.show()
# # density plot of residuals
# residuals.plot(kind='kde')
# pyplot.show()
# # summary stats of residuals
# print(residuals.describe())