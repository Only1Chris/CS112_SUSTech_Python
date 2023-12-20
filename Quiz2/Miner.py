# fileName=input()
schedule=[]
fileName="file1.csv"
record=[]
with open(fileName) as file:
    file.readline()
    for lines in file:
        record=lines.split(",")
        schedule.append(record)

schedule.sort(key=(lambda x:(x[0],x[1])))

for i in range(len(schedule)):
    print(schedule[i][0]+","+schedule[i][1])