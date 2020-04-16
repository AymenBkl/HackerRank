from collections import Counter
def makeAnagram(str1,str2):
    #We count the lenght of string 1 and String 2 and we substract from the them 
    #the same number of same alphabitic occurnse like that we get the numbe of deletions
    return len(str1) + len(str2) - countDeleteion(str1,str2)
def countDeleteion(str1,str2):
    counters1 = Counter(str1)
    counters2 = Counter(str2)
    same = 0
    #We iterate through our Counter(str)
    #Remark this return chaque alphabit ocurruns in the string
    #We check if the alphabit is present in the other string 
    #We add the number of occurse too the our same counts  
    #if the number is not equal we get the min of both value so we build a two equal strings
    for key,value in counters1.items():
        if key  in counters2 :
            val = counters2[key]
            if value == val:
                same += 2*value
            else :
                same+= 2*min(value,val)
    return same
    """
    Another Solution
    Here we are going to the distinct values from both counters and we add them to get
    one counter containing all the distinct values
    a = counters1 - counters2
    b = counters2 - counters1
    d = a + b
    print(sum(d.values()))
    """
    

s1 = list(input())
s2 = list(input())
print(makeAnagram(s1,s2))
