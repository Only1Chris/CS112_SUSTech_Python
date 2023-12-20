home = input().split()
construct = int(input())
homex = int(home[0])
homey = int(home[1])
construct_crossing = []
for i in range(construct):
    construct_crossing.append(input().split())
tables = []
for i in range(homex + 1):
    tables.append([])
for i in range(homex + 1):
    for j in range(homey + 1):
        if [str(i), str(j)] in construct_crossing:
            tables[i].append(0)
        elif i == 0:
            if j == 0:
                tables[i].append(1)
            elif tables[i][j - 1] == 0:
                tables[i].append(0)
            else:
                tables[i].append(1)
        elif j == 0:
            if tables[i - 1][j] == 0:
                tables[i].append(0)
            else:
                tables[i].append(1)
        else:
            tables[i].append(tables[i - 1][j] + tables[i][j - 1])

print(tables[-1][-1])