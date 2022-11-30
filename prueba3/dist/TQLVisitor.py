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


    # Visit a parse tree produced by TQLParser#specifications.
    def visitSpecifications(self, ctx:TQLParser.SpecificationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#name.
    def visitName(self, ctx:TQLParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TQLParser#command.
    def visitCommand(self, ctx:TQLParser.CommandContext):
        return self.visitChildren(ctx)



del TQLParser