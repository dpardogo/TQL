import sys
from antlr4 import *

from dist.TQLParser import TQLParser

from dist.TQLListener import TQLListener
from dist.TQLVisitor import TQLVisitor
from logic.TQLDataBase import TQLDataBase

class visitor(TQLVisitor):
    def __init__(self,output):
        self.output=output
        
    def visitLine(self, ctx: TQLParser.LineContext):
        self.output.write("esto es una linea\n")
        return super().visitLine(ctx)

    def visitCreate_query(self, ctx: TQLParser.Create_queryContext):
        name = ctx.name().STRING().getText().replace('"', '')
        abbr = None
        attributes = []
        participatsNumber = None
        participats = []
        teams= True

        if ctx.name().abbr() != None:
            abbr = ctx.name().abbr().getText()

        if ctx.specifications() != None:
            if ctx.specifications().attributes() != None:
                attributes = ctx.specifications().attributes().WORD()
                for i in range(len(attributes)):
                    attributes[i] = attributes[i].getText()

            if ctx.specifications().INTEGER() != None:
                participatsNumber =  int(ctx.specifications().INTEGER().getText())

            if ctx.specifications().list_() != None:
                if participatsNumber != None and (participatsNumber !=
                len(ctx.specifications().list_().name())):
                    raise Exception("List must have {} elements, but list has {}".format(participatsNumber, len(ctx.specifications().list_().name())))
                participats = []
                lis = ctx.specifications().list_().name()
                for i in range(len(lis)):
                    par = {
                        "name": lis[i].STRING().getText().replace('"', ''),
                        "abbr": lis[i].abbr().getText()
                    }
                    participats.append(par)

            if ctx.specifications().PLAYER() != None:
                teams = False
        print("si llega")
        createTournament = TQLDataBase()
        createTournament.createTournament(name, abbr, attributes, participats, teams)
        createTournament.organize('RoundRobin',abbr)
        createTournament.closeConnection()
        return super().visitCreate_query(ctx)


