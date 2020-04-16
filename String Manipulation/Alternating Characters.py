from itertools import groupby
def NumberDeletionsAdjacent(str):
    countDeletion = 0
    for key , group in groupby(str):
        countDeletion += len(list(group)) - 1
    return countDeletion
for _ in range(int(input())):
    s = list(input())
    print(NumberDeletionsAdjacent(s))
    