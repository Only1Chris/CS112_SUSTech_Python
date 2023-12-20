m = int(input())
star = {}
star_low = {}
star_high = {}
count = {}
cmt_low = {}
cmt_high = {}
for i in range(m):
    line = eval(input())
    value = list(line.values())

    if value[0] not in star.keys():
        count[value[0]] = 1
        star[value[0]] = value[1]
        star_low[value[0]] = value[1]
        star_high[value[0]] = value[1]
        cmt_low[value[0]] = value[2]
        cmt_high[value[0]] = value[2]
    else:
        count[value[0]] += 1
        star[value[0]] += value[1]
        if value[1] > star_high[value[0]]:
            star_high[value[0]] = value[1]
            cmt_high[value[0]] = value[2]
        elif value[1] < star_low[value[0]]:
            star_low[value[0]] = value[1]
            cmt_low[value[0]] = value[2]

key = []
for keys in star.keys():
    star[keys] = round(star[keys] / count[keys], 3)
    if keys not in key:
        key.append(keys)
key.sort()
avgstar = sum(star.values()) / len(star.keys())

print("Problem_ID;Star;Comment")
for keys in key:
    if star[keys] >= avgstar:
        print(keys + ';' + '{:.2f}'.format(star[keys]) + ';' + cmt_high[keys])
    else:
        print(keys + ';' + '{:.2f}'.format(star[keys]) + ';' + cmt_low[keys])
