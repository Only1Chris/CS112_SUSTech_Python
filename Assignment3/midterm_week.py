def format_course(s):
    course = s.split()
    for i in range(len(course)):
        course[i] = course[i].capitalize()
    return course


exam = input()
if exam.isdigit():
    m = int(exam)
    exam = ['Math']
else:
    m = int(input())
    exam = format_course(exam)
for i in range(m):
    line = input().split(';')
    calendar = dict()
    midterm = []
    for j in range(len(line)):
        course = line[j].split()[0].capitalize()
        credit = int(line[j].split()[1])
        calendar[course] = credit
        if course in exam:
            midterm.append(course)
    if sum(calendar.values()) > 25:
        print("Your current credits are %i, which is greater than 25. Pay attention!" % sum(calendar.values()))
    elif len(midterm) == 0:
        print("You don't have any exam during midterm week. Amazing!")
    elif len(midterm) == 1:
        print("You have 1 exam during midterm week, which is %s." % midterm[0])
    else:
        midterm.sort()
        print("You have %i exams during midterm week, which are %s." % (len(midterm), ', '.join(str(e) for e in midterm)))


        # Your current credits are 26, which is greater than 25. Pay attention!
        # You have 1 exam during midterm week, which is English.
        # You have 2 exams during midterm week, which are English, Math.
        # You don't have any exam during midterm week. Amazing!
        # Your current credits are 29, which is greater than 25. Pay attention!
        # You have 1 exam during midterm week, which is Math.
        # You don't have any exam during midterm week. Amazing!
