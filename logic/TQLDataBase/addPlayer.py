def addPlayer(self, target, tournament ,toAdd):
    query = "select id from tournament where name='{}' and contender=1".format(tournament)

    self.cursor.execute(query)
    ansDB = self.cursor.fetchall()
    if len(ansDB) == 0:
        return {"done": False, "error": "Tournament not found"}
    idInDB = ansDB[0][0]

    query = "select id from team where name='{}' and tournament={}".format(target, idInDB)
    self.cursor.execute(query)
    ansDB = self.cursor.fetchall()
    if len(ansDB) == 0:
        return {"done": False, "error": "Team not found"}
    idTeam = ansDB[0][0]
    
    for team in toAdd:
        if team["abbr"] != None:
            query = "INSERT INTO player (name, abbreviation , games, wins, team)VALUES ('{}', '{}', 0, 0, {})".format(team["name"], team["abbr"] , idTeam)
        else: 
            query = "INSERT INTO player (name, abbreviation , games, wins, team)VALUES ('{}', NULL, 0, 0, {})".format(team["name"], idTeam)
        self.cursor.execute(query)
    self.sqliteConnection.commit()

    return { "done":True }