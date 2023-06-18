a=[1, 2, 3, 4, 5, 2, 3, 4, 5, 1, 2, 3, 4, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 3, 4, 4, 1, 2, 3, 2, 3]
toal=[]
for i in a:
    toal.append(a.count(i))
final=[]
for i in a:
    if a.count(i)==max(toal):
        final.append(i)
# print(final)
final=list(set(final))
print(final)

