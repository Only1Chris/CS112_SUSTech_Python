list=input().split(',')
max=0
min=list[0]
step=0
vol=0
for i in range(len(list)-1):
    if list[i]>=max:
        max=list[i]
        vol+=(max-min)*step
        max=0
        step=0
    if list[i]<min:
        min=list[i]

    step+=step
print(vol)


# def trapped_water(heights):
#     left = 0
#     right = len(heights) - 1
#     max_left = 0
#     max_right = 0
#     water = 0
#
#     while left <= right:
#         if heights[left] <= heights[right]:
#             if heights[left] > max_left:
#                 max_left = heights[left]
#             else:
#                 water += max_left - heights[left]
#             left += 1
#         else:
#             if heights[right] > max_right:
#                 max_right = heights[right]
#             else:
#                 water += max_right - heights[right]
#             right -= 1
#
#     return water
#
# # Example usage:
# heights = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(trapped_water(heights))