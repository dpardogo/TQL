def modifyParticipants(self,team,abbr1,tournament,abbr2,dic):
    idt=0
    if abbr2:
        self.cursor.execute("select id from tournament where abbreviation='{}'".format(tournament))
        idt=self.cursor.fetchall()[0][0]
      
    else:
        self.cursor.execute("select id from tournament where name='{}'".format(tournament))
        idt=self.cursor.fetchall()[0][0]

    self.cursor.execute("select contender from tournament where id={} ".format(idt))
    contender='team' if self.cursor.fetchall()[0][0] else 'player'
    
    idteam=0
    if abbr1:
        self.cursor.execute("select id from {} where tournament={} and abbreviation='{}'".format(contender,idt,team))
        idteam=self.cursor.fetchall()[0][0]
      
    else:
        self.cursor.execute("select id from {} where tournament={} and name='{}'".format(contender,idt,team))
        idteam=self.cursor.fetchall()[0][0]

    
    modifications=''
    for key in dic:
        modifications+=' '+key+'='+dic[key]+' '

    query="update "+contender+" set "+ modifications+"where id ="+str(idteam)
    
    self.cursor.execute(query)

    self.sqliteConnection.commit()
    pass
