import math
n=int(input())
# def se(n):
#     number=0
#     for i in range(math.floor(n/2)+1):
#         number+=math.comb(n-i,i)
#     return number

def se(n):
    a=1
    b=2
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        for i in range(n-1):
            a,b=b,a+b
        return a


if __name__=='__main__':
    print(se(n))