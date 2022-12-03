def addSinglePlayer(self,target, toAdd):
    query = "select id from tournament where name='{}' and contender=0".format(target)
    self.cursor.execute(query)
    ansDB = self.cursor.fetchall()
    if len(ansDB) == 0:
        return {"done": False, "error": "Tournament not found"}
    idInDB = ansDB[0][0]
    
    for player in toAdd:
        if player["abbr"] != None:
            query = "INSERT INTO singleplayer (name, abbreviation , games, wins, tournament)VALUES ('{}', '{}', 0, 0, {})".format(player["name"], player["abbr"] , idInDB)
        else: 
            query = "INSERT INTO singleplayer (name, abbreviation , games, wins, tournament)VALUES ('{}', NULL, 0, 0, {})".format(player["name"], idInDB)
        self.cursor.execute(query)
    self.sqliteConnection.commit()

    return { "done":True }
