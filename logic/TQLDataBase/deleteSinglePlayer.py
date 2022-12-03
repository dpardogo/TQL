def deleteSinglePlayer(self,target, toAdd):
    query = "select id from tournament where name='{}' and contender=0".format(target)
    self.cursor.execute(query)
    ansDB = self.cursor.fetchall()
    if len(ansDB) == 0:
        return {"done": False, "error": "Tournament not found"}
    idInDB = ansDB[0][0]
    
    for player in toAdd:
        query = "DELETE FROM singleplayer WHERE name='{}' and tournament={}".format(player["name"], idInDB)
        self.cursor.execute(query)
        print(query)
    self.sqliteConnection.commit()

    return { "done":True }
