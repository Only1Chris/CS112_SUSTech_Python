# # 读取以逗号分隔的整数列表
# int_list = [int(x) for x in input().split(',')]
#
# # 输出整数列表
# print(int_list,sum(int_list[0:2]))
def find_Max_Subarray():
    list=input().split(',')
    max_val=int(list[0])
    i_max=0
    j_max=0
    for i in range(len(list)-1):
        ext_val=int(list[i])
        if ext_val>max_val:
            max_val=ext_val
            i_max=i
            j_max=i
        for j in range(i+1,len(list)):
            ext_val += int(list[j])
            if ext_val>max_val:
                max_val=ext_val
                i_max=i
                j_max=j
    sub_arr=[]
    for i in range(i_max,j_max+1):
        sub_arr.append(int(list[i]))
    return sub_arr
print(find_Max_Subarray())
# list = input().split(',')
# max_val = int(list[0])
# i_max=0
# j_max=0
# for i in range(len(list) - 1):
#     ext_val = int(list[i])
#     if ext_val > max_val:
#         max_val = ext_val
#         i_max=i
#         j_max=i
#     for j in range(i + 1, len(list)):
#         ext_val += int(list[j])
#         if ext_val> max_val:
#             max_val = ext_val
#             i_max=i
#             j_max=j
# # print(i_max,j_max)
# sub_arr=[]
# for i in range(i_max,j_max+1):
#     sub_arr.append(int(list[i]))
# print(sub_arr)