from math import factorial

(X, Y) = input().split(' ')
X = int(X)
Y = int(Y)
blockNum = int(input())


def C(n, m):
    if m <= n:
        a = factorial(n) / (factorial(n - m) * factorial(m))
    return int(a)


if blockNum == 0:
    ans = C(X + Y, X)
    print(ans)

if blockNum != 0:
    blockList = []
    for i in range(0, blockNum):
        (x, y) = input().split()
        blockList.append([int(x), int(y)])
    # print(blockList)
    matrix = []
    for i in range(0, Y + 1):
        row = []
        for j in range(0, X + 1):
            row.append(None)
        matrix.append(row)
    # print(matrix)

    for i in range(0, blockNum):
        matrix[blockList[i][1]][blockList[i][0]] = 0

    temp = 1
    for i in range(0, X + 1):
        if temp == 0:
            matrix[0][i] = 0
        elif matrix[0][i] != 0:
            matrix[0][i] = 1
        else:
            temp = 0
    temp = 1
    for i in range(0, Y + 1):
        if temp == 0:
            matrix[i][0] = 0
        elif matrix[i][0] != 0:
            matrix[i][0] = 1
        else:
            temp = 0
    # print(matrix)

    for i in range(1, Y + 1):
        for j in range(1, X + 1):
            if matrix[i][j] != 0:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    # for row in matrix:
    #     print(row)
    print(matrix[Y][X])