import yfinance as yf
stock_list = ['0005.HK', '0006.HK', '0066.HK', '0700.HK', '2800.HK']
print('stock_list:', stock_list)
data = yf.download(stock_list, start="2015-01-01", end="2020-02-21")
print('data fields downloaded:', set(data.columns.get_level_values(0)))
data.head()