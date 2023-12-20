import pandas as pd
category=input()
df=pd.read_csv(category+'.csv')
if category=='sweaters':
    print("The sweaters he can buy are:", ', '.join(df[df['price']<=200]['options'])+".")
elif category=='pants':
    print("The pants he can buy are:", ', '.join(df[df['price']<=300]['options'])+".")
elif category=='shoes':
    print("The shoes he can buy are:", ', '.join(df[df['price']<=400]['options'])+".")
elif category=='down coats':
    print("The down coats he can buy are:", ', '.join(df[df['price']<=500]['options'])+".")
    # 200 yuan for sweaters, 300 yuan for pants, 400 yuan for shoes, and 500 yuan for down coats.