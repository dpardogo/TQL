def deleteTeam(self,target, toAdd):
    query = "select id from tournament where name='{}'".format(target)

    self.cursor.execute(query)
    ansDB = self.cursor.fetchall()
    if len(ansDB) == 0:
        return {"done": False, "error": "Tournament not found"}
    idInDB = ansDB[0][0]
    
    for team in toAdd:
        query = "DELETE FROM team where name='{}' and tournament={}".format(team["name"], idInDB)
        self.cursor.execute(query)
    self.sqliteConnection.commit()

    return { "done":True }
