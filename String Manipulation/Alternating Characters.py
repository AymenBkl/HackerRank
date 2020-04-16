from itertools import groupby
def NumberDeletionsAdjacent(str):
    countDeletion = 0
    #we user groupby to group our characters string it returing a key and group
    #Exemple if we have thre consecutive A it return a key A and group AAA
    #So we count the lenght of our group and we substract 1 for the A caracter only
    for key , group in groupby(str):
        countDeletion += len(list(group)) - 1
    return countDeletion
for _ in range(int(input())):
    s = list(input())
    print(NumberDeletionsAdjacent(s))
    