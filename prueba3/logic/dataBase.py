from TQLDataBase import TQLDataBase

a = TQLDataBase()

#print(a.plainQuery("SELECT name FROM sqlite_master WHERE type='table';"))
#print(a.plainQuery("DROP TABLE tournamet"))
att = ["a1", "a2"]
atttt = ""
for at in att:
    atttt += at + "INTEGER NOT NULL,"
query = """CREATE TABLE IF NOT EXISTS player (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,""" + atttt +  """
        games INTEGER NOT NULL,
        wins INTEGER NOT NULL,
        team INTEGER NOT NULL,
        FOREIGN KEY(team) REFERENCES team(id)
        );"""
#print(a.plainQuery(query))
#print(a.plainQuery("SELECT name FROM sqlite_master WHERE type='table';"))
#print(a.plainQuery("INSERT INTO tournament (name, type, contender)VALUES ('hola', 1, 0)"))
#print(a.plainQuery("INSERT INTO team (name, a1, a2, games, wins, tournament)VALUES ('hola', 1, 0)"))
#print(a.plainQuery("SELECT * FROM team"))
#print(a.sqliteConnection.commit())
#query = "select seq from sqlite_sequence where name='tournament'"
#print(a.plainQuery(query)[0][0])
#print(a.plainQuery("DROP TABLE tournament"))
#print(a.plainQuery("DROP TABLE sqlite_sequence"))
#print(a.plainQuery("DROP TABLE team"))
#print(a.plainQuery("DROP TABLE player"))
print(a.plainQuery("SELECT name FROM sqlite_master WHERE type='table';"))
#print(a.plainQuery("PRAGMA table_info(player);"))
#print(a.plainQuery("PRAGMA table_info(team);"))
#print(a.plainQuery("PRAGMA table_info(tournament);"))
#a.createTournament("mundialitl4", "mnd",["a1", "a2"], [{"name": "colombia",  "abbr": "COL"}, {"name": "alemania",  "abbr": "GER"}])
#a.createTournament("mundialitl5", None,["a1", "a2"], [])

print(a.plainQuery("SELECT * FROM tournament"))
print(a.plainQuery("SELECT * FROM team"))
print(a.plainQuery("SELECT * FROM player"))