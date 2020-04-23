"""
def formedString(counter,string):
    s = ""
    for c in string:
        if c in counter and counter[c] > 0:
            s += c
            counter[c] -= 1
    return s 
def Checks(indiceS1,indiceS2):
   for i in range(lens1+1):
       for j in range(lens2+1):
           if (i==0) or (j==0):
               tcs[i][j] = 0
           elif s1[i-1] == s2[j-1]:
               tcs[i][j] = 1 + tcs[i-1][j-1]
           else :
               tcs[i][j]= max(tcs[i-1][j],tcs[i][j-1])
"""
def commonChild(s1, s2):
    # row 0 = 0, column 0  = 0
    l1 = len(s1)
    l2 = len(s2)
    # we only need history of previous row
    lcs = [[0]*(l1+1) for _ in range(2)]
    #lcs_letters = [['']*(len(s1)+1) for _ in range(2)]
    
    # i in s1 = i+1 in lcs
    for i in range(l1):
        # get index pointers for current and previous row
        li1 = (i+1)%2
        li = i%2
        # j in s1 = j+1 in lcs
        for j in range(l2):
            # i and j are used to step forward in each string.
            # Now check if s1[i] and s2[j] are equal 
            if s1[i] == s2[j]:
                # Now we have found one longer sequence 
                # than what we had previously found.
                # so add 1 to the length of previous longest
                # sequence which we could have found at
                # earliest previous position of each string,
                # therefore subtract -1 from both i and j
                lcs[li1][j+1] = (lcs[li][j] + 1) 
                #lcs_letters[li1][j+1] = lcs_letters[li][j]+s1[li]

            # if not matching pair, then
            # get the biggest previous value
            elif lcs[li1][j] > lcs[li][j+1]:
                lcs[li1][j+1] = lcs[li1][j] 
                #lcs_letters[li1][j+1] = lcs_letters[li1][j]
            else:
                lcs[li1][j+1] = lcs[li][j+1] 
                #lcs_letters[li1][j+1] = lcs_letters[li][j+1]
    #print(lcs_letters[(i+1)%2][j+1])
    return lcs[(i+1)%2][j+1]   
s1 = input()
s2 = input()
print(commonChild(s1,s2))
