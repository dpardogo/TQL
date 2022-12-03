import sys
from antlr4 import *

from dist.TQLParser import TQLParser

from dist.TQLListener import TQLListener
from dist.TQLVisitor import TQLVisitor
from logic.TQLDataBase import TQLDataBase
from dist.TQLLexer import TQLLexer

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