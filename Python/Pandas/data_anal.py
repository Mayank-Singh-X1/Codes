import pandas as pd

data = pd.read_csv(r"D:\BOOKS\1. Weather Data.csv")

# print(data.head())        print first n lines of data | 5 is default value

# print(data.shape)         prints shape of data , (8784, 8) for this data set

# print(data.index)         prints index range RangeIndex(start=0, stop=8784, step=1)

# print(data.columns)       prints columns names of data set

# print(data.dtypes)          data type of every column

# data['Weather'].unique()  prints unique values from column | 'weather' is the column name

# print(data['Weather'].nunique()) prints no. of unique data
# print(data['Weather'].nunique(), data['Temp_C'].nunique()) 
# print(data.info()) prints data 