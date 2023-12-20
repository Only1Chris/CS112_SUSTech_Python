# 定义一个空的二维数组
array = []

# 按行分割输入的字符串，并将每个元素添加到二维数组中
file_name = input()
input_str=open(file_name, encoding='utf-8')
# # 按行分割字符串
# rows = input_str.strip().split("\n")

# 遍历每一行，按逗号分割元素，并添加到二维数组中
for row in input_str:
    elements = row.strip().split(",")
    array.append(elements)

for i in range(9):
    list = []
    for j in range(9):
        # print(array[j][i])
        list.append(array[j][i])
    # print(list)
    array.append(list)

for i in range(3):
    for j in range(3):
        list=[]
        for k in range(3):
            for l in range(3):
                list.append(array[3*i+k][3*j+l])
        array.append(list)
# print(array)

if __name__=="__main__":
    for i in range(27):
        # print(array[i])
        if array[i].count('0')>=2 or array[i].count('1')>=2 or array[i].count('2')>=2 or array[i].count('3')>=2 or array[i].count('4')>=2 or array[i].count('5')>=2 or array[i].count('6')>=2 or array[i].count('7')>=2 or array[i].count('8')>=2 or array[i].count('9')>=2:
            print('False')
            break
        elif i==26:
            print('True')