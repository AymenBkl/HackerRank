from collections import Counter
def makeAnagram(str1,str2):
    return len(str1) + len(str2) - countDeleteion(str1,str2)
def countDeleteion(str1,str2):
    counters1 = Counter(str1)
    counters2 = Counter(str2)
    deleteion = 0
    for key,value in counters1.items():
        if key  in counters2 :
            val = counters2[key]
            if value == val:
                deleteion += 2*value
            else :
                deleteion += 2*min(value,val)
    return deleteion
    

s1 = list(input())
s2 = list(input())
print(makeAnagram(s1,s2))
