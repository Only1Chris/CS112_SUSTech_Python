import pandas as pd

country = list(input().split(','))
year = int(input())
if year >= 2024:
    print("Happy every day!")
else:
    file1 = pd.read_csv('life_expectancy.csv')
    df = file1[file1['Year'] == year].sort_values(by='Life expectancy', ascending=False)
    for i in range(len(df)):
        if df['Entity'].iloc[i] not in country:

            i -= 1

    print(','.join(df['Code']))
