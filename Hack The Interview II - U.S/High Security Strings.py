string = input()
weight = int(input())
sums = 0
for s in string:
    sums += (ord(s) - 97 + weight) % 26
print(sums) 