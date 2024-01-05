import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; 

sns.set()

# Date must be in the fromat ("%Y-%m-%d") That is, year-month-day
start_date = '2020-1-1' #1 December 2020
end_date = '2020-12-31'    #2 February 2023
# "start_date" must be an older date than the "end_date"

#stock_list = ['0005.HK', '0006.HK', '0066.HK', '0700.HK', '2800.HK']
stock_list = ['AMZN']
print('stock_list:', stock_list)

amazon = yf.download(stock_list, start = start_date, end = end_date)
#amazon = yf.download(tickers = "AMZN", start = start_date, end = end_date)

print('data fields downloaded:', set(amazon.columns.get_level_values(0)))

# You can see that “Date” is part of our DataFrame index. You need to convert
# it to a column to plot the data.
amazon.reset_index(inplace=True)
amazon.head()

# See raw data
#print(amazon)

plt.figure(figsize=(14,5))

sns.set_style("ticks")
sns.lineplot(data=amazon,x="Date",y='Close',color='firebrick')
sns.despine() # remove top and right lines

plt.title("The Stock Price of Amazon",size='x-large',color='blue')
plt.show()
