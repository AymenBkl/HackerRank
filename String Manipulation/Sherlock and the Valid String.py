from collections import Counter,defaultdict
s = input()
l = defaultdict(list)
counts = Counter(s)
a = True
#A simple Task for Simple use
#We count the number of occurnse for each character
#After we made a defaultdict that will transfer the value to key and characters to list of same value
#if we hade more than 2 values we exit and print No
# else we chec if the we had more the two values 
# then we check if the lenght of characters in value is greater then 2 if so we print no 
# else we check the number of caracters is equal too one and we can delete only one character
for key,value in counts.items():
    l[value].append(key)
    if len(l.keys()) > 2:
        a = False
        break
if (a and len(l.keys()) > 1):
    lenghts = []
    for key in l.keys():
        lenghts.append((len(l[key]),key))
    a = lenghts[0]
    b = lenghts[1]
    if (a[0] >= 2 and b[0] >= 2) or (a[0]==1 and a[1] > b[1] +1) or (b[0] == 1 and b[1] > a[1] + 1) :
        a = False
print("YES") if a else print("NO")        