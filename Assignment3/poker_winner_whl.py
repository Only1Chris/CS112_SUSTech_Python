def type_check(a):
    res1 = int(a[0]) == int(a[1])+1 == int(a[2])-1 or int(a[1]) == int(a[0])+1 == int(a[2])-1 or int(a[2]) == int(a[0])+1 == int(a[2])-1
    res2 = int(a[0]) == int(a[2])+1 == int(a[1])-1 or int(a[1]) == int(a[2])+1 == int(a[0])-1 or int(a[2]) == int(a[1])+1 == int(a[0])-1
    if int(a[0]) == int(a[1]) == int(a[2]):
        return 4
    elif int(a[0]) == int(a[1]) != int(a[2]) or int(a[0]) == int(a[2]) != int(a[1]) or int(a[2]) == int(a[1]) != int(a[0]):
        return 2
    elif res1 or res2:
        return 3
    else:
        return 1
# 先判断是什么类型 根据不同的类型从低到高输出数字



player1 = input().split(",")
for i in range(0, 3):
    if player1[i] == "1":
        player1[i] = 14

player1 = list(map(int, player1))
player2 = input().split(",")
for i in range(0, 3):
    if player2[i] == "1":
        player2[i] = 14
player2 = list(map(int, player2))
player3 = input().split(",")
for i in range(0, 3):
    if player3[i] == "1":
        player3[i] = 14
# 把所有的1换成14

player3 = list(map(int, player3))
p1 = type_check(player1)
p2 = type_check(player2)
p3 = type_check(player3)
player1 = sorted(player1)
player2 = sorted(player2)
player3 = sorted(player3)
player1.reverse()
player2.reverse()
player3.reverse()
re1 = [p1] + player1
re2 = [p2] + player2
re3 = [p3] + player3
# 这里list里面有四个数，第一个数代表种类，后面三个是扑克牌从大到小。如果种类不同，比第一个就行，如果种类相同，就比后面的数字谁更大
result = [re1, re2, re3]
if max(result) == re1:
    print("player1 is the winner")
elif max(result) == re2:
    print("player2 is the winner")
elif max(result) == re3:
    print("player3 is the winner")