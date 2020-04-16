# Python 3 program to count inversions in an array 
inv_counts = 0
# Function to Use Inversion Count 
def mergeSort(arr, n): 
    # We call to the sort function here
    # sorted array in merge function 
    return _mergeSort(arr) 
  
# This Function will use MergeSort to count inversions 
  
def _mergeSort(arr): 
  
    # A variable inv_counts is used to store 
    # inversion counts in each recursive call 
  
  
    # We will make a recursive call if and only if 
    # we have more than one elements  (len of our array is > 1)
  
    # mid is calculated to divide the array into two subarrays 
    # Floor division is must in case of python 
    # We will create two halfs the right half and right half
    if len(arr) > 1 :
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
    
        # It will calculate inversion counts in the left subarray 
        # we call the mergesort with righthalf and lefthalf
  
        _mergeSort(lefthalf)
        _mergeSort(righthalf)
        #We will call the merge to sort our tables righthelf and lefthelf
        merge(arr,lefthalf,righthalf) 


  
        # It will calculate inversion counts in right subarray 
        # It will merge two subarrays in a sorted subarray 
  
  
# This function will merge two subarrays in a single sorted subarray 
def merge(arr, lefthalf,righthalf): 
    left = 0    # Starting index of left subarray 
    right = 0 # Starting index of right subarray 
    index = 0     # Starting index of to be sorted subarray 
    global inv_counts
    # the inv_counts will store our inventions count
    # Conditions are checked to make sure that i and j don't exceed their 
    # subarray limits. 
    lenleft = len(lefthalf)
    lenright = len(righthalf)
    while left < lenleft and right < lenright: 
  
        # There will be no inversion if lefthalf[left] <= righthelf[right] 
        arrl = lefthalf[left]
        arrr = righthalf[right]
        if arrl <= arrr: 
            arr[index] = arrl 
            index += 1
            left += 1
        else: 
            # Inversion will occur. 
            arr[index] = arrr 
            inv_counts += lenleft - left 
            index += 1
            right += 1
  
    # Copy the remaining elements of left subarray into temporary array 
    while left < lenleft:
        arr[index] = lefthalf[left]
        left += 1
        index += 1
  
    # Copy the remaining elements of right subarray into temporary array 
    while right < lenright:
        arr[index] = righthalf[right]
        right += 1
        index += 1
  
for _ in range(int(input())):
    lenarr = int(input()) 
    arr = list(map(int,input().split()))
    mergeSort(arr,lenarr)
    print(inv_counts)
    inv_counts = 0
