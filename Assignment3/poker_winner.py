p1 = input().split(',')
p2 = input().split(',')
p3 = input().split(',')
# poker=[]
# for i in range(3):

for i in range(3):
    p1[i] = int(p1[i])
    p2[i] = int(p2[i])
    p3[i] = int(p3[i])


def assign_type(p):
    if p[0] == p[1] == p[2]:
        return 3
    elif p[0] == p[1] or p[1] == p[2]:
        return 1
    elif p[0] + 1 == p[1] and p[1] + 1 == p[2]:
        return 2
    else:
        return 0


def comp2(p1, p2, m, n):
    for i in range(3):
        if p1[i] == 1:
            p1[i] = 14
        if p2[i] == 1:
            p2[i] = 14
    if p1[2] > p2[2]:
        return "player%i is the winner" % m
    elif p1[2] < p2[2]:
        return "player%i is the winner" % n
    elif p1[1] > p2[1]:
        return "player%i is the winner" % m
    elif p1[1] < p1[2]:
        return "player%i is the winner" % n
    elif p1[0] > p2[0]:
        return "player%i is the winner" % m
    elif p1[0] < p2[0]:
        return "player%i is the winner" % n
    else:
        return 0

if __name__=="__main__":
    t1 = assign_type(p1)
    t2 = assign_type(p2)
    t3 = assign_type(p3)

    if t1 > t2 and t1 > t3:
        print("player1 is the winner")
    elif t2 > t1 and t2 > t3:
        print("player2 is the winner")
    elif t3 > t1 and t3 > t2:
        print("player3 is the winner")
    elif t1 == t2 == t3:
        if comp2(p1, p2, 1, 2) == comp2(p1, p3, 1, 3):
            print("player1 is the winner")
        elif comp2(p1, p2, 1, 2) == comp2(p2, p3, 2, 3):
            print("player2 is the winner")
        elif comp2(p1, p3, 1, 3) == comp2(p2, p3, 2, 3):
            print("player3 is the winner")

    elif t1 == t2:
        print(comp2(p1, p2, 1, 2))
    elif t2 == t3:
        print(comp2(p2, p3, 2, 3))
    elif t1 == t3:
        print(comp2(p1, p3, 1, 3))

#  For card combinations, all three cards being the same is the biggest (5,5,5),
#  followed by straights (4,5,6),
#  pairs (4,4,5),
#  and finally singles (4,5,7). If the combinations are of the same type, compare the card numbers.
#  For single-card combinations, the three cards are weighted differently, comparing the largest card first, then the next.
