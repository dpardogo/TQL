def createTournament(self, name, abbreviation, attributes, participants, teams):
    query = """CREATE TABLE IF NOT EXISTS tournament (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        abbreviation VARCHAR(50),
        type INTEGER NOT NULL,
        contender BOOLEAN NOT NULL,
        curr_phase INTEGER NOT NULL
        );"""
    self.cursor.execute(query)
    atbs = ""
    for atb in attributes:
        atbs += atb + " INTEGER NOT NULL, "
    if teams:
        query = """CREATE TABLE IF NOT EXISTS team (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            abbreviation VARCHAR(5), """ + atbs +  """
            games INTEGER NOT NULL,
            wins INTEGER NOT NULL,
            tournament INTEGER NOT NULL,
            FOREIGN KEY(tournament) REFERENCES tournament(id)
            );"""
        self.cursor.execute(query)
        query = """CREATE TABLE IF NOT EXISTS player (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,""" + atbs +  """
        games INTEGER NOT NULL,
        wins INTEGER NOT NULL,
        team INTEGER NOT NULL,
        FOREIGN KEY(team) REFERENCES team(id)
        );"""
        self.cursor.execute(query)
    else:
        self.cursor.execute(query)
        query = """CREATE TABLE IF NOT EXISTS player (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        abbreviation VARCHAR(5),""" + atbs +  """
        games INTEGER NOT NULL,
        wins INTEGER NOT NULL,
        team INTEGER NOT NULL,
        FOREIGN KEY(team) REFERENCES team(id)
        );"""
        self.cursor.execute(query) 
    if abbreviation != None:
        query = "INSERT INTO tournament (name, abbreviation, type, contender, curr_phase)  VALUES ('{}', '{}', 0, {}, {})".format(name, abbreviation, teams, 0)
    else:
        query = "INSERT INTO tournament (name, abbreviation, type, contender, curr_phase)  VALUES ('{}', NULL, 0, {}, {})".format(name, teams, 0)

    self.cursor.execute(query)
    self.sqliteConnection.commit()


    query = "select seq from sqlite_sequence where name='tournament'"

    self.cursor.execute(query)
    idInDB = self.cursor.fetchall()[0][0]
    atbs = ""
    for atb in attributes:
        atbs += atb + " , "
    for prtc in participants:
        if prtc["abbr"] != None:
            query = "INSERT INTO team (name, abbreviation , {}  games, wins, tournament)VALUES ('{}', '{}', {} 0, 0, {})".format(atbs, prtc["name"], prtc["abbr"],"0, "*len(attributes), idInDB)
        else: 
            query = "INSERT INTO team (name, abbreviation , {}  games, wins, tournament)VALUES ('{}', NULL, {} 0, 0, {})".format(atbs, prtc["name"],"0, "*len(attributes), idInDB)
        self.cursor.execute(query)
    self.sqliteConnection.commit()

