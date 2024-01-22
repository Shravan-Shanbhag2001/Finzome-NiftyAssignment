# Importing required libraries
import pandas as pd
import math

# Read the CSV file into a DataFrame
nifty_df = pd.read_csv(r"C:\Users\Shreyas\Downloads\NIFTY_50.csv")

# Calculate daily returns using a loop
daily_returns_list = []

# Previous close value retrieved from given NSE website
previous_close = 18053.30  

# Iterate over the 'Close' column
for current_close in nifty_df['Close ']:
    # Calculate daily returns using the specified formula
    ret = (current_close / previous_close) - 1
    
    # Append the result to the list
    daily_returns_list.append(ret)

# Create a Series for daily returns with the 'Date' column as the index
daily_returns_Series = pd.Series(daily_returns_list, index=nifty_df['Date '])

# Display the Series
print("Daily Returns: \n",daily_returns_Series)

# Calculate daily volatility
daily_volatility = daily_returns_Series.std()
print("Daily Volatility:", daily_volatility)

# Get the length of the Series
length_Series = daily_returns_Series.size

# Calculate annualized volatility
Annualized_Volatility = daily_volatility * math.sqrt(length_Series)
print("Annualized Volatility:", Annualized_Volatility)
