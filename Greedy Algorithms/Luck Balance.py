def  luckBalanc(arr):
    #after filling all the array we would like to sort from the highest to lowest 
    arr.sort(reverse = True)
    #in the end we return the sum from 0 index to k like that we would take all the maxium values
    #and substract the round she loses that would be from k to the end
    return sum(arr[:k]) - sum(arr[k:])

#We read the number of element in the round to loses
n,k = map(int,input().split())
arr = []
score = 0
for _ in range(n):
    #Here we define the luck and the importance of each contest 
    #if importance is equal too 0 then we add the luck to the score 
    #else we added to our array
    luck,importance = map(int,input().split())
    if importance == 0:
        score += luck
    else :
        arr.append(luck)

print(score+luckBalanc(arr))