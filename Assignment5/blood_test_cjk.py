f1 = "registration_11_29.csv"
f2 = "results_11_29.csv"
# f1=input()
registration=open(f1,'r')
lines1=registration.readlines()
lines1=lines1[1:]
name=[0]
abnormal=[]
for line in lines1:
    num=line.split(',')[0]
    n=line.split(',')[1]
    name.append(n)
registration.close()
# f2=input()
result=open(f2,'r')
lines2=result.readlines()
lines2=lines2[1:]
wbc=[0]*len(name)
for line in lines2:
    num=line.split(',')[0]
    data=line.split(',')[1]
    wbc[int(num)]=float(data)
result.close()
for i in range(1,len(name)):
    if not 3.5<=wbc[i]<=9.5:
        abnormal.append(name[i].strip('\n'))
abnormal1=' '.join(abnormal)
print(f"Patients with abnormal WBC results include: {abnormal1}")
