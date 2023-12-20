import csv


def find_Cap(country):
    with open('CountryCapitals.csv') as file:
        reader = csv.reader(file)
        try:
            for row in reader:
                if row[0] == country:
                    return row[1]
            else:
                return 'Not found'
        except:
            return 'Not found'


country = input()
capital = find_Cap(country)
print(capital)
