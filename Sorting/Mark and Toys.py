ntoys,amount = map(int,input().split())
toys = list(map(int,input().split()))
toys.sort()
numbertoystobuy = 0
for i in range(1,ntoys + 1):
    if sum(toys[:i]) > amount:
        numbertoystobuy = i -1
        break
print(numbertoystobuy)
