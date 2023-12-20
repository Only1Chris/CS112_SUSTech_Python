import numpy as np

m=int(input())
arr=[]
for i in range(m):
    lst=list(map(int,input().split(',')))
    arr.append(lst)

arr=np.array(arr)
n=arr.shape[1]
A=arr[:,:n-1]
b=arr[:,n-1]
x = np.linalg.solve(A, b)

print(','.join(np.around(x,decimals=1).astype(str)))