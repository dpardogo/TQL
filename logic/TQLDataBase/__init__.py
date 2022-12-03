import sqlite3
import os
from dotenv import load_dotenv
import prettytable
class TQLDataBase:
    sqliteConnection = None
    cursor = None
    
    from ._createTournament import createTournament
    from ._organizeTournament import organize,organizeSE,organizeDE,organizeRR,organizeSS
    from ._reportTournament import reportTournament,reportVictory
    from ._modifyParticipants import modifyParticipants
    from .addTeam import addTeam
    from .addPlayer import addPlayer
    from .addSinglePlayer import addSinglePlayer
    from .deleteTeam import deleteTeam
    from .deletePlayer import deletePlayer
    from .deleteSinglePlayer import deleteSinglePlayer
    from .deleteTournament import deleteTournament
    def __init__(self):
        load_dotenv()
        try:
            self.sqliteConnection = sqlite3.connect(os.getenv('DB_PATH'))
            self.cursor = self.sqliteConnection.cursor()
            self.plainQuery("PRAGMA foreign_keys = ON")

        except sqlite3.Error as error:
            print("Error estavlishing connection with data base, error: ", error)
    
    def closeConnection(self):
        self.cursor.close()
    def plainQuery(self, query):
        self.cursor.execute(query)
        return self.cursor
    def printTournament(self):
        if not self.checkTableExist("tournament"):
            print("No tournament records")
            return False
        table = prettytable.from_db_cursor(self.plainQuery("SELECT * FROM tournament"))
        print(table)
    def printTeam(self):
        if not self.checkTableExist("team"):
            print("No team records")
            return False
        table = prettytable.from_db_cursor(self.plainQuery("SELECT tournament.name  as tournament_name, team.* FROM team inner join tournament on tournament.id = team.tournament"))
        print(table)
    def printPlayer(self):
        if not self.checkTableExist("player"):
            print("No player records")
            return False
        table = prettytable.from_db_cursor(self.plainQuery("SELECT * FROM player"))
        print(table)
    def printSinglePlayer(self):
        if not self.checkTableExist("singleplayer"):
            print("No single player records")
            return False
        table = prettytable.from_db_cursor(self.plainQuery("SELECT * FROM singleplayer"))
        print(table)
    def printMatches(self):
        if not self.checkTableExist("matches"):
            print("No matches records")
            return False
        table = prettytable.from_db_cursor(self.plainQuery("SELECT * FROM matches"))
        print(table)
    def printTable(self, query):
        print(prettytable.from_db_cursor(query))
    def checkTableExist(self, table):
        ans = self.plainQuery("SELECT name FROM sqlite_master WHERE type='table' and name='{}';".format(table))
        return True if len(ans.fetchall()) != 0 else False