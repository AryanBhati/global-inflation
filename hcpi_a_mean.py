# -*- coding: utf-8 -*-
"""hcpi_a_mean.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14oUNn425AwNpGafAocGxndeKOc9HNU4r
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


worksheets = pd.read_excel('Inflation-data.xlsx', sheet_name=None)
print(worksheets)

type(worksheets)

worksheets.keys()

worksheets['hcpi_a']

details = pd.read_excel('Inflation-data.xlsx', sheet_name = 1)
details

#
# remove null values and nan values just presenting the details of the worksheets of the project
intro = pd.DataFrame(details)
intro = intro.dropna(axis=0, how='all')
intro = intro.dropna(axis=1, how='all')
intro

#now i would be creating all worksheets in dataframes
hcpi_a_original=pd.DataFrame(worksheets['hcpi_a'])
hcpi_a_original.drop('Note', axis=1, inplace=True)
hcpi_a_original.drop('Indicator Type', axis=1, inplace=True)
hcpi_a_original.drop('Series Name', axis=1, inplace=True)
hcpi_a_original = hcpi_a_original[:-1]
hcpi_a_original

# remove last row 203 from hcpi_a
hcpi_a_original = hcpi_a_original[:-1]
hcpi_a_original

plt.figure(figsize=(10, 6))
sns.heatmap(hcpi_a_original.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()

hcpi_a_original.info()
hcpi_a_original.isnull().sum()

numerical_cols = hcpi_a_original.select_dtypes(include=np.number).columns

# Create the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(hcpi_a_original[numerical_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of hcpi_a_original')
plt.show()

df_zero = hcpi_a_original.fillna(0)
df_zero

# filling missing value with mean in hcpi_a_original

numerical_cols = hcpi_a_original.select_dtypes(include=np.number).columns
hcpi_a_original[numerical_cols] = hcpi_a_original[numerical_cols].fillna(hcpi_a_original[numerical_cols].mean())
hcpi_a_original

hcpi_a_original.columns

if 'Country Code' in hcpi_a_original.columns:
  hcpi_a_original = hcpi_a_original.drop('Country Code', axis=1)

hcpi_a_original.columns

hcpi_a_original.dtypes

#  plot the columns of 1970 to 2023 for india in hpci_a_original
hcpi_a_original_transposed = hcpi_a_original.set_index('Country').transpose()
years_to_plot = list(range(1970, 2024))
india_data = hcpi_a_original_transposed.loc[years_to_plot, 'India']

plt.figure(figsize=(12, 6))
plt.plot(years_to_plot, india_data)
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('India Data from 1970 to 2023')
plt.show()

hcpi_a_original_transposed = hcpi_a_original.set_index('Country').transpose()
years_to_plot = list(range(1970, 2024))
countries = hcpi_a_original_transposed.columns.tolist()
for country in countries:
    try:
        country_data = hcpi_a_original_transposed.loc[years_to_plot, country]

        # Plot the data
        plt.figure(figsize=(18, 10))
        plt.plot(years_to_plot, country_data)
        plt.xlabel('Year')
        plt.ylabel('Value')
        plt.title(f'{country} Data from 1970 to 2023')
        plt.show()
    except:
        print(f"Could not plot data for {country}")

# histogram of US IND AUS CHINA RUSSIAN Federation BRAZIL ARGENTINA GERMANY SWEDEN CANADA JAPAN  KOREA, Rep.,  FRANCE SPAIN AND IRELAND

countries_to_plot = ['United States', 'India', 'Australia', 'China', 'Russian Federation', 'Brazil', 'Argentina', 'Germany', 'Sweden', 'Canada', 'Japan', 'Korea, Rep.', 'France', 'Spain', 'Ireland']
years_to_plot = list(range(1970, 2024))
plt.figure(figsize=(12, 6))
for country in countries_to_plot:
  try:
    country_data = hcpi_a_original_transposed.loc[years_to_plot, country]
    plt.hist(country_data, bins=20, alpha=0.5, label=country)
  except:
    print(f"Could not plot data for {country}")

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Inflation Data for Selected Countries (1970-2023)')
plt.legend()

# Show the plot
plt.show()

# visualization of mean and median of all inflation from 1980 to 2023

years_to_plot = list(range(1980, 2024))
mean_inflation = hcpi_a_original_transposed.loc[years_to_plot].mean(axis=1)
median_inflation = hcpi_a_original_transposed.loc[years_to_plot].median(axis=1)
plt.figure(figsize=(12, 6))
plt.plot(years_to_plot, mean_inflation, label='Mean Inflation')
plt.plot(years_to_plot, median_inflation, label='Median Inflation')
plt.xlabel('Year')
plt.ylabel('Inflation')
plt.title('Mean and Median Inflation (1980-2023)')
plt.legend()
plt.show()

# line dataframe visualization with height of 20
import plotly.express as px

years_to_plot = list(range(1970, 2024))
fig = px.line(
    hcpi_a_original_transposed.loc[years_to_plot],
    height=600
)
fig.update_layout(
    title="Inflation Data for All Countries (1970-2023)",
    xaxis_title="Year",
    yaxis_title="Inflation",
)
fig.show()

# value between negative max  and postitive max

years_to_plot = list(range(1980, 2024))

min_inflation = hcpi_a_original_transposed.loc[years_to_plot].min(axis=1)
max_inflation = hcpi_a_original_transposed.loc[years_to_plot].max(axis=1)
plt.figure(figsize=(12, 6))
plt.plot(years_to_plot, min_inflation, label='Minimum Inflation')
plt.plot(years_to_plot, max_inflation, label='Maximum Inflation')
plt.xlabel('Year')
plt.ylabel('Inflation')
plt.title('Minimum and Maximum Inflation (1980-2023)')
plt.legend()
plt.show()

years_to_plot = list(range(1970, 2024))
fig = px.line(
    hcpi_a_original_transposed.loc[years_to_plot],
    height=900,
    log_y=True
)
fig.update_layout(
    title="Inflation Data for All Countries (1970-2023)",
    xaxis_title="Year",
    yaxis_title="Inflation (Log Scale)",
)
fig.show()
plt.style.use('ggplot')

years_to_plot = list(range(1970, 2024))
average_inflation = hcpi_a_original_transposed.loc[years_to_plot].mean(axis=1)
plt.figure(figsize=(12, 6))
plt.plot(years_to_plot, average_inflation, label='Average Inflation')

plt.xlabel('Year')
plt.ylabel('Inflation')
plt.title('Average Inflation Rate (1970-2023)')
plt.legend()
plt.show()

# prompt: now apply adf and kpss test and compare stationarity for india

from statsmodels.tsa.stattools import adfuller, kpss

india_data = india_data.dropna()

# ADF Test
result_adf = adfuller(india_data)
print('ADF Statistic:', result_adf[0])
print('p-value:', result_adf[1])
print('Critical Values:', result_adf[4])

# KPSS Test
result_kpss = kpss(india_data)
print('\nKPSS Statistic:', result_kpss[0])
print('p-value:', result_kpss[1])
print('Critical Values:', result_kpss[3])


# Interpretation
print("\nInterpretation:")

if result_adf[1] <= 0.05:
    print("ADF test suggests that the data is stationary.")
else:
    print("ADF test suggests that the data is not stationary.")

if result_kpss[1] <= 0.05:
     print("KPSS test suggests that the data is not stationary.")
else:
    print("KPSS test suggests that the data is stationary.")

# adf and kpss for all countries
years_to_plot = list(range(1970, 2024))
countries = hcpi_a_original_transposed.columns.tolist()
results = []

# Loop through each country and perform ADF and KPSS tests
for country in countries:
    try:
        country_data = hcpi_a_original_transposed.loc[years_to_plot, country]
        country_data = country_data.dropna()

        # ADF Test
        result_adf = adfuller(country_data)
        adf_statistic = result_adf[0]
        adf_p_value = result_adf[1]

        # KPSS Test
        result_kpss = kpss(country_data)
        kpss_statistic = result_kpss[0]
        kpss_p_value = result_kpss[1]

        # Interpretation
        adf_stationary = "Stationary" if result_adf[1] <= 0.05 else "Non-Stationary"
        kpss_stationary = "Stationary" if result_kpss[1] > 0.05 else "Non-Stationary"

        results.append([country, adf_stationary, kpss_stationary])

        print(f"Country: {country}")
        print("ADF Test:")
        print(f"  ADF Statistic: {adf_statistic:.4f}")
        print(f"  p-value: {adf_p_value:.4f}")
        print("KPSS Test:")
        print(f"  KPSS Statistic: {kpss_statistic:.4f}")
        print(f"  p-value: {kpss_p_value:.4f}")
        print(f"ADF Stationary: {adf_stationary}, KPSS Stationary: {kpss_stationary}\n")

    except Exception as e:
        print(f"Could not perform tests for {country}: {e}")


# Create a DataFrame from the results
results_df = pd.DataFrame(results, columns=['Country', 'ADF Stationary', 'KPSS Stationary'])

# Print the results DataFrame
print("\nSummary of Stationarity Results:")
results_df

# prompt: check trend seasonality and residual with original

from statsmodels.tsa.seasonal import seasonal_decompose

india_data = india_data.dropna()
decomposition = seasonal_decompose(india_data, model='additive', period=1)  # You may need to adjust the period
# Extract the components
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid
# Plot the original data, trend, seasonality, and residual
plt.figure(figsize=(12, 8))
plt.subplot(411)
plt.plot(india_data, label='Original')
plt.legend(loc='best')
plt.title('Time Series Decomposition')
plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(seasonal, label='Seasonality')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(residual, label='Residual')
plt.legend(loc='best')

plt.tight_layout()
plt.show()

# You can also analyze the trend, seasonality, and residual components separately
plt.figure(figsize=(12, 6))
plt.plot(india_data, label='Original')
plt.plot(trend, label='Trend')
plt.legend()
plt.title('Original Data vs. Trend')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(india_data, label='Original')
plt.plot(seasonal, label='Seasonality')
plt.legend()
plt.title('Original Data vs. Seasonality')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(india_data, label='Original')
plt.plot(residual, label='Residual')
plt.legend()
plt.title('Original Data vs. Residual')
plt.show()



# Melt the DataFrame to transform it from wide to long format
hcpi_a_long = pd.melt(hcpi_a_original, id_vars=['Country'], var_name='Year', value_name='Inflation')

# Convert the 'Year' column to numeric (if it's not already)
hcpi_a_long['Year'] = pd.to_numeric(hcpi_a_long['Year'], errors='coerce')

# Sort the DataFrame by Country and Year
hcpi_a_long = hcpi_a_long.sort_values(['Country', 'Year'])

# Now you have a time series dataset in hcpi_a_long with columns:
# - Country
# - Year
# - Inflation

print(hcpi_a_long)

hcpi_a_long

hcpi_a_long

# prompt: remove nan from hcpi_a_long

# Assuming you have the hcpi_a_long DataFrame as defined in your code.

# Remove rows with NaN values in the 'Inflation' column
hcpi_a_long = hcpi_a_long.dropna(subset=['Inflation'])

# Now hcpi_a_long contains only rows where 'Inflation' is not NaN.

hcpi_a_long

"""we would go for adf as kpss p value is more than actual value
......
"""

# prompt: do kpss test and adf test and compare the test results

# Assuming you have the hcpi_a_long DataFrame as defined in your code.

# Filter data for the years 1970 to 2023
hcpi_a_long_filtered = hcpi_a_long[(hcpi_a_long['Year'] >= 1970) & (hcpi_a_long['Year'] <= 2023)]

# Perform ADF and KPSS tests for each country
adf_results = {}
kpss_results = {}
for country in hcpi_a_long_filtered['Country'].unique():
    country_data = hcpi_a_long_filtered[hcpi_a_long_filtered['Country'] == country]
    adf_result = adfuller(country_data['Inflation'])
    kpss_result = kpss(country_data['Inflation'])
    adf_results[country] = adf_result
    kpss_results[country] = kpss_result

# Compare the test results and classify countries
stationary_countries_adf = []
non_stationary_countries_adf = []
stationary_countries_kpss = []
non_stationary_countries_kpss = []

for country in hcpi_a_long_filtered['Country'].unique():
    adf_p_value = adf_results[country][1]
    kpss_p_value = kpss_results[country][1]

    if adf_p_value <= 0.05:
        stationary_countries_adf.append(country)
    else:
        non_stationary_countries_adf.append(country)

    if kpss_p_value <= 0.05:
        stationary_countries_kpss.append(country)
    else:
        non_stationary_countries_kpss.append(country)

# Print the results
print("Countries likely stationary according to ADF test:")
print(stationary_countries_adf)
print("\nCountries likely non-stationary according to ADF test:")
print(non_stationary_countries_adf)
print("\nCountries likely stationary according to KPSS test:")
print(stationary_countries_kpss)
print("\nCountries likely non-stationary according to KPSS test:")
non_stationary_countries_kpss

# prompt: now use double exponential smoothing

def double_exponential_smoothing(series, alpha, beta):
  """
  Performs double exponential smoothing on a time series.

  Args:
    series: The time series data as a list or pandas Series.
    alpha: The smoothing factor for the level.
    beta: The smoothing factor for the trend.

  Returns:
    A list containing the smoothed values.
  """

  level = series[0]
  trend = series[1] - series[0]
  smoothed_values = [series[0], series[1]]

  for i in range(2, len(series)):
    new_level = alpha * series[i] + (1 - alpha) * (level + trend)
    new_trend = beta * (new_level - level) + (1 - beta) * trend
    level = new_level
    trend = new_trend
    smoothed_values.append(level + trend)

  return smoothed_values

# Example usage:
# Assuming you want to apply double exponential smoothing to the inflation data of India
india_data_list = india_data.tolist()

# You need to choose appropriate alpha and beta values based on your data
alpha = 0.2
beta = 0.1
smoothed_india_data = double_exponential_smoothing(india_data_list, alpha, beta)

# Plot the original and smoothed data
plt.figure(figsize=(12, 6))
plt.plot(years_to_plot, india_data, label='Original Inflation Data')
plt.plot(years_to_plot, smoothed_india_data, label='Smoothed Inflation Data')
plt.xlabel('Year')
plt.ylabel('Inflation')
plt.title('Double Exponential Smoothing for India')
plt.legend()
plt.show()

# prompt: do double exponential for all countries

def double_exponential_smoothing(series, alpha, beta):
  """
  Performs double exponential smoothing on a time series.

  Args:
    series: The time series data as a list or pandas Series.
    alpha: The smoothing factor for the level.
    beta: The smoothing factor for the trend.

  Returns:
    A list containing the smoothed values.
  """

  level = series[0]
  trend = series[1] - series[0]
  smoothed_values = [series[0], series[1]]

  for i in range(2, len(series)):
    new_level = alpha * series[i] + (1 - alpha) * (level + trend)
    new_trend = beta * (new_level - level) + (1 - beta) * trend
    level = new_level
    trend = new_trend
    smoothed_values.append(level + trend)

  return smoothed_values

# Assuming you have the hcpi_a_original_transposed DataFrame as defined in your code.

# Select the years from 1970 to 2023
years_to_plot = list(range(1970, 2024))

# Get a list of all countries
countries = hcpi_a_original_transposed.columns.tolist()

# Loop through each country and apply double exponential smoothing
for country in countries:
  try:
    country_data = hcpi_a_original_transposed.loc[years_to_plot, country]
    country_data_list = country_data.tolist()

    # You need to choose appropriate alpha and beta values based on your data
    alpha = 0.2
    beta = 0.1
    smoothed_country_data = double_exponential_smoothing(country_data_list, alpha, beta)

    # Plot the original and smoothed data
    plt.figure(figsize=(12, 6))
    plt.plot(years_to_plot, country_data, label='Original Inflation Data')
    plt.plot(years_to_plot, smoothed_country_data, label='Smoothed Inflation Data')
    plt.xlabel('Year')
    plt.ylabel('Inflation')
    plt.title(f'Double Exponential Smoothing for {country}')
    plt.legend()
    plt.show()

  except:
    print(f"Could not plot data for {country}")

years_to_plot = list(range(1970, 2024))

# Get a list of all countries
countries = hcpi_a_original_transposed.columns.tolist()

# Loop through each country and apply double exponential smoothing
for country in countries:
  try:
    country_data = hcpi_a_original_transposed.loc[years_to_plot, country]
    # Convert the data to numeric type, handling potential errors
    country_data = pd.to_numeric(country_data, errors='coerce')
    country_data_list = country_data.dropna().tolist()  # Remove NaN values before smoothing


    # You need to choose appropriate alpha and beta values based on your data
    alpha = 0.2
    beta = 0.1
    smoothed_country_data = double_exponential_smoothing(country_data_list, alpha, beta)

    # Plot the original and smoothed data
    plt.figure(figsize=(12, 6))
    plt.plot(years_to_plot[:len(country_data_list)], country_data_list, label='Original Inflation Data')
    plt.plot(years_to_plot[:len(smoothed_country_data)], smoothed_country_data, label='Smoothed Inflation Data')
    plt.xlabel('Year')
    plt.ylabel('Inflation')
    plt.title(f'Double Exponential Smoothing for {country}')
    plt.legend()
    plt.show()

  except Exception as e:
    print(f"Could not plot data for {country}: {e}")

from statsmodels.tsa.arima.model import ARIMA
years_to_plot = list(range(1970, 2024))

countries = hcpi_a_original_transposed.columns.tolist()

for country in countries:
  try:
    country_data = hcpi_a_original_transposed.loc[years_to_plot, country]
    country_data = pd.to_numeric(country_data, errors='coerce')
    country_data = country_data.dropna()

    # Fit the ARIMA model (you may need to adjust the order based on your data)
    model = ARIMA(country_data, order=(5, 1, 0))
    model_fit = model.fit()

    print(f"\nARIMA Model for {country}:")
    print(model_fit.summary())

    # You can also make forecasts using the fitted model
    # forecasts = model_fit.forecast(steps=5)  # Forecast the next 5 years

  except Exception as e:
    print(f"Could not fit ARIMA model for {country}: {e}")

# prompt: perform acf and pacf

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Assuming you have the hcpi_a_long_filtered DataFrame as defined in your code.

# Choose a country for ACF and PACF analysis
country_to_analyze = 'India'
country_data = hcpi_a_long_filtered[hcpi_a_long_filtered['Country'] == country_to_analyze]

# Create a time series object
country_series = pd.Series(country_data['Inflation'].values, index=country_data['Year'])

# Plot the ACF
plot_acf(country_series, lags=20)
plt.title(f'ACF for {country_to_analyze}')
plt.show()

# Plot the PACF
plot_pacf(country_series, lags=20)
plt.title(f'PACF for {country_to_analyze}')
plt.show()

years_to_plot = list(range(1970, 2023))

# Get India's data
india_data = hcpi_a_original_transposed.loc[years_to_plot, 'India']

# Convert the data to numeric type, handling potential errors
india_data = pd.to_numeric(india_data, errors='coerce')
india_data = india_data.dropna()  # Remove NaN values


# Fit the ARIMA model (you may need to adjust the order based on your data)
model = ARIMA(india_data, order=(5, 1, 0))  # Example order (p, d, q)
model_fit = model.fit()

# Print the model summary
print("\nARIMA Model for India:")
print(model_fit.summary())


# Forecast the next 3 years
forecast_steps = 3
forecast_years = [2023,2024, 2025]
forecasts = model_fit.forecast(steps=forecast_steps)

# Print the forecast results
print("\nInflation Forecast for India:")
for year, forecast in zip(forecast_years, forecasts):
  print(f"{year}: {forecast:.2f}")

# Plot the original data and the forecast
plt.figure(figsize=(12, 6))
plt.plot(india_data.index, india_data.values, label='Historical Inflation')
plt.plot(forecast_years, forecasts, label='Forecast', marker='o')
plt.xlabel('Year')
plt.ylabel('Inflation')
plt.title('Inflation Forecast for India')
plt.legend()
plt.show()

# prompt: now forecast for all countries

# Assuming you have the hcpi_a_original_transposed DataFrame as defined in your code.

# Select the years from 1970 to 2023
years_to_plot = list(range(1970, 2023))

# Get a list of all countries
countries = hcpi_a_original_transposed.columns.tolist()

# Loop through each country and fit an ARIMA model, then forecast
for country in countries:
  try:
    country_data = hcpi_a_original_transposed.loc[years_to_plot, country]
    # Convert the data to numeric type, handling potential errors
    country_data = pd.to_numeric(country_data, errors='coerce')
    country_data = country_data.dropna()  # Remove NaN values

    # Fit the ARIMA model (you may need to adjust the order based on your data)
    model = ARIMA(country_data, order=(5, 1, 0))  # Example order (p, d, q)
    model_fit = model.fit()

    # Forecast the next 2 years
    forecast_steps = 2
    forecast_years = [2024, 2025]
    forecasts = model_fit.forecast(steps=forecast_steps)

    # Print the forecast results
    print(f"\nInflation Forecast for {country}:")
    for year, forecast in zip(forecast_years, forecasts):
      print(f"{year}: {forecast:.2f}")

    # Plot the original data and the forecast
    plt.figure(figsize=(12, 6))
    plt.plot(country_data.index, country_data.values, label='Historical Inflation')
    plt.plot(forecast_years, forecasts, label='Forecast', marker='o')
    plt.xlabel('Year')
    plt.ylabel('Inflation')
    plt.title(f'Inflation Forecast for {country}')
    plt.legend()
    plt.show()


  except Exception as e:
    print(f"Could not fit ARIMA model for {country}: {e}")

# prompt: do metrics of above arima model

from sklearn.metrics import mean_squared_error, mean_absolute_error

# Assuming you have the hcpi_a_original_transposed DataFrame and years_to_plot as defined in your code.

# Get a list of all countries
countries = hcpi_a_original_transposed.columns.tolist()

# Loop through each country and fit an ARIMA model, then forecast and evaluate
for country in countries:
  try:
    country_data = hcpi_a_original_transposed.loc[years_to_plot, country]
    # Convert the data to numeric type, handling potential errors
    country_data = pd.to_numeric(country_data, errors='coerce')
    country_data = country_data.dropna()  # Remove NaN values

    # Split the data into training and testing sets (e.g., last 5 years for testing)
    train_data = country_data[:-5]
    test_data = country_data[-5:]

    # Fit the ARIMA model on the training data
    model = ARIMA(train_data, order=(5, 1, 0))  # Example order (p, d, q)
    model_fit = model.fit()

    # Forecast on the test data
    forecasts = model_fit.forecast(steps=len(test_data))

    # Calculate metrics for the forecast
    mse = mean_squared_error(test_data, forecasts)
    mae = mean_absolute_error(test_data, forecasts)
    rmse = np.sqrt(mse)

    # Print the forecast results and metrics
    print(f"\nARIMA Model for {country}:")
    print(f"MSE: {mse:.2f}")
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")

    # Plot the original data and the forecast
    plt.figure(figsize=(12, 6))
    plt.plot(train_data.index, train_data.values, label='Training Data')
    plt.plot(test_data.index, test_data.values, label='Actual Inflation')
    plt.plot(test_data.index, forecasts, label='Forecast', marker='o')
    plt.xlabel('Year')
    plt.ylabel('Inflation')
    plt.title(f'Inflation Forecast for {country}')
    plt.legend()
    plt.show()

  except Exception as e:
    print(f"Could not fit ARIMA model for {country}: {e}")

# prompt: dash visualization with future forecast

import plotly.graph_objects as go


countries = hcpi_a_original_transposed.columns.tolist()

# Loop through each country and fit an ARIMA model, then forecast and create a Plotly visualization
for country in countries:
  try:
    country_data = hcpi_a_original_transposed.loc[years_to_plot, country]
    # Convert the data to numeric type, handling potential errors
    country_data = pd.to_numeric(country_data, errors='coerce')
    country_data = country_data.dropna()  # Remove NaN values

    # Split the data into training and testing sets (e.g., last 5 years for testing)
    train_data = country_data[:-5]
    test_data = country_data[-5:]

    # Fit the ARIMA model on the training data
    model = ARIMA(train_data, order=(5, 1, 0))  # Example order (p, d, q)
    model_fit = model.fit()

    # Forecast on the test data
    forecasts = model_fit.forecast(steps=len(test_data))

    # Create a Plotly figure
    fig = go.Figure()

    # Add the historical data
    fig.add_trace(go.Scatter(x=train_data.index, y=train_data.values, mode='lines', name='Training Data'))
    fig.add_trace(go.Scatter(x=test_data.index, y=test_data.values, mode='lines', name='Actual Inflation'))
    fig.add_trace(go.Scatter(x=test_data.index, y=forecasts, mode='lines', name='Forecast'))

    # Customize the layout
    fig.update_layout(
        title=f'Inflation Forecast for {country}',
        xaxis_title='Year',
        yaxis_title='Inflation',
        showlegend=True
    )

    # Show the plot
    fig.show()

  except Exception as e:
    print(f"Could not fit ARIMA model for {country}: {e}")

!pip install dash
!pip install dash-core-components
!pip install dash-html-components

# prompt: an dash app for visualization for each country


import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

# Assuming you have the hcpi_a_original_transposed DataFrame and years_to_plot as defined in your code.

# Get a list of all countries
countries = hcpi_a_original_transposed.columns.tolist()

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children="Inflation Forecast for Countries"),

    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in countries],
        value=countries[0]  # Default selected country
    ),

    dcc.Graph(id='inflation-forecast-graph')
])

# Define the callback function to update the graph based on the selected country
@app.callback(
    dash.Output('inflation-forecast-graph', 'figure'),
    [dash.Input('country-dropdown', 'value')]
)
def update_graph(selected_country):
  try:
    country_data = hcpi_a_original_transposed.loc[years_to_plot, selected_country]
    # Convert the data to numeric type, handling potential errors
    country_data = pd.to_numeric(country_data, errors='coerce')
    country_data = country_data.dropna()  # Remove NaN values

    # Split the data into training and testing sets (e.g., last 5 years for testing)
    train_data = country_data[:-5]
    test_data = country_data[-5:]

    # Fit the ARIMA model on the training data (replace with your preferred model)
    model = ARIMA(train_data, order=(5, 1, 0))  # Example order (p, d, q)
    model_fit = model.fit()

    # Forecast on the test data
    forecasts = model_fit.forecast(steps=len(test_data))

    # Create a Plotly figure
    fig = px.line(
        x=train_data.index.tolist() + test_data.index.tolist(),
        y=train_data.values.tolist() + test_data.values.tolist(),
        title=f'Inflation Forecast for {selected_country}',
        labels={'x': 'Year', 'y': 'Inflation'}
    )

    # Add forecast data to the plot
    fig.add_scatter(x=test_data.index, y=forecasts, mode='lines', name='Forecast')

    return fig

  except Exception as e:
    print(f"Could not fit ARIMA model for {selected_country}: {e}")
    return px.line(
        title=f"No data available for {selected_country}",
        labels={'x': 'Year', 'y': 'Inflation'}
    )

# Run the app
if __name__ == '__main__':
  app.run_server(debug=True)

# prompt: NOW USE GOOGLE  CHARTS FOR ALL COUNTRIES DATA FORECASTING AND VIEW VISUALIZATION IN WORLD MAP

!pip install pycountry
!pip install googlemaps

import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Assuming you have the hcpi_a_original_transposed DataFrame and years_to_plot as defined in your previous code.
# ... (your existing code to load and process the data) ...

countries = hcpi_a_original_transposed.columns.tolist()
years_to_plot = list(range(1970, 2023))  # Or your preferred years

# Create a dictionary to store country data and forecasts
country_forecasts = {}

for country in countries:
    try:
        country_data = hcpi_a_original_transposed.loc[years_to_plot, country]
        country_data = pd.to_numeric(country_data, errors='coerce')
        country_data = country_data.dropna()

        # Fit your ARIMA model (or any other forecasting model) here
        # ...
        # Example ARIMA (replace with your actual model and parameters)
        from statsmodels.tsa.arima.model import ARIMA
        model = ARIMA(country_data, order=(1, 1, 1))
        model_fit = model.fit()

        forecast_steps = 3
        forecasts = model_fit.forecast(steps=forecast_steps)

        country_forecasts[country] = forecasts.tolist()  # Store as a list


    except Exception as e:
        print(f"Could not process data for {country}: {e}")
        country_forecasts[country] = [None, None] # Placeholders for missing data


import pycountry

# Function to get country code (alpha-3)
def get_country_code(country_name):
    try:
        country = pycountry.countries.search_fuzzy(country_name)[0]
        return country.alpha_3
    except LookupError:
        return None

# Create a list of locations and values for the world map
locations = []
z = []
for country, forecast in country_forecasts.items():
  try:
    code = get_country_code(country)
    if code and forecast[0]: # Add to locations and z only if country code is found and the forecast exists.
        locations.append(code)
        z.append(forecast[0])
  except:
    print(f"Error processing country: {country}")

# Create the choropleth map using Plotly
fig = go.Figure(data=go.Choropleth(
    locations=locations,
    z=z,
    text=locations,  # Display country codes on hover
    colorscale='Viridis',  # Choose a colorscale
    autocolorscale=False,
    reversescale=True,  # Reverse the colorscale
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title='Inflation Forecast',colorbar=dict(
        tickvals=[min(z), max(z)],
        ticktext=['Low', 'High'],
        title='Inflation Forecast',
        titleside='right'
    )
))

fig.update_layout(
    title_text='Inflation Forecast for Countries (2024)',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations=[dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Source: <a href="your_data_source_here"></a>',
        showarrow=False
    )]
)

fig.show()

