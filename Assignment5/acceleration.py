time = input().split(' ')
v = input().split(' ')
t1 = [int(num1) for num1 in time]
v1 = [int(num2) for num2 in v]
tchange = []
vchange = []
for i in range(len(t1) - 1):
    change_t = t1[i + 1] - t1[i]
    tchange.append(change_t)
for s in range(len(v1) - 1):
    change_v = v1[s + 1] - v1[s]
    vchange.append(change_v)
achange = []
for a in range(len(vchange)):
    change_a = vchange[a] / tchange[a]
    # change_a1=(format(change_a,'.1f'))
    change_a1 = round(change_a, 1)
    achange.append(str(change_a1))
# achange2=[]
# for i in achange:
#      achange2.append(str(i))
print(f"The accelerations is: {', '.join(achange)}")
if len(set(achange)) == 1:
    print(True)
else:
    print(False)


# t = list(map(float, input().split())) # input array of times
# v = list(map(float, input().split())) # input array of speeds
#
# accelerations = [] # empty list to store calculated accelerations
#
# for i in range(1, len(v)):
#     acceleration = round((v[i] - v[i-1]) / (t[i] - t[i-1]), 1) # calculate acceleration and round to one decimal place
#     accelerations.append(acceleration) # add acceleration to the list
#
# is_uniform = all(a == accelerations[0] for a in accelerations) # check if all accelerations are equal
#
# print(*accelerations) # print the list of accelerations
# print(is_uniform) # print whether the object is undergoing uniform acceleration motion
class B():

    def __init__(self, data):
        self.data = data

    def __getattribute__(self, name):
        # return self.data[name]
        return self.data

b = B({"foo": "bar"})
print(b.foo)
