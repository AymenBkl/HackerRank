import math
from collections import deque
from bisect import insort,bisect_left
#we will read the number of days and the number of trailingdays after that we read the trailingdays
numberdays , trailingdays = map(int,input().split())
expenditure = list(map(int,input().split()))
notifications = 0
#first we need to sort the firstpart of our trailing days
newsorted = sorted(expenditure[:trailingdays])
#here we the get the indexex of the median in our sorted list in both if the number is even or odd
midindex1 = math.ceil((trailingdays+1)/2) - 1
midindex12 = math.floor((trailingdays+1)/2) - 1
#we will move forward on our expenditures from trailingdays until the end 

for day,current in enumerate(expenditure[trailingdays:]):
    #we get the position of day one you understand at the end
    de = expenditure[day]
    #we calcaulate the median
    median = newsorted[midindex1] + newsorted[midindex12]
    #checkin if the day is verifieng our condition and if it is we increment the number of notifications
    if current >= median:
        notifications += 1
    #here comes all of the magic 
    #with bisect_left we get the position of the day that we are doing to delete from our sortedlist
    #why is this ?
    #because we need to delete the days according to the historique days so with this instructions 
    #we will get the index of the day to delete in the sorted list
    todelete = bisect_left(newsorted,de)
    del newsorted[todelete]
    #here we insert the new day and keep the list sorted accord to insort 
    insort(newsorted,current)

print(notifications)
    
