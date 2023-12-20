filename=input()
with open(filename) as file:
    lst=[]
    for line in file:
        lst.append(line.strip('\n'))


for i in range(3,len(lst),2):
    sim=0
    if len(lst[1])>len(lst[i]):
        for j in range(len(lst[i])):
            if lst[i][j]==lst[1][j]:
                sim+=1
        print(round(sim/len(lst[i]),3))
    else:
        for j in range(len(lst[1])):
            if lst[i][j]==lst[1][j]:
                sim+=1
        print(round(sim/len(lst[1]),3))
