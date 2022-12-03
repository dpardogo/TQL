import sys
from antlr4 import *

from dist.TQLParser import TQLParser

from dist.TQLListener import TQLListener
from dist.TQLVisitor import TQLVisitor
from logic.TQLDataBase import TQLDataBase

from re import match

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
        
        createTournament = TQLDataBase()
        createTournament.createTournament(name, abbr, attributes, participats, teams)
        createTournament.closeConnection()

        return super().visitCreate_query(ctx)


    def visitOrganize_query(self, ctx: TQLParser.Organize_queryContext):
        tid=self.visit(ctx.t_identifier())
        system=ctx.WORD().getText()

        organizeTournament = TQLDataBase()
        organizeTournament.organize(system,tid[0],tid[1])
        organizeTournament.closeConnection()
               
        return super().visitOrganize_query(ctx)


    def visitReport_query(self, ctx: TQLParser.Report_queryContext):
        atr=self.visit(ctx.a_identifier())
        team=self.visit(ctx.p_identifier())
        tourn=self.visit(ctx.t_identifier())

        reportTournament = TQLDataBase()
        if match("[Vv][Ii][Cc][Tt][Oo][Rr][Yy]",atr): 
            reportTournament.reportVictory(team[0],team[1],tourn[0],tourn[1]) 
        else:
            reportTournament.reportTournament(atr,team[0],team[1],tourn[0],tourn[1])
        reportTournament.closeConnection()

        return super().visitReport_query(ctx)

    def visitModify_query(self, ctx: TQLParser.Modify_queryContext):
        team=self.visit(ctx.p_identifier())
        tourn=self.visit(ctx.t_identifier())
        dic=dict([self.visit(i) for i in ctx.pair() ])

        modifyParticipants = TQLDataBase()
        modifyParticipants.modifyParticipants(team[0],team[1],tourn[0],tourn[1],dic)
        modifyParticipants.closeConnection()

        return super().visitModify_query(ctx)


    #-------------------------------Reglas intermedias------------------------------


    def visitA_identifier(self, ctx: TQLParser.A_identifierContext):
        return ctx.WORD().getText()

    def visitP_identifier(self, ctx: TQLParser.P_identifierContext):
        if ctx.WORD()!=None:
            return (ctx.WORD().getText(), True)
        else:
            return (ctx.STRING().getText().replace('"', ''), False)

    def visitT_identifier(self, ctx: TQLParser.T_identifierContext):
        if ctx.WORD()!=None:
            return (ctx.WORD().getText(), True)
        else:
            return (ctx.STRING().getText().replace('"', ''), False)

    def visitList(self, ctx: TQLParser.ListContext):
        array=[]
        for i in ctx.name():
            array.append(self.visit(i))
        return array
    
    def visitPair(self, ctx: TQLParser.PairContext):
        return (self.visit(ctx.a_identifier()),self.visit(ctx.dtype()))

    def visitDtype(self, ctx: TQLParser.DtypeContext):
        if ctx.WORD()!=None:
            return '"'+ctx.WORD().getText()+'"'
        elif ctx.INTEGER!=None:
            return ctx.INTEGER().getText()
        else:
            return ctx.STRING().getText()
        
        
    def visitName(self, ctx: TQLParser.NameContext):
        abr=''
        if ctx.abbr()!= None:
            abr=self.visit(ctx.abbr()).getText()
        return (ctx.STRING().getText(),abr)
        

    def visitAbbr(self, ctx: TQLParser.AbbrContext):
        return ctx.WORD()
