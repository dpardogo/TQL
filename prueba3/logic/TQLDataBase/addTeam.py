def addTeam(self,target, toAdd):
    query = "select id from tournament where name='{}'".format(target)

    self.cursor.execute(query)
    ansDB = self.cursor.fetchall()
    if len(ansDB) == 0:
        return {"done": False, "error": "Tournament not found"}
    idInDB = ansDB[0][0]
    
    for team in toAdd:
        if team["abbr"] != None:
            query = "INSERT INTO team (name, abbreviation , games, wins, tournament)VALUES ('{}', '{}', 0, 0, {})".format(team["name"], team["abbr"] , idInDB)
        else: 
            query = "INSERT INTO team (name, abbreviation , games, wins, tournament)VALUES ('{}', NULL, 0, 0, {})".format(team["name"], idInDB)
        self.cursor.execute(query)
    self.sqliteConnection.commit()

    return { "done":True }
