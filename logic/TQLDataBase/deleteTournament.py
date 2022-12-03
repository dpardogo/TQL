def deleteTournament(self, name, team):
    query = "select id from tournament where name='{}' and contender={}".format(name, int(team))

    self.cursor.execute(query)
    ansDB = self.cursor.fetchall()
    if len(ansDB) == 0:
        return {"done": False, "error": "Tournament not found"}
    idInDB = ansDB[0][0]
    
    
    query = "DELETE FROM tournament WHERE id={}".format(idInDB)
    self.cursor.execute(query)
    self.sqliteConnection.commit()

    return { "done":True }