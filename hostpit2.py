admit=[1,2,1,2,5,3,4,1,2]
discharge=[5,5,4,2,15,4,4,3,3]

dates=[[x,y] for x,y in zip(admit,discharge)]
total=[]
for i in range(len(dates)):
    for j in range(dates[i][0],dates[i][1]+1):
        total.append(j)
# print(total)

occ=[total.count(x) for x in total]

# print(occ)
final=[x for x in total if total.count(x)==max(occ)]
final=list(set(final))
print(final)

