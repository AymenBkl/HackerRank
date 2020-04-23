def Special(string,lens):
    count = 0
    if lens < 2:
        return 1
    mid = lens // 2
    lefthalf = string[:mid]
    righthalf = string[mid:]
    count += Special(lefthalf,len(lefthalf))
    count += Special(righthalf,len(righthalf))  
    return count
lens = int(input())
s = input()
counts = 0
print(Special(s,lens))

