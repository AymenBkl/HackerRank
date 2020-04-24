from bisect import insort

n = int(input())
k = int(input())
arr = []
for _ in range(n):
    #Insort is for when we insert new element we kept the array in the sorting order
    value = int(input())
    insort(arr,value)
minfairnes = 10**10
for i in range(n-k+1):
    currentfairnes = arr[i+k-1] - arr[i]
    if (currentfairnes < minfairnes):
        minfairnes = currentfairnes
print(minfairnes)