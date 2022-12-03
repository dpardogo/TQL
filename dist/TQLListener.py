# Generated from TQL.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TQLParser import TQLParser
else:
    from TQLParser import TQLParser

# This class defines a complete listener for a parse tree produced by TQLParser.
class TQLListener(ParseTreeListener):

    # Enter a parse tree produced by TQLParser#program.
    def enterProgram(self, ctx:TQLParser.ProgramContext):
        pass

    # Exit a parse tree produced by TQLParser#program.
    def exitProgram(self, ctx:TQLParser.ProgramContext):
        pass


    # Enter a parse tree produced by TQLParser#line.
    def enterLine(self, ctx:TQLParser.LineContext):
        pass

    # Exit a parse tree produced by TQLParser#line.
    def exitLine(self, ctx:TQLParser.LineContext):
        pass


    # Enter a parse tree produced by TQLParser#create_query.
    def enterCreate_query(self, ctx:TQLParser.Create_queryContext):
        pass

    # Exit a parse tree produced by TQLParser#create_query.
    def exitCreate_query(self, ctx:TQLParser.Create_queryContext):
        pass


    # Enter a parse tree produced by TQLParser#specifications.
    def enterSpecifications(self, ctx:TQLParser.SpecificationsContext):
        pass

    # Exit a parse tree produced by TQLParser#specifications.
    def exitSpecifications(self, ctx:TQLParser.SpecificationsContext):
        pass


    # Enter a parse tree produced by TQLParser#attributes.
    def enterAttributes(self, ctx:TQLParser.AttributesContext):
        pass

    # Exit a parse tree produced by TQLParser#attributes.
    def exitAttributes(self, ctx:TQLParser.AttributesContext):
        pass


    # Enter a parse tree produced by TQLParser#add_team.
    def enterAdd_team(self, ctx:TQLParser.Add_teamContext):
        pass

    # Exit a parse tree produced by TQLParser#add_team.
    def exitAdd_team(self, ctx:TQLParser.Add_teamContext):
        pass


    # Enter a parse tree produced by TQLParser#add_single_player.
    def enterAdd_single_player(self, ctx:TQLParser.Add_single_playerContext):
        pass

    # Exit a parse tree produced by TQLParser#add_single_player.
    def exitAdd_single_player(self, ctx:TQLParser.Add_single_playerContext):
        pass


    # Enter a parse tree produced by TQLParser#add_player.
    def enterAdd_player(self, ctx:TQLParser.Add_playerContext):
        pass

    # Exit a parse tree produced by TQLParser#add_player.
    def exitAdd_player(self, ctx:TQLParser.Add_playerContext):
        pass


    # Enter a parse tree produced by TQLParser#delete_tournament.
    def enterDelete_tournament(self, ctx:TQLParser.Delete_tournamentContext):
        pass

    # Exit a parse tree produced by TQLParser#delete_tournament.
    def exitDelete_tournament(self, ctx:TQLParser.Delete_tournamentContext):
        pass


    # Enter a parse tree produced by TQLParser#delete_team.
    def enterDelete_team(self, ctx:TQLParser.Delete_teamContext):
        pass

    # Exit a parse tree produced by TQLParser#delete_team.
    def exitDelete_team(self, ctx:TQLParser.Delete_teamContext):
        pass


    # Enter a parse tree produced by TQLParser#delete_single_player.
    def enterDelete_single_player(self, ctx:TQLParser.Delete_single_playerContext):
        pass

    # Exit a parse tree produced by TQLParser#delete_single_player.
    def exitDelete_single_player(self, ctx:TQLParser.Delete_single_playerContext):
        pass


    # Enter a parse tree produced by TQLParser#delete_player.
    def enterDelete_player(self, ctx:TQLParser.Delete_playerContext):
        pass

    # Exit a parse tree produced by TQLParser#delete_player.
    def exitDelete_player(self, ctx:TQLParser.Delete_playerContext):
        pass


    # Enter a parse tree produced by TQLParser#delete_query.
    def enterDelete_query(self, ctx:TQLParser.Delete_queryContext):
        pass

    # Exit a parse tree produced by TQLParser#delete_query.
    def exitDelete_query(self, ctx:TQLParser.Delete_queryContext):
        pass


    # Enter a parse tree produced by TQLParser#modify_query.
    def enterModify_query(self, ctx:TQLParser.Modify_queryContext):
        pass

    # Exit a parse tree produced by TQLParser#modify_query.
    def exitModify_query(self, ctx:TQLParser.Modify_queryContext):
        pass


    # Enter a parse tree produced by TQLParser#add_fs.
    def enterAdd_fs(self, ctx:TQLParser.Add_fsContext):
        pass

    # Exit a parse tree produced by TQLParser#add_fs.
    def exitAdd_fs(self, ctx:TQLParser.Add_fsContext):
        pass


    # Enter a parse tree produced by TQLParser#add_ss.
    def enterAdd_ss(self, ctx:TQLParser.Add_ssContext):
        pass

    # Exit a parse tree produced by TQLParser#add_ss.
    def exitAdd_ss(self, ctx:TQLParser.Add_ssContext):
        pass


    # Enter a parse tree produced by TQLParser#organize_query.
    def enterOrganize_query(self, ctx:TQLParser.Organize_queryContext):
        pass

    # Exit a parse tree produced by TQLParser#organize_query.
    def exitOrganize_query(self, ctx:TQLParser.Organize_queryContext):
        pass


    # Enter a parse tree produced by TQLParser#report_query.
    def enterReport_query(self, ctx:TQLParser.Report_queryContext):
        pass

    # Exit a parse tree produced by TQLParser#report_query.
    def exitReport_query(self, ctx:TQLParser.Report_queryContext):
        pass


    # Enter a parse tree produced by TQLParser#show_query.
    def enterShow_query(self, ctx:TQLParser.Show_queryContext):
        pass

    # Exit a parse tree produced by TQLParser#show_query.
    def exitShow_query(self, ctx:TQLParser.Show_queryContext):
        pass


    # Enter a parse tree produced by TQLParser#dtype.
    def enterDtype(self, ctx:TQLParser.DtypeContext):
        pass

    # Exit a parse tree produced by TQLParser#dtype.
    def exitDtype(self, ctx:TQLParser.DtypeContext):
        pass


    # Enter a parse tree produced by TQLParser#pair.
    def enterPair(self, ctx:TQLParser.PairContext):
        pass

    # Exit a parse tree produced by TQLParser#pair.
    def exitPair(self, ctx:TQLParser.PairContext):
        pass


    # Enter a parse tree produced by TQLParser#list.
    def enterList(self, ctx:TQLParser.ListContext):
        pass

    # Exit a parse tree produced by TQLParser#list.
    def exitList(self, ctx:TQLParser.ListContext):
        pass


    # Enter a parse tree produced by TQLParser#a_identifier.
    def enterA_identifier(self, ctx:TQLParser.A_identifierContext):
        pass

    # Exit a parse tree produced by TQLParser#a_identifier.
    def exitA_identifier(self, ctx:TQLParser.A_identifierContext):
        pass


    # Enter a parse tree produced by TQLParser#t_identifier.
    def enterT_identifier(self, ctx:TQLParser.T_identifierContext):
        pass

    # Exit a parse tree produced by TQLParser#t_identifier.
    def exitT_identifier(self, ctx:TQLParser.T_identifierContext):
        pass


    # Enter a parse tree produced by TQLParser#p_identifier.
    def enterP_identifier(self, ctx:TQLParser.P_identifierContext):
        pass

    # Exit a parse tree produced by TQLParser#p_identifier.
    def exitP_identifier(self, ctx:TQLParser.P_identifierContext):
        pass


    # Enter a parse tree produced by TQLParser#identifier.
    def enterIdentifier(self, ctx:TQLParser.IdentifierContext):
        pass

    # Exit a parse tree produced by TQLParser#identifier.
    def exitIdentifier(self, ctx:TQLParser.IdentifierContext):
        pass


    # Enter a parse tree produced by TQLParser#name.
    def enterName(self, ctx:TQLParser.NameContext):
        pass

    # Exit a parse tree produced by TQLParser#name.
    def exitName(self, ctx:TQLParser.NameContext):
        pass


    # Enter a parse tree produced by TQLParser#abbr.
    def enterAbbr(self, ctx:TQLParser.AbbrContext):
        pass

    # Exit a parse tree produced by TQLParser#abbr.
    def exitAbbr(self, ctx:TQLParser.AbbrContext):
        pass


    # Enter a parse tree produced by TQLParser#clear.
    def enterClear(self, ctx:TQLParser.ClearContext):
        pass

    # Exit a parse tree produced by TQLParser#clear.
    def exitClear(self, ctx:TQLParser.ClearContext):
        pass


    # Enter a parse tree produced by TQLParser#list_data.
    def enterList_data(self, ctx:TQLParser.List_dataContext):
        pass

    # Exit a parse tree produced by TQLParser#list_data.
    def exitList_data(self, ctx:TQLParser.List_dataContext):
        pass


    # Enter a parse tree produced by TQLParser#list_team.
    def enterList_team(self, ctx:TQLParser.List_teamContext):
        pass

    # Exit a parse tree produced by TQLParser#list_team.
    def exitList_team(self, ctx:TQLParser.List_teamContext):
        pass


    # Enter a parse tree produced by TQLParser#list_tournament.
    def enterList_tournament(self, ctx:TQLParser.List_tournamentContext):
        pass

    # Exit a parse tree produced by TQLParser#list_tournament.
    def exitList_tournament(self, ctx:TQLParser.List_tournamentContext):
        pass


    # Enter a parse tree produced by TQLParser#list_player_team.
    def enterList_player_team(self, ctx:TQLParser.List_player_teamContext):
        pass

    # Exit a parse tree produced by TQLParser#list_player_team.
    def exitList_player_team(self, ctx:TQLParser.List_player_teamContext):
        pass


    # Enter a parse tree produced by TQLParser#list_single_players.
    def enterList_single_players(self, ctx:TQLParser.List_single_playersContext):
        pass

    # Exit a parse tree produced by TQLParser#list_single_players.
    def exitList_single_players(self, ctx:TQLParser.List_single_playersContext):
        pass


    # Enter a parse tree produced by TQLParser#list_matches.
    def enterList_matches(self, ctx:TQLParser.List_matchesContext):
        pass

    # Exit a parse tree produced by TQLParser#list_matches.
    def exitList_matches(self, ctx:TQLParser.List_matchesContext):
        pass


    # Enter a parse tree produced by TQLParser#exit.
    def enterExit(self, ctx:TQLParser.ExitContext):
        pass

    # Exit a parse tree produced by TQLParser#exit.
    def exitExit(self, ctx:TQLParser.ExitContext):
        pass


    # Enter a parse tree produced by TQLParser#read_file.
    def enterRead_file(self, ctx:TQLParser.Read_fileContext):
        pass

    # Exit a parse tree produced by TQLParser#read_file.
    def exitRead_file(self, ctx:TQLParser.Read_fileContext):
        pass



del TQLParser