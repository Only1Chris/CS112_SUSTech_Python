# 定义一个字典，用于存储每门课程的学分
course_credits = {}

# 读入学生数量和课程信息
m = int(input())
for i in range(m):
    n = int(input())
    for j in range(n):
        course, credit = input().split()
        credit = int(credit)
        if course in course_credits:
            course_credits[course] += credit
        else:
            course_credits[course] = credit

        # 找到最受欢迎的课程及其获得的学分
max_credits = 0
most_popular_course = ''
for course, credits in course_credits.items():
    if credits > max_credits:
        max_credits = credits
        most_popular_course = course

    # 输出结果
print(most_popular_course, max_credits)