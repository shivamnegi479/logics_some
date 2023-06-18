admit=[1,2,1,2,5,3,4,1,2]
discharge=[5,5,4,2,15,4,4,3,3]
total=[]
date_range=[]
for i,j in zip(admit,discharge):
    date_range.append([i,j])
print(date_range)

for j in range(len(date_range)):
    for i in range(date_range[j][0],date_range[j][1]+1):
        total.append(i)

print(total)
def occrence(List):
    c = 0
    num = []  
    for i in List:
        current = List.count(i)
        if(current>c):
            c = current
            num = i

    return num
print(occrence(total))

print(total.count(occrence(total)))
# print(total.count(2))
# print(total.count(3))
# print(max(total,key=total.count))



