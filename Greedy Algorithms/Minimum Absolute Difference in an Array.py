lenarr = int(input())
arr = list(map(int,input().split()))
arr.sort();
minabs = 999999999
for i in range(lenarr-1):
    currentabs = abs(arr[i]-arr[i+1])
    if currentabs < minabs:
        minabs = currentabs
print(minabs)