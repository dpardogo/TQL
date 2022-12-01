import sqlite3
import random

class Tournament:

    name=''
    teams=set({})
    attributes=[]
    databasePath=''

    def __init__(self, name, attributes, teams):
        
        self.name=name
        
    def addTeams(self,list):
        self.teams=self.teams | list

    def organize(self):
        pass

    def show(self):
        pass

    def report(self):
        pass



class Elimination(Tournament):
    def organize(self):
        return super().organize()

    def show(self):
        return super().show()
    


class DoubleElimination(Tournament):
    def organize(self):
        return super().organize()

    def show(self):
        return super().show()



class RoundRobin(Tournament):
    def organize(self):
        return super().organize()

class SwissSystem(Tournament):
    def organize(self):
        return super().organize()


