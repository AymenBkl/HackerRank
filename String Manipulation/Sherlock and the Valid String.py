from collections import Counter,defaultdict
s = input()
l = defaultdict(list)
counts = Counter(s)
a = True
for key,value in counts.items():
    l[value].append(key)
    if len(l.keys()) > 2:
        a = False
        break
print(len(l.keys()))
if (a and len(l.keys()) > 1):
    lenghts = []
    for key in l.keys():
        lenghts.append((len(l[key]),key))
    a = lenghts[0]
    b = lenghts[1]
    if (a[0] >= 2 and b[0] >= 2) or (a[0]==1 and a[1] > b[1] +1) or (b[0] == 1 and b[1] > a[1] + 1) :
        a = False
print("YES") if a else print("NO")        