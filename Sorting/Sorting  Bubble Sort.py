def swap(arr,i):
    a = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = a


n,arr = int(input()),list(map(int,input().split()))
swaps = 0
for i in range(n):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            swap(arr,j)
            swaps += 1
print("Array is sorted in {} swaps.".format(swaps))
print("First Element: {}".format(arr[0]))
print("Last Element: {}".format(arr[-1]))