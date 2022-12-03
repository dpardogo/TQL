def reportTournament(self,atr,team,abbr1,tournament,abbr2):
    idtour=0
    if abbr2:
        self.cursor.execute("select id from tournament where abbreviation='{}'".format(tournament))
        idtour=self.cursor.fetchall()[0][0]
      
    else:
        self.cursor.execute("select id from tournament where name='{}'".format(tournament))
        idtour=self.cursor.fetchall()[0][0]

    idteam=0
    if abbr1:
        self.cursor.execute("select id from team where abbreviation='{}'".format(team))
        idteam=self.cursor.fetchall()[0][0]
      
    else:
        self.cursor.execute("select id from team where name='{}'".format(team))
        idteam=self.cursor.fetchall()[0][0]

    query="""UPDATE team SET {} = {} + 1
        WHERE id={} and  tournament={}
    """.format(atr,atr,idteam,idtour)
    print(query)
    self.cursor.execute(query)
    self.sqliteConnection.commit()

def reportVictory(self, team, abbr1,tournament,abbr2):
    infotour=0
    if abbr2:
        self.cursor.execute("select id,curr_phase from tournament where abbreviation='{}';".format(tournament))
        infotour=self.cursor.fetchall()[0]
      
    else:
        self.cursor.execute("select id,curr_phase from tournament where name='{}';".format(tournament))
        infotour=self.cursor.fetchall()[0]

    idteam=0
    if abbr1:
        self.cursor.execute("select id from team where abbreviation='{}';".format(team))
        idteam=self.cursor.fetchall()[0][0]
      
    else:
        self.cursor.execute("select id from team where name='{}';".format(team))
        idteam=self.cursor.fetchall()[0][0]

    query="""UPDATE team SET wins= wins + 1
        WHERE id={} and  tournament={}
    """.format(idteam,infotour[0])
    self.cursor.execute(query)

    query="""
    select nextMatch,loserRound,P1,P2,id from matches where phase={} and ( P1={} or P2={} )
    """.format(infotour[1],idteam,idteam)
    print(query)
    self.cursor.execute(query)
    
    infomatch=self.cursor.fetchall()
    if not len(infomatch):
        print("The participant does not have a match in the current phase")
        return
    infomatch=infomatch[0]
    print(infomatch)
    
    winnerIndex= 1 if infomatch[3] == idteam else 2

    self.cursor.execute(
        "update matches set winner='{}' where id={}".format(winnerIndex,infomatch[4])
    )
    
    if infomatch[0]!=None:
        query="""
        update match set P{} where id={}
        """.format(winnerIndex,infomatch[0])

    if infomatch[1]!=None:
        query="""
        update match set P{} where id={}
        """.format(winnerIndex,infomatch[1])

    self.cursor.execute(
        'select id from matches where tournament={} and phase={} and winner is NULL'.format(infotour[0],infotour[1])
    )
    res=self.cursor.fetchall()
    print(res)
    if not len(res):
        self.cursor.execute(
            'update tournament set curr_phase=curr_phase+1 where id={}'.format(infotour[0])
        )   

    self.sqliteConnection.commit()



    
    pass