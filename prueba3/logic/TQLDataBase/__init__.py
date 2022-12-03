import sqlite3
import os
from dotenv import load_dotenv
class TQLDataBase:
    sqliteConnection = None
    cursor = None
    
    from ._createTournament import createTournament
    from ._organizeTournament import organize,organizeSE,organizeDE,organizeRR,organizeSS
    from ._reportTournament import reportTournament,reportVictory
    from ._modifyParticipants import modifyParticipants
    def __init__(self):
        load_dotenv()
        try:
            self.sqliteConnection = sqlite3.connect(os.getenv('DB_PATH'))
            self.cursor = self.sqliteConnection.cursor()

        except sqlite3.Error as error:
            print("Error estavlishing connection with data base, error: ", error)
    
    def closeConnection(self):
        self.cursor.close()
    def plainQuery(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result


