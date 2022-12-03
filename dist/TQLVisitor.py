# Generated from TQL.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TQLParser import TQLParser
else:
    from TQLParser import TQLParser

# This class defines a complete generic visitor for a parse tree produced by TQLParser.

class TQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TQLParser#program.
    def visitProgram(self, ctx:TQLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#line.
    def visitLine(self, ctx:TQLParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#create_query.
    def visitCreate_query(self, ctx:TQLParser.Create_queryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#specifications.
    def visitSpecifications(self, ctx:TQLParser.SpecificationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#attributes.
    def visitAttributes(self, ctx:TQLParser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#add_team.
    def visitAdd_team(self, ctx:TQLParser.Add_teamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#add_single_player.
    def visitAdd_single_player(self, ctx:TQLParser.Add_single_playerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#add_player.
    def visitAdd_player(self, ctx:TQLParser.Add_playerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#delete_tournament.
    def visitDelete_tournament(self, ctx:TQLParser.Delete_tournamentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#delete_team.
    def visitDelete_team(self, ctx:TQLParser.Delete_teamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#delete_single_player.
    def visitDelete_single_player(self, ctx:TQLParser.Delete_single_playerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#delete_player.
    def visitDelete_player(self, ctx:TQLParser.Delete_playerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#delete_query.
    def visitDelete_query(self, ctx:TQLParser.Delete_queryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#modify_query.
    def visitModify_query(self, ctx:TQLParser.Modify_queryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#add_fs.
    def visitAdd_fs(self, ctx:TQLParser.Add_fsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#add_ss.
    def visitAdd_ss(self, ctx:TQLParser.Add_ssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#organize_query.
    def visitOrganize_query(self, ctx:TQLParser.Organize_queryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#report_query.
    def visitReport_query(self, ctx:TQLParser.Report_queryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#show_query.
    def visitShow_query(self, ctx:TQLParser.Show_queryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#dtype.
    def visitDtype(self, ctx:TQLParser.DtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#pair.
    def visitPair(self, ctx:TQLParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#list.
    def visitList(self, ctx:TQLParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#a_identifier.
    def visitA_identifier(self, ctx:TQLParser.A_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#t_identifier.
    def visitT_identifier(self, ctx:TQLParser.T_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#p_identifier.
    def visitP_identifier(self, ctx:TQLParser.P_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#identifier.
    def visitIdentifier(self, ctx:TQLParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#name.
    def visitName(self, ctx:TQLParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#abbr.
    def visitAbbr(self, ctx:TQLParser.AbbrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#clear.
    def visitClear(self, ctx:TQLParser.ClearContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#list_data.
    def visitList_data(self, ctx:TQLParser.List_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#list_team.
    def visitList_team(self, ctx:TQLParser.List_teamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#list_tournament.
    def visitList_tournament(self, ctx:TQLParser.List_tournamentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#list_player_team.
    def visitList_player_team(self, ctx:TQLParser.List_player_teamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#list_single_players.
    def visitList_single_players(self, ctx:TQLParser.List_single_playersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#list_matches.
    def visitList_matches(self, ctx:TQLParser.List_matchesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#exit.
    def visitExit(self, ctx:TQLParser.ExitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#read_file.
    def visitRead_file(self, ctx:TQLParser.Read_fileContext):
        return self.visitChildren(ctx)



del TQLParser