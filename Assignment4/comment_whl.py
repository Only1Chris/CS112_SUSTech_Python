def average_star(s):
    b = 0
    a = len(s)
    for i in s:
        b += i
    return b / a


# l1 = []
l2 = []
# l3 = []
a = {}
total = 0
import json

number = int(input())
for i in range(0, number):
    b = json.loads(input())
    total += b["Star"] #计算总体平均分
    if b["Problem_ID"] not in l2:
        l2.append(b["Problem_ID"])
        a[b["Problem_ID"]] = {"Star": [b["Star"]], "Comments": [b["Comments"]]}
    else:
        if max(a[b["Problem_ID"]]["Star"]) < b["Star"]:
            a[b["Problem_ID"]]["Comments"].append(b["Comments"])
        elif min(a[b["Problem_ID"]]["Star"]) > b["Star"]:
            a[b["Problem_ID"]]["Comments"].insert(0, b["Comments"])
        a[b["Problem_ID"]]["Star"].append(b["Star"])
average = total / number
l2 = sorted(l2)
print("Problem_ID;Star;Comment")
for i in l2:
    star = round(average_star(a[i]['Star']), 2)
    stars = float(star)
    if len(str(star)) == 3:
        star = str(star) + "0"
        stars = float(star)
    if stars < average:
        comment = a[i]["Comments"][0]
    else:
        comment = a[i]["Comments"][-1]
    print(i + ";" + str(star) + ";" + comment)

