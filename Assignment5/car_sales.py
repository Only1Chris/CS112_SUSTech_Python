import pandas as pd

path=input()
# path="car_sales_1.csv"
file=pd.read_csv(path)
print(file.shape)
# print(tuple(file[file['Price']==file['Price'].max()].iloc[0,])[0:3:2])
expensive=file[file['Price']==file['Price'].max()][['Brand','Price']]
print(tuple(expensive.iloc[0,]))

# print(dict(file['Price'].groupby(file['Brand']).mean().convert_dtypes(int)))
print(dict(file['Price'].groupby(file['Brand']).mean().astype(int)))

print(tuple(file.loc[file['Year']>2015]['Model']))