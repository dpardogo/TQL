import math, random
def organize(self,system,name,abbr=True):
    functions={
        'Knockout': lambda : self.organizeSE(name,abbr),
        'DoubleElimination': lambda : self.organizeDE(name,abbr),
        'RoundRobin': lambda : self.organizeRR(name,abbr),
        'SwissSystem': lambda : self.organizeSS(name,abbr),
    }
    query = """CREATE TABLE IF NOT EXISTS matches (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        P1 INTEGER ,
        P2 INTEGER ,
        abbreviation VARCHAR(12),
        winner INTEGER,
        nextMatch INTEGER,
        loserRound INTEGER,
        tournament INTEGER NOT NULL,
        phase INTEGER NOT NULL,
        FOREIGN KEY(P1) REFERENCES team(id),
        FOREIGN KEY(P2) REFERENCES team(id),
        FOREIGN KEY(tournament) REFERENCES tournament(id)
        );"""
    self.cursor.execute(query)
    self.sqliteConnection.commit()

    functions[system]()

def organizeSE(self,name,abbr=True):  
    idt=0
    if abbr:
        self.cursor.execute("select id from tournament where abbreviation='{}'".format(name))
        idt=self.cursor.fetchall()[0][0]
      
    else:
        self.cursor.execute("select id from tournament where name='{}'".format(name))
        idt=self.cursor.fetchall()[0][0]
     

    query = """select id, abbreviation from team 
            where tournament ={} ;
            """.format(idt)
    self.cursor.execute(query)

    remaining=[i for i in self.cursor.fetchall()]
    random.shuffle(remaining)

    n= len(remaining)
    rounds=math.floor(math.log(n,2))
    
    nextRound=[]

    matches=0
    phase=0

    self.cursor.execute("SELECT MAX(id) FROM matches")
    currid=self.cursor.fetchall()[0][0]
    currid= 0 if currid==None else currid

    while matches<(n-2**rounds):
        p1,p2=remaining.pop(),remaining.pop()
        matches+=1
        currid+=1

        query = "INSERT INTO matches (P1, P2, abbreviation, tournament, phase)  VALUES ({}, {}, '{}', {}, {})".format(p1[0],p2[0],p1[1]+'-'+p2[1],idt,phase)
        self.cursor.execute(query)

        nextRound.append((currid,))
    
    while len(nextRound):
        remaining.append(nextRound.pop())
    

    while matches<n-1:
        phase+=1
        while len(remaining)>1:
            p1,p2=remaining.pop(),remaining.pop()
            matches+=1
            currid+=1

            print(p1,p2)
            if len(p1)==1:
                self.cursor.execute("update matches set nextMatch={} where id={}".format(currid,p1[0]))
                p1=('NULL','W'+str(p1[0]))

            if len(p2)==1:
                self.cursor.execute("update matches set nextMatch={} where id={}".format(currid,p2[0]))
                p2=('NULL','W'+str(p2[0]))

            query = "INSERT INTO matches (P1, P2, abbreviation, tournament, phase)  VALUES ({}, {}, '{}', {},{})".format(p1[0],p2[0],p1[1]+'-'+p2[1],idt,phase)
                      
            self.cursor.execute(query)

            nextRound.append((currid,))

        while len(nextRound):
            remaining.append(nextRound.pop())
    
        
    print(matches)
    self.sqliteConnection.commit()
    pass

def organizeDE(self,name,abbr=True):
    idt=0
    if abbr:
        self.cursor.execute("select id from tournament where abbreviation='{}'".format(name))
        idt=self.cursor.fetchall()[0][0]
      
    else:
        self.cursor.execute("select id from tournament where name='{}'".format(name))
        idt=self.cursor.fetchall()[0][0]

    query = """select id, abbreviation from team 
            where tournament ={} ;
            """.format(idt)
    self.cursor.execute(query)

    mainRound=[i for i in self.cursor.fetchall()]
    
    random.shuffle(mainRound)

    n= len(mainRound)
    rounds=math.floor(math.log(n,2))
    
    nextRound=[]
    losersRound=[]

    matches=0
    phase=0

    self.cursor.execute("SELECT MAX(id) FROM matches")
    currid=self.cursor.fetchall()[0][0]
    currid= 0 if currid==None else currid

    while matches<(n-2**rounds):
        p1,p2=mainRound.pop(),mainRound.pop()
        matches+=1
        currid+=1

        query = "INSERT INTO matches (P1, P2, abbreviation, tournament, phase)  VALUES ({}, {}, '{}', {}, {})".format(p1[0],p2[0],p1[1]+'-'+p2[1],idt,phase)
        self.cursor.execute(query)

        nextRound.append((currid,))
        losersRound.append((-currid,))

    while len(nextRound):
        mainRound.append(nextRound.pop())

    while matches<2*n-3:
        phase+=1

        while max(len(mainRound)//2,1) < len(losersRound):
            p1,p2=losersRound.pop(),losersRound.pop()
            print(p1,p2)
            matches+=1
            currid+=1

            if len(p1)==1:
                if(p1[0]>0):
                    self.cursor.execute("update matches set nextMatch={} where id={}".format(currid,p1[0]))
                    p1=('NULL','W'+str(p1[0]))
                else:
                    self.cursor.execute("update matches set loserRound={} where id={}".format(currid,-p1[0]))
                    p1=('NULL','l'+str(-p1[0]))

            if len(p2)==1:
                if(p2[0]>0):
                    self.cursor.execute("update matches set nextMatch={} where id={}".format(currid,p2[0]))
                    p2=('NULL','W'+str(p2[0]))
                else:
                    print('entra')
                    self.cursor.execute("update matches set loserRound={} where id={}".format(currid,-p2[0]))
                    p2=('NULL','l'+str(-p2[0]))
            
            query = "INSERT INTO matches (P1, P2, abbreviation, tournament, phase)  VALUES ({}, {}, '{}', {},{})".format(p1[0],p2[0],p1[1]+'-'+p2[1],idt,phase)
            self.cursor.execute(query)

            losersRound.append((currid,))


        while 1<len(mainRound):
            p1,p2=mainRound.pop(),mainRound.pop()
            matches+=1
            currid+=1
    
            if len(p1)==1:
                if(p1[0]>0):
                    self.cursor.execute("update matches set nextMatch={} where id={}".format(currid,p1[0]))
                    p1=('NULL','W'+str(p1[0]))
                else:
                    self.cursor.execute("update matches set loserRound={} where id={}".format(currid,-p1[0]))
                    p1=('NULL','l'+str(-p1[0]))

            if len(p2)==1:
                if(p2[0]>0):
                    self.cursor.execute("update matches set nextMatch={} where id={}".format(currid,p2[0]))
                    p2=('NULL','W'+str(p2[0]))
                else:
                    self.cursor.execute("update matches set loserRound={} where id={}".format(currid,-p2[0]))
                    p2=('NULL','l'+str(-p2[0]))

            query = "INSERT INTO matches (P1, P2, abbreviation, tournament, phase)  VALUES ({}, {}, '{}', {},{})".format(p1[0],p2[0],p1[1]+'-'+p2[1],idt,phase)
                      
            self.cursor.execute(query)

            nextRound.append((currid,))
            losersRound.append((-currid,))

        while len(nextRound):
            mainRound.append(nextRound.pop())

    p1,p2=losersRound[0],mainRound[0]

    query = "INSERT INTO matches (abbreviation, tournament, phase)  VALUES ( '{}', {},{})".format('W'+str(p1[0])+'-'+'W'+str(p2[0]),idt,phase) 
    print(matches)
    self.sqliteConnection.commit()
    

def organizeRR(self,name,abbr=True):

    idt=0
    if abbr:
        self.cursor.execute("select id from tournament where abbreviation='{}'".format(name))
        idt=self.cursor.fetchall()[0][0]
      
    else:
        self.cursor.execute("select id from tournament where name='{}'".format(name))
        idt=self.cursor.fetchall()[0][0]

    query = """select id, abbreviation from team 
            where tournament ={} ;
            """.format(idt)
    self.cursor.execute(query)

    participants=[i for i in self.cursor.fetchall()]
    
    random.shuffle(participants)
    matches=[]
    even=True
    if len(participants)%2==1:
        m=len(participants)+1
        even=False
    else:
        m=len(participants)
    
    for i in range(m-1):
        if even:
            p1,p2=participants[i],participants[m-1]
            matches.append((p1,p2))
            query = "INSERT INTO matches (P1, P2, abbreviation, tournament, phase)  VALUES ({}, {}, '{}', {},{})".format(p1[0],p2[0],p1[1]+'-'+p2[1],idt,i)
            self.cursor.execute(query)

        for j in range(1,m//2):
            index1=(i+j)%(m-1)
            index2=(i-j)%(m-1)

            p1,p2=participants[index1],participants[index2]
            matches.append((p1,p2))
            query = "INSERT INTO matches (P1, P2, abbreviation, tournament, phase)  VALUES ({}, {}, '{}', {},{})".format(p1[0],p2[0],p1[1]+'-'+p2[1],idt,i)
            self.cursor.execute(query)

    
    print(matches)
    self.sqliteConnection.commit()
    

def organizeSS():
    pass