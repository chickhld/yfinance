import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
sns.set()

# Date must be in the fromat ("%Y-%m-%d") That is, year-month-day
#start_date = '2020-1-1' #1 December 2020
#end_date = '2020-12-31'    #2 February 2023
# "start_date" must be an older date than the "end_date"

start_date_month = '-1-1'
end_date_month = '-12-30'

# Set Year range (eg 5 years)
start_year = 2017
end_year = 2023
range_year = end_year - start_year

start_range_date = []
end_range_date = []

datalist = []

plt.figure(figsize=(14,5))
sns.set_style("ticks")

print('============= Start  ============')

for x in range(range_year):

    # Get dates
    start_date = str(start_year + x) + start_date_month
    end_date = str(start_year + x) + end_date_month
    print("start_date:" + start_date)
    print("end_date:" + end_date)
    start_range_date.append(start_date)
    end_range_date.append(end_date)

    # extract stock data from yahoo finance
    #stock_name = "^AORD"
    stock_name = "CBA.AX"

    datadownland = yf.download(tickers = stock_name, start = start_date, end = end_date)
    datalist.append(datadownland)

    # print out downloaded columns
    print('data fields downloaded:', set(datadownland.columns.get_level_values(0)))

    # print entries (head takes out the first 5 entries (rows))
    print('============= Print Entries  ============')
    print(datadownland.head())
    
    # print type
    print('============= Print Whole Dataframe  ============') 
    print(type(datadownland))

    # print size (250, 6)
    print('============= Print Dataframe Size ============') 
    print(datadownland.shape)
    
    # print Index(['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], dtype='object')
    print('============= Print Dataframe Columns ============') 
    print(datadownland.columns)

    # print types of columns
    #Open         float64
    #High         float64
    #Low          float64
    #Close        float64
    #Adj Close    float64
    #Volume         int64
    print('============= Print Types of columns ============') 
    print(datadownland.dtypes)

    # print 
    print('============= Print Info ============') 
    print(datadownland.info())

    # print index
    print('============= Print Index ============') 
    print(datadownland.index)

    # add extra row_number column which we can potentially use as index
    #datadownland = datadownland.assign(row_number=range(len(datadownland)))
    #print(datadownland.head())

    # add extra row_number column which we can potentially use as index
    print('============= Print extra day column ============') 
    datadownland['day'] = datadownland.reset_index().index
    print(datadownland.head())

    print('============= Print new date column ============') 
    datadownland = datadownland.assign(date=datadownland.index)
    print(datadownland.head())

    print('============= Print new year column ============') 
    datadownland['year'] = pd.DatetimeIndex(datadownland['date']).year
    print(datadownland.head())

    # Single line plot
    #sns.lineplot(data=datadownland,x="day",y="High",color='blue')

    # different ways to define palette color
    #sns.lineplot(data=datadownland,x="day",y="High",hue='year', palette='spring')
    #sns.lineplot(data=datadownland,x="day",y="High",hue='year', palette=['magenta', 'deepskyblue', 'yellowgreen'])

    # Generate random numbers for colors
    r_rl = random.randint(0,255)
    g_rl = random.randint(0,255) 
    b_rl = random.randint(0,255)

    # Plot the line
    sns.lineplot(data=datadownland,x="day",y="High",hue='year', palette=[(r_rl/255, g_rl/255, b_rl/255)])


plt.title("All Ordinaries Chart",size='x-large',color='blue')
plt.show()

