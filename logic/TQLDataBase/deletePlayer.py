def deletePlayer(self, target, tournament ,toAdd):
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
        query = "DELETE FROM player WHERE name='{}' and team={}".format(team["name"] , idTeam)
        self.sqliteConnection.execute(query)
    self.sqliteConnection.commit()

    return { "done":True }