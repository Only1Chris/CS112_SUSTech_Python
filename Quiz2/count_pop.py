filename=input()
# city=[]
city_dict={}
with open(filename) as file:
    for line in file:
        c,cname,pop=line.split(',')
        pop=int(pop)
        if cname in city_dict.keys():
            city_dict[cname]+=pop
        else:
            city_dict[cname]=pop
            # city.append([cname,pop])
for e in city_dict.keys():
    print(e+':',city_dict[e])
