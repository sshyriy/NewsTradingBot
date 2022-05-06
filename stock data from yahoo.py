
import numpy as np
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as dp
import datetime

start1 = datetime.datetime(2015, 5, 22)
end1 = datetime.datetime(2022, 1, 14)

df = dp.DataReader('^GSPC', 'yahoo', start=start1, end=end1)

print( df )

df['log_ret'] = np.log(df['Adj Close']/df['Adj Close'].shift(1))
print(df)



df.to_csv('C:\\Users\\operator\\Documents\\Python\\SP500CFAmonthly.csv')
