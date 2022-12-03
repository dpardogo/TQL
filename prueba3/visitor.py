import sys
from antlr4 import *

from dist.TQLParser import TQLParser

from dist.TQLListener import TQLListener
from dist.TQLVisitor import TQLVisitor
from logic.TQLDataBase import TQLDataBase
from dist.TQLLexer import TQLLexer

from re import match

from os import system, name
from os import path as pathMng
class visitor(TQLVisitor):
        
    def visitLine(self, ctx: TQLParser.LineContext):
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
                lis = ctx.specifications().list_().name()
                for i in range(len(lis)):
                    par = {
                        "name": lis[i].STRING().getText().replace('"', ''),
                        "abbr": lis[i].abbr().getText()
                    }
                    participats.append(par)

            if ctx.specifications().PLAYER() != None:
                teams = False
        
        tql = TQLDataBase()
        if(tql.createTournament(name, abbr, attributes, participats, teams)):
            print("Done")
        tql.closeConnection()
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

    def visitAdd_team(self, ctx:TQLParser.Add_teamContext):
        target = None
        toAdd = []
        if ctx.add_fs().STRING() != None:
            target = ctx.add_fs().STRING().getText().replace('"', '')
        if ctx.name() != None:
            toAdd.append({
                        "name": ctx.name().STRING().getText().replace('"', ''),
                        "abbr": None if lis[i].abbr() == None else lis[i].abbr().getText()
                    })
        if ctx.list_() != None:
            lis = ctx.list_().name()
            for i in range(len(lis)):
                par = {
                    "name": lis[i].STRING().getText().replace('"', ''),
                    "abbr": None if lis[i].abbr() == None else lis[i].abbr().getText()
                }
                toAdd.append(par)

        #print(target, toAdd)
        tql = TQLDataBase()
        execAns = tql.addTeam(target,toAdd)
        if not execAns["done"]:
            print("Error,",execAns["error"])
        else:
            print("Done")
        tql.closeConnection()

        return super().visitAdd_team(ctx)

    def visitAdd_player(self, ctx:TQLParser.Add_playerContext):
        target = None
        tournament = None
        toAdd = []
        if ctx.add_fs().STRING() != None:
            target = ctx.add_fs().STRING().getText().replace('"', '')
        if ctx.add_ss().STRING() != None:
            tournament = ctx.add_ss().STRING().getText().replace('"', '')
        if ctx.name() != None:
            toAdd.append({
                        "name": ctx.name().STRING().getText().replace('"', ''),
                        "abbr": None if lis[i].abbr() == None else lis[i].abbr().getText()
                    })
        if ctx.list_() != None:
            lis = ctx.list_().name()
            for i in range(len(lis)):
                par = {
                    "name": lis[i].STRING().getText().replace('"', ''),
                    "abbr": None if lis[i].abbr() == None else lis[i].abbr().getText()
                }
                toAdd.append(par)

        #print(target, tournament ,toAdd)

        tql = TQLDataBase()
        execAns = tql.addPlayer(target, tournament ,toAdd)
        if not execAns["done"]:
            print("Error,",execAns["error"])
        else:
            print("Done")
        tql.closeConnection()

        return super().visitAdd_player(ctx)

    def visitAdd_single_player(self, ctx:TQLParser.Add_single_playerContext):
        target = None
        toAdd = []
        if ctx.add_fs().STRING() != None:
            target = ctx.add_fs().STRING().getText().replace('"', '')
        if ctx.name() != None:
            toAdd.append({
                        "name": ctx.name().STRING().getText().replace('"', ''),
                        "abbr": None if lis[i].abbr() == None else lis[i].abbr().getText()
                    })
        if ctx.list_() != None:
            lis = ctx.list_().name()
            for i in range(len(lis)):
                par = {
                    "name": lis[i].STRING().getText().replace('"', ''),
                    "abbr": None if lis[i].abbr() == None else lis[i].abbr().getText()
                }
                toAdd.append(par)

        #print(target, toAdd)
        tql = TQLDataBase()
        execAns = tql.addSinglePlayer(target,toAdd)
        if not execAns["done"]:
            print("Error,",execAns["error"])
        else:
            print("Done")
        tql.closeConnection()

        return super().visitAdd_single_player(ctx)

    def visitDelete_team(self, ctx:TQLParser.Delete_teamContext):
        target = None
        toAdd = []
        if ctx.add_fs().STRING() != None:
            target = ctx.add_fs().STRING().getText().replace('"', '')
        if ctx.name() != None:
            toAdd.append({
                        "name": ctx.name().STRING().getText().replace('"', ''),
                    })
        if ctx.list_() != None:
            lis = ctx.list_().name()
            for i in range(len(lis)):
                par = {
                    "name": lis[i].STRING().getText().replace('"', ''),
                }
                toAdd.append(par)

        #print(target, toAdd)
        tql = TQLDataBase()
        execAns = tql.deleteTeam(target,toAdd)
        if not execAns["done"]:
            print("Error,",execAns["error"])
        else:
            print("Done")
        tql.closeConnection()

        return super().visitDelete_team(ctx)

    def visitDelete_player(self, ctx:TQLParser.Delete_playerContext):
        target = None
        tournament = None
        toAdd = []
        if ctx.add_fs().STRING() != None:
            target = ctx.add_fs().STRING().getText().replace('"', '')
        if ctx.add_ss().STRING() != None:
            tournament = ctx.add_ss().STRING().getText().replace('"', '')
        if ctx.name() != None:
            toAdd.append({
                        "name": ctx.name().STRING().getText().replace('"', ''),
                    })
        if ctx.list_() != None:
            lis = ctx.list_().name()
            for i in range(len(lis)):
                par = {
                    "name": lis[i].STRING().getText().replace('"', ''),
                }
                toAdd.append(par)

        #print(target, tournament ,toAdd)

        tql = TQLDataBase()
        execAns = tql.deletePlayer(target, tournament ,toAdd)
        if not execAns["done"]:
            print("Error,",execAns["error"])
        else:
            print("Done")
        tql.closeConnection()

        return super().visitDelete_player(ctx)

    def visitDelete_single_player(self, ctx:TQLParser.Delete_single_playerContext):
        target = None
        toAdd = []
        if ctx.add_fs().STRING() != None:
            target = ctx.add_fs().STRING().getText().replace('"', '')
        if ctx.name() != None:
            toAdd.append({
                        "name": ctx.name().STRING().getText().replace('"', ''),
                    })
        if ctx.list_() != None:
            lis = ctx.list_().name()
            for i in range(len(lis)):
                par = {
                    "name": lis[i].STRING().getText().replace('"', ''),
                }
                toAdd.append(par)

        #print(target, toAdd)
        tql = TQLDataBase()
        execAns = tql.deleteSinglePlayer(target,toAdd)
        if not execAns["done"]:
            print("Error,",execAns["error"])
        else:
            print("Done")
        tql.closeConnection()

        return super().visitDelete_single_player(ctx)

    def visitDelete_tournament(self, ctx: TQLParser.Delete_tournamentContext):
        name = ctx.name().STRING().getText().replace('"', '')
        teams= True

        if ctx.PLAYER() != None:
            teams = False
        tql = TQLDataBase()
        execAns = tql.deleteTournament(name, teams)
        if not execAns["done"]:
            print("Error,",execAns["error"])
        else:
            print("Done")
        tql.closeConnection()
        return super().visitDelete_tournament(ctx)
    def visitClear(self, ctx:TQLParser.ClearContext):
        if name == 'nt':
            system('cls')
        else:
            system('clear')
        return super().visitClear(ctx)
    def visitList_data(self, ctx:TQLParser.List_dataContext):
        tql = TQLDataBase()
        print("TOURNAMENTS:")
        tql.printTournament()
        print("TEAMS:")
        tql.printTeam()
        print("PLAYERS IN TEAMS:")
        tql.printPlayer()
        print("PLAYERS IN TOURNAMENTS:")
        tql.printSinglePlayer()
        return super().visitList_data(ctx)
    def visitExit(self, ctx:TQLParser.ExitContext):
        print("Bye bye")
        raise SystemExit
    def visitList_tournament(self, ctx:TQLParser.List_dataContext):
        tql = TQLDataBase()
        print("TOURNAMENTS:")
        tql.printTournament()
        return super().visitList_tournament(ctx)
    def visitList_team(self, ctx:TQLParser.List_player_teamContext):
        tql = TQLDataBase()
        print("TEAMS:")
        tql.printTeam()
        return super().visitList_team(ctx)
    def visitList_player_team(self, ctx:TQLParser.List_player_teamContext):
        tql = TQLDataBase()
        print("PLAYERS IN TEAMS:")
        tql.printPlayer()
        return super().visitList_player_team(ctx)
    def visitList_single_players(self, ctx:TQLParser.List_single_playersContext):
        tql = TQLDataBase()
        print("PLAYERS IN TOURNAMENTS:")
        tql.printSinglePlayer()
        return super().visitList_single_players(ctx)
    def visitRead_file(self, ctx: TQLParser.Read_fileContext):
        path = ""
        if ctx.STRING() != None:
            path = ctx.STRING().getText().replace('"', '')
        if not pathMng.isfile(path):
            print("File not found")
            return False

        input = FileStream(path)

        lexer = TQLLexer(input)
        stream = CommonTokenStream(lexer)
        parser = TQLParser(stream)
        tree = parser.program()

        obj=visitor()
        obj.visit(tree)
               
        return super().visitRead_file(ctx)
