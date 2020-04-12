n = int(input())
maxHeads,countHeads = 0,0
maxTails,countTails = 0,0

for i in range(n):
    toast = input()
    if toast == "Heads" and countTails == 0:
        countHeads += 1
    elif toast == "Heads" and countTails != 0:
        maxTails = max(countTails,maxTails)
        countTails = 0
        countHeads +=1
    elif toast == "Tails" and countHeads == 0:
        countTails += 1
    elif toast == "Tails" and countHeads != 0:
        maxHeads = max(countHeads,maxHeads)
        countHeads = 0
        countTails += 1

print(max(maxHeads,countHeads) , max(maxTails,countTails))
