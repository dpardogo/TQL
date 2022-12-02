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


    # Enter a parse tree produced by TQLParser#add_query.
    def enterAdd_query(self, ctx:TQLParser.Add_queryContext):
        pass

    # Exit a parse tree produced by TQLParser#add_query.
    def exitAdd_query(self, ctx:TQLParser.Add_queryContext):
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



del TQLParser