x, y = input().split()
x = int(x)
y = int(y)
dim = x + y
if x < y:
    x = y
    y = dim - y

if dim == 1:
    triangle = [1]
elif dim == 2:
    triangle = [[1], [1, 1]]
else:
    triangle = [[1], [1, 1]]
    for i in range(3, dim + 2, 1):
        trans_list = list(range(1, i + 1))
        triangle.append(trans_list)
# print(triangle) 建立好杨辉三角

n = int(input())
for i in range(n):
    x1, y1 = input().split()
    x1=int(x1)
    y1=int(y1)
    triangle[x1+y1][y1] = 0
for i in range(2,len(triangle)):
    for j in range(len(triangle[i])):
        if triangle[i][j]==0:
            pass
        elif j==0:
            triangle[i][j]=triangle[i-1][j]
        elif j==len(triangle[i])-1:
            triangle[i][j]=triangle[i-1][j-1]
        else:
            triangle[i][j]=triangle[i-1][j-1]+triangle[i-1][j]
print(triangle[x+y][y])
