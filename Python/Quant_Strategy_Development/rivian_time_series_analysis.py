import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch historical data for Rivian (RIVN)
print("Fetching Rivian (RIVN) stock data...")
rivian_data = yf.Ticker("RIVN")
rivian_hist = rivian_data.history(period="max")

# Reset index to make 'Date' a column
rivian_hist.reset_index(inplace=True)

# Check if data is available
if rivian_hist.empty:
    print("No data fetched for RIVN. Check the ticker or internet connection.")
else:
    print("Data fetched successfully!")

# Plot the closing prices
plt.figure(figsize=(10, 6))
plt.plot(rivian_hist['Date'], rivian_hist['Close'], label='Closing Price', linewidth=2)
plt.title('Rivian Stock Closing Prices Since Inception', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Closing Price (USD)', fontsize=12)
plt.grid(True)
plt.legend()
plt.show()

# Display basic statistics
rivian_stats = rivian_hist[['Close']].describe()
print("\nDescriptive Statistics for Rivian Closing Prices:")
print(rivian_stats)

# Calculate daily returns
rivian_hist['Daily Return'] = rivian_hist['Close'].pct_change()

# Plot daily returns
plt.figure(figsize=(10, 6))
plt.plot(rivian_hist['Date'], rivian_hist['Daily Return'], label='Daily Return', linewidth=1)
plt.title('Rivian Daily Returns Since Inception', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Daily Return', fontsize=12)
plt.grid(True)
plt.legend()
plt.show()