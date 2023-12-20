poker = []
for i in range(3):
    p = input().split(',')
    for j in range(3):
        p[j] = int(p[j])
        if p[j] == 1:
            p[j] = 14

    p.sort(reverse=True)
    sorted(p,reverse=True)

    if p[0] == p[1] == p[2]:
        poker.append([300, p[0], p[1], p[2]])
    elif p[0] == p[1] or p[1] == p[2]:
        poker.append([100, p[0], p[1], p[2]])
    elif p[0] - 1 == p[1] and p[1] - 1 == p[2]:
        poker.append([200, p[0], p[1], p[2]])
    # elif p[0] == 1 and p[1] == 2 and p[2] == 3:
    #     poker.append([200, p[2], p[1], p[0]])
    # elif p[0] == 12 and p[1] == 13 and p[2] == 1:
    #     poker.append([200, p[2], p[1], p[0]])
    else:
        poker.append([0, p[0], p[1], p[2]])
    # for j in range(1,4):
    #     if poker[i][j]==1:
    #         poker[i][j]=14

if __name__ == "__main__":
    if poker[0] > poker[1] and poker[0] > poker[2]:
        print("player1 is the winner")
    elif poker[1] > poker[0] and poker[1] > poker[2]:
        print("player2 is the winner")
    elif poker[2] > poker[0] and poker[2] > poker[1]:
        print("player3 is the winner")
