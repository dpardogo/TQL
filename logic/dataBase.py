from TQLDataBase import TQLDataBase

a = TQLDataBase()

a.printTable(a.plainQuery("SELECT name FROM sqlite_master WHERE type='table';"))
a.printTournament()
a.printTeam()
a.printPlayer()
a.printSinglePlayer()