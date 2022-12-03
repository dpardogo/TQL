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
        
        createTournament = TQLDataBase()
        createTournament.createTournament(name, abbr, attributes, participats, teams)
        createTournament.organize('Knockout',abbr,True)
        createTournament.closeConnection()

        return super().visitCreate_query(ctx)


    def visitDelete_query(self, ctx: TQLParser.Delete_queryContext):
        tourn=self.visit(ctx.t_identifier)
        todel=None
        if ctx.WORD()!= None:
            todel=[ctx.WORD().getText()]
        elif ctx.list_()!= None:
            todel=self.visit(ctx.list_())

        if todel!=None:
            deleteParticipant = TQLDataBase()
            deleteParticipant.deleteParticipant(tourn,todel)
            deleteParticipant.closeConnection()
            return
        else:
            todel=self.visit(ctx.attributes)
            deleteAtributes = TQLDataBase()
            deleteAtributes.deleteAtributes(tourn,todel)
            deleteAtributes.closeConnection()
            return


    def visitOrganize_query(self, ctx: TQLParser.Organize_queryContext):
        tid=self.visit(ctx.t_identifier())
        system=ctx.WORD()

        organizeTournament = TQLDataBase()
        organizeTournament.organize(system,tid[0],tid[1])
        organizeTournament.closeConnection()
               
        return super().visitOrganize_query(ctx)


    def visitReport_query(self, ctx: TQLParser.Report_queryContext):
        atr=self.visit(ctx.a_identifier)
        team=self.visit(ctx.p_identifier)
        tourn=self.visit(ctx.t_identifier)

        reportTournament = TQLDataBase()
        reportTournament.reportTournament(atr,team[0],team[1],tourn[0],tourn[1])
        reportTournament.closeConnection()

        return super().visitReport_query(ctx)



    def visitA_identifier(self, ctx: TQLParser.A_identifierContext):
        return ctx.WORD()

    def visitP_identifier(self, ctx: TQLParser.P_identifierContext):
        if ctx.WORD()!=None:
            return (ctx.WORD().getText(), False)
        else:
            return (ctx.STRING().getText().replace('"', ''), True)

    def visitT_identifier(self, ctx: TQLParser.T_identifierContext):
        if ctx.WORD()!=None:
            return (ctx.WORD().getText(), False)
        else:
            return (ctx.STRING().getText().replace('"', ''), True)

    def visitList(self, ctx: TQLParser.ListContext):
        array=[]
        for i in ctx.name():
            array.append(self.visit(i))
        return array
   
    def visitAttributes(self, ctx: TQLParser.AttributesContext):
        array=[]
        for i in ctx.WORD():
            array.append(i.getText())
        return array
        
"""
    def visitSpecifications(self, ctx: TQLParser.SpecificationsContext):
        array=[]
        if ctx.list_()!= None:
            array=self.visit(ctx.list_())
        
        if ctx.INTEGER()!=None:
            n=int(ctx.INTEGER().getText())
            while( len(array)<n):
                array.append(("participant"+str(len(array)),"PR"+str(len(array))))

        return (self.visit(ctx.attributes),array)

    
    
    

    

    def visitName(self, ctx: TQLParser.NameContext):
        abr=''
        if ctx.abbr()!= None:
            abr=self.visit(ctx.abbr()).getText()
        return (ctx.STRING().getText(),abr)
        

    def visitAbbr(self, ctx: TQLParser.AbbrContext):
        return ctx.WORD()
"""