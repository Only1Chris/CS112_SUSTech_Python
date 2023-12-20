import csv

with open('CountryCapitals.csv') as file:
    file.readline()
    csv_file=csv.reader(file)
    cap={}
    for line in csv_file:
        country, capital = line[0], line[1]
        cap.update({country:capital}) #.strip('\n')
        # cap[country]=capital

cname=input()
if cname in cap.keys():
    print(cap[cname])
else:
    print('Not found')