fileName = input() + '.csv'
nameList = []

with open(fileName) as file:
    i = 0
    for line in file:
        i += 1
        if i == 2:
            capacity = line.split(',')[1]
            capacity = int(capacity)
        elif i > 6:
            lst = [0, 0]
            sid, points = line.split(',')
            lst[0] = int(sid)
            lst[1] = int(points)
            nameList.append(lst)


def same_points(capacity):
    if capacity == 0:
        return 0
    elif nameList[capacity - 1][1] == nameList[capacity][1]:
        capacity -= 1
        return same_points(capacity)
    else:
        return capacity

nameList.sort()
if len(nameList) <= capacity:

    for i in range(len(nameList)):
        print(nameList[i][0])
else:
    nameList.sort(key=(lambda x: x[1]), reverse=True)
    capacity=same_points(capacity)
    for i in range(capacity):
        print(nameList[i][0])
