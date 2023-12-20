import pandas as pd

df=pd.read_csv(input())
# df=pd.read_csv('SalesData1.csv')

category=df['Category'].value_counts().index[0]

# print(str(round(df[df['Category']==category]['Price'].mean(),2))+','+category)
print(str(round(df['Price'].mean(),2))+','+category)