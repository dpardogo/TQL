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


    # Visit a parse tree produced by TQLParser#add_query.
    def visitAdd_query(self, ctx:TQLParser.Add_queryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#delete_query.
    def visitDelete_query(self, ctx:TQLParser.Delete_queryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#modify_query.
    def visitModify_query(self, ctx:TQLParser.Modify_queryContext):
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



del TQLParser