# dim = int(input())
# if dim == 1:
#     triangle = [1]
# elif dim == 2:
#     triangle = [[1],[1, 1]]
# else:
#     triangle=[[1],[1, 1]]
#     for i in range(3,dim+1,1):
#         trans_list=list(range(i))
#         trans_list[0] = 1
#         trans_list[i - 1] = 1
#         for j in range(1,i-1,1): #从1->i-2
#             trans_list[j]=triangle[i-2][j-1]+triangle[i-2][j]
#         print(trans_list)
#         triangle.append(trans_list)
# print(triangle)
dim = int(input())
if dim == 1:
    print(1)
elif dim == 2:
    print(1)
    print(1,1)
else:
    print(1)
    print(1,1)
    triangle=[[1],[1, 1]]
    for i in range(3,dim+1,1):
        trans_list=list(range(i))
        trans_list[0] = 1
        trans_list[i - 1] = 1
        for j in range(1,i-1,1): #从1->i-2
            trans_list[j]=triangle[i-2][j-1]+triangle[i-2][j]
        print(" ".join(map(str,trans_list)))
        triangle.append(trans_list)
# print(triangle)