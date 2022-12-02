import sqlite3,random,math,queue
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class item:
    priority: int
    item: Any=field(compare=False)

class Tournament:

    name=''
    teams=set({})
    attr_num=0
    databasePointer=None

    def __init__(self, name, attributes, teams):
        
        self.name=name
        self.teams=self.teams | set([i[0] for i in teams])
        self.attr_num=len(attributes)

        self.databasePointer=sqlite3.connect(self.name+'.db')
        command=("CREATE TABLE IF NOT EXISTS Participants ( Name TEXT, Abbr TEXT, Victories INTEGER)")
            #+" INTEGER,".join(attributes)+");")
        self.databasePointer.cursor().execute(command)
        
        for team in teams:
            command=("INSERT INTO Participants  VALUES("+team[0]+","+team[1]
                    +",0"*(self.attr_num+1)+");"
                    )
            self.databasePointer.cursor().execute(command)

        
        
    def addTeams(self,list):
        for team in list:
            command=("INSERT INTO Participants  VALUES("+team[0]+","+team[1]
                    +",0"*(self.attr_num+1)+");"
                    )
            self.databasePointer.cursor().execute(command)
        self.teams=self.teams | list

    def organize(self):
        pass

    def show(self):
        pass

    def report(self):
        pass



class Elimination(Tournament):
    def organize(self):
        remaining=list(self.teams)
        random.shuffle(remaining)
        print(remaining)
        n= len(remaining)
        rounds=math.floor(math.log(n,2))

        matches=[]
        nextRound=[]
    
        while len(matches)<(n-2**rounds):
            matches.append((remaining.pop(),remaining.pop()))
            nextRound.append('w'+str(len(matches)))
        
        while len(nextRound):
            remaining.append(nextRound.pop())

        while len(matches)<n-1:
            while len(remaining):
                matches.append((remaining.pop(),remaining.pop()))
                nextRound.append('w'+str(len(matches)))
            while len(nextRound):
                remaining.append(nextRound.pop())
            
        print(matches)



        return super().organize()

    def show(self):
        return super().show()
    


class DoubleElimination(Tournament):
    def organize(self):
        mainRound=list(self.teams)
        random.shuffle(mainRound)

        n= len(mainRound)
        rounds=math.floor(math.log(n,2))

        matches=[]
        
        nextRound=[]
        losersRound=[]

        while len(matches)<(n-2**rounds):
            matches.append((mainRound.pop(),mainRound.pop()))
            nextRound.append('w'+str(len(matches)))
            losersRound.append('l'+str(len(matches)))
        
        while len(nextRound):
            mainRound.append(nextRound.pop())

    
        while len(matches)<2*n-3:
            
            while max(len(mainRound)//2,1) < len(losersRound):
                matches.append((losersRound.pop(0),losersRound.pop(0)))
                losersRound.append('w'+str(len(matches)))

            while 1<len(mainRound):
                matches.append((mainRound.pop(),mainRound.pop()))
                nextRound.append('w'+str(len(matches)))
                losersRound.append('l'+str(len(matches)))

            while len(nextRound):
                mainRound.append(nextRound.pop())

        matches.append((losersRound[0],mainRound[0]))
            
        print(matches)


        return super().organize()

    def show(self):
        return super().show()



class RoundRobin(Tournament):
    def organize(self,n=1):
        teams=list(self.teams)
        random.shuffle(teams)

        matches=[]
        even=True
        if len(teams)%2==1:
            m=len(teams)+1
            even=False
        else:
            m=len(teams)
        
        for i in range(m-1):
            if even:
                matches.append((teams[i],teams[m-1]))
            for j in range(1,m//2):
                index1=(i+j)%(m-1)
                index2=(i-j)%(m-1)
                matches.append((teams[index1],teams[index2]))
        
        print(matches)
        return super().organize()

class SwissSystem(Tournament):
    remaining=[]

    def organize(self):
        teams=list(self.teams)
        random.shuffle(teams)
        self.teams=teams
        matches=[]
        n=len(teams)

        for i in range(n):
            obj=item(0,[i,1<<i])
            self.remaining.append(obj)
        print(self.remaining)
        for i in range(n//2):
            a,b=self.remaining[2*i],self.remaining[2*i+1]
            matches.append((self.teams[a.item[0]],self.teams[b.item[0]]))
            a.item[1]=a.item[1] | (1<<b.item[0])
            b.item[1]=(1<<a.item[0]) | b.item[1]
        
        if n%2==1:
            self.remaining[-1].priority+=1
        print(matches)
        
        return super().organize()

    def report(self,dic):
        n=len(self.teams)
        q=queue.PriorityQueue()
        matches=[]
        

        for i in range(n):
            value=dic.get(self.teams[self.remaining[i].item[0]])
            if value != None and value: 
                self.remaining[i].priority+=1

        print(self.remaining,(n>>1)<<1)
        while len(self.remaining):
            q.put(self.remaining.pop())

        wait=[]
        while not q.empty():
            if len(wait):
                next=q.get()
                wait.append(next)
                for i in range(len(wait)-2,-1,-1):
                    a,b=wait[i],next
                    if not a.item[1] &  b.item[1]:

                        a.item[1]=a.item[1] | (1<<b.item[0])
                        b.item[1]=(1<<a.item[0]) | b.item[1]
                        matches.append((self.teams[a.item[0]],self.teams[b.item[0]]))
                        self.remaining.extend([a,b])
                        del wait[i]
                        wait.pop()
                        break
            else:
                wait.append(q.get())

        while len(wait)>1:
            a,b=wait.pop(0),wait.pop(0)
            a.item[1]=a.item[1] | (1<<b.item[0])
            b.item[1]=(1<<a.item[0]) | b.item[1]
            matches.append((self.teams[a.item[0]],self.teams[b.item[0]]))

        if len(wait):
            wait[-1].priority+=1
            self.remaining.append(wait[-1])

        print(matches)
        return super().report()

obj=DoubleElimination('a',[],[('1','1'),('2','2'),('3','2'),('4','2'),('5','2')])
obj.organize()
