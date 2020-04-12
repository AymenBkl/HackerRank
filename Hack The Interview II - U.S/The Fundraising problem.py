class student :
    def __init__(self,charm,group,count,element):
        self.id = group
        self.charm = charm
        self.count = count
        self.element = element
    def deccount(self):
        self.count -= 1
    def __str__(self):
        return f"{self.id} {self.charm} {self.count} {self.element}"
class geusts :
    def __init__(self,gen,table,id):
        self.id = id
        self.gen = gen
        self.table = table
    def __str__(self):
        return f"{self.id} {self.gen} {self.table}"
def onelist(l,p):
    k = []
    for i,x in enumerate(l):
        for j,y in enumerate(x):
            k.append(student(y,i,p,i*fl[1]+j))
    return k
def onelist1(l):
    k = []
    for i,x in enumerate(l):
        for j,y in enumerate(x):
            k.append(geusts(i*fl[2]+j,y,i))
    return k
def removeobject(l,id):
    for x in l:
        if x.element == id:
            l.remove(x)
    
for i in range(1):
    fl = [int(x) for x in (input().rstrip()).split(" ")]
    students = []
    for j in range(fl[0]):
        students.append([int(x) for x in (input().rstrip()).split(" ")])
    sponsors = []
    for j in range(fl[2]):
        sponsors.append([int(x) for x in (input().rstrip()).split(" ")])
    k = int(input())
    a = True
    geust = 0
    for x in sponsors :
        if x[0] > fl[1]*k :
            print(-1)
            a = False
            break
        else :
            geust += x.pop(0)
            x.sort(reverse = True)
    if (geust > fl[0]*fl[1]*k):
        print(-1)
        a = False
    if (a):
        for x in students:
            x.sort(reverse = True)
        sortedstudent = onelist(students,k)
        sortedgeust = onelist1(sponsors)
        print(sortedgeust[0])
        sponsors.sort(key = lambda x:sum(x),reverse = True)

        s,count = 0,0
        for l in sponsors :
            count = 0                    
            stu = max(sortedstudent,key = lambda x:(x.charm)*(x.count))
            while len(students[stu.id])*stu.count < len(l):
                sortedstudent.remove(stu)
                stu = max(sortedstudent,key = lambda x:(x.charm)*(x.count))
            for i,x in enumerate(l) :
                s += x*students[stu.id][0]
                stu.deccount()
                if (stu.count == 0 ):
                    students[stu.id].pop(0)
                    removeobject(sortedstudent,stu.element)
                    stu.element += 1
                    stu.count = k

                    
                           
        print(s)
