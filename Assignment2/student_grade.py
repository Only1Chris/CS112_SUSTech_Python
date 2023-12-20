students={'Alice':85,'Bob':90,'Chaelie':75,'David':92,}
total_score=0
max=max(students.values())
for score in students.values():
    total_score+=score
count=len(students)
avg=total_score/count if count>0 else 0
print("学生人数",count)
print("最高分",max)
print("平均分",avg)

def fb(n):
    lst=[1,1]
    for i in range(2,n+1):
        lst.append(lst[i-2]+lst[i-1])
    print(lst[n])