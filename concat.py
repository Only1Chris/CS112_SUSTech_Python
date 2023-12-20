def concat(*args, sep='/'):
    return sep.join(args)


print(concat('footbar'))
print(concat('earth', 'mars', 'venus'), end="\n")
print(concat('earth', 'mars', 'venus', sep='.'))
print(concat('a', 'b', {'sep': '!'}))

a = {}
b = {x for x in 'language' if x not in 'aeiou'}
c = {x for x in 'python' if x not in 'aeiou'}
for elements in b & c:
    a.add(elements)


def func(length):
    print(length)


func(length=10)


def is_leap_year(yyyy):
    return (yyyy % 4 == 0 and yyyy % 100 != 0) or yyyy % 400 == 0


def is_valid_date(date_string):
    year, month, day = map(int, date_string.split('-'))
    if year < 1000 or year > 9999:
        return False
    if month < 1 or month > 12:
        return False
    if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if day < 1 or day > 31:
            return False
    elif month == 4 or 6 or 9 or 11:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if is_leap_year(year):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    return True


print(is_valid_date(input()))

import numpy as np

array=np.array([[-1,0,-1,-1,0],[0,0,0,-1,0],[-1,0,0,0,0],[0,0,0,0,0],[0,-1,0,0,0]])

def check(array,n):
    result=np.zeros(array.shape)
    board=np.zeros((array.shape[0]+2*n,array.shape[1]+2*n))
    board[n:n+array.shape[0],n:n+array.shape[1]]=array
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if board[n+i][n+j]==0:
                result[i][j]=-sum(sum(board[n+i-2:n+i+3,n+j-2:n+j+3]))
            elif board[n+i][n+j]==-1:
                result[i][j]=-1
    return result


def mine(array, n):
    """
    array: Game environment, also known as board. A numpy array.
    n: int
    """
    result = np.zeros(array.shape)

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            count = 0
            for x in range(max(0, i - n), min(array.shape[0], i + n + 1)):
                for y in range(max(0, j - n), min(array.shape[1], j + n + 1)):
                    if array[x, y] == -1:  # Assuming -1 represents a mine
                        count += 1
            if array[i,j]==-1:
                result[i,j]=-1
            else:
                result[i, j] = count

    return result
