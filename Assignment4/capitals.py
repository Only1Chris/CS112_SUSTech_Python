import csv

def find_capital(country):
    with open('CountryCapitals.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == country:
                return row[1]
    return "Not found"

country = input()
capital = find_capital(country)
print(capital)