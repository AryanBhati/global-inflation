# global-inflation
DISCUSSION ON DATA:

Dataset Details
- Source: IMF & WORLDBANK 
- Period: 1970-2023
- Countries: Up to 198
- Inflation Measures: core consumer price inflation
- Frequencies: ANNUALLY
 

METHODOLOGY

1. Data Collection and Processing:
   - Data Acquisition: Collect data from the IMF and other credible sources.
   - Data Cleaning: Address missing values, outliers, and inconsistencies. Ensure data is normalized and comparable across different countries and time periods.
   - Data Integration: Combine data from various sources to form a comprehensive database.



 
3. Exploratory Data Analysis (EDA):
   - Descriptive Statistics: Calculate mean, median, standard deviation, and other statistical measures for the dataset.
   - Trend Analysis: Plot inflation trends over time for different regions and inflation measures.
   - Correlation Analysis: Examine the correlation between different inflation measures and economic indicators.



4. Model Development:

Machine Learning models we can use:
-	ARIMA (AutoRegressive Integrated Moving Average): Ideal for forecasting inflation based on past values by handling various forms of non-stationary data. ARIMA models can also capture seasonality when extended to Seasonal ARIMA (SARIMA).


5.Evaluation Metrics
•	Mean Absolute Error (MAE)
o	Measures the average magnitude of errors in predictions, without considering direction.
•	Mean Squared Error (MSE)
o	Measures the average of the squares of errors, giving more weight to larger errors.
•	Root Mean Squared Error (RMSE)
o	Measures the square root of the average of the squared errors, providing an indication of the magnitude of errors.
•	Partial Autocorrelation Function (PACF)
o	Used to identify the correlation between a time series and its lagged values, while controlling for the values of the intermediate lags. Helps in determining the order of an ARIMA model.
