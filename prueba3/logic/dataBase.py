import sqlite3
class TQLDataBase:
    def __init__(self):
        try:
            self.sqliteConnection = sqlite3.connect('TQL.db')
            self.cursor = self.sqliteConnection.cursor()
        except sqlite3.Error as error:
            print("Error estavlishing connection with data base, error: ", error)
    def plainQuery(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(result)
    def closeConnection(self):
        self.cursor.close()
    def dropSchema(self):
        self.cursor.execute("DROP TABLE IF EXISTS tournaments")

data = TQLDataBase()
table = """ CREATE TABLE GEEK (
            Email VARCHAR(255) NOT NULL,
            First_Name CHAR(25) NOT NULL,
            Last_Name CHAR(25),
            Score INT
        ); """
data.plainQuery(query = "SELECT name FROM sqlite_master WHERE type='table' AND name='GEEK';")


