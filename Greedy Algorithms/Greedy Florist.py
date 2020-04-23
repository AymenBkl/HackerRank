def getMinimumCost(BeginIndex,EndIndex):
    minpurchase,i = 0,1
    #We will iterate through the array but will get the number of element according to the number of friends
    #We calculate the sum
    #we multiplate By i
    #We recalculate the begin and end index
    #we increment i
    while BeginIndex < EndIndex :
        minpurchase += sum(arr[BeginIndex:EndIndex])*i
        BeginIndex = max(0,BeginIndex - k)
        EndIndex -=k
        i += 1
    return minpurchase
#We read the number of friends in group and number of flowers
n,k = map(int,input().split())
arr = list(map(int,input().split()))
#We sort the array from the lowest to highest
arr.sort()
#Now begin all the magic 
#We calculate the beginindex and the index
#All the friends had to buy the highest cost one by one and so on 
#every one will buy the next lowest cost from the highest and so on 

BeginIndex,EndIndex = n-k,n
print(getMinimumCost(BeginIndex,EndIndex))
