from collections import defaultdict
numbers = defaultdict(int)
values = defaultdict(int)
for _ in range(int(input())):
    op,i = map(int,input().split())
    if op == 1:
        values[numbers[i]] = max(0,values[numbers[i]] -1)
        numbers[i] += 1
        values[numbers[i]] += 1
    elif op == 2:
        values[numbers[i]] = max(0,values[numbers[i]]-1)
        numbers[i] = max(0,numbers[i] - 1)
        if numbers[i] > 0:
            values[numbers[i]] += 1
    else:
       print(1) if values[i] > 0 else print(0)


