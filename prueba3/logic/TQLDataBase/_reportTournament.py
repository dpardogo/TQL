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

    query="""
    select nextMatch,P1,P2 from matches where curr_phase={} and ( P1={} or P2={} )
    """.format(infotour[1],idteam,idteam)
    self.cursor.execute(query)
    infomatch=self.cursor.fetchall()[0]
    
    winnerIndex=0
    if infomatch[1] == idteam:
        winnerIndex=1
    else:
        winnerIndex=2
    
    query="""
    UPDATE matches SET P{} =-P{}
        WHERE id={}
    """.format(infomatch[0],infomatch[0],infomatch[0])
    self.cursor.execute(query)
    nextMatch=self.cursor.fetchall()




    if len(nextMatch)>0:   
        self.cursor.execute("UPDATE team SET {} = {} + 1 WHERE id={} and  tournament={} ")


    query="""
    select id,P1,P2 from matches where P1=L{} or P2=L{}
    """
    self.cursor.execute(query)
    loserMatch=self.cursor.fetchall()



    query="""UPDATE team SET wins = wins + 1
        WHERE id={} and  tournament={}
    """.format(idteam,infotour[0])
    pass