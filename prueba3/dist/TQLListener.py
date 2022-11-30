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


    # Enter a parse tree produced by TQLParser#specifications.
    def enterSpecifications(self, ctx:TQLParser.SpecificationsContext):
        pass

    # Exit a parse tree produced by TQLParser#specifications.
    def exitSpecifications(self, ctx:TQLParser.SpecificationsContext):
        pass


    # Enter a parse tree produced by TQLParser#name.
    def enterName(self, ctx:TQLParser.NameContext):
        pass

    # Exit a parse tree produced by TQLParser#name.
    def exitName(self, ctx:TQLParser.NameContext):
        pass


    # Enter a parse tree produced by TQLParser#command.
    def enterCommand(self, ctx:TQLParser.CommandContext):
        pass

    # Exit a parse tree produced by TQLParser#command.
    def exitCommand(self, ctx:TQLParser.CommandContext):
        pass



del TQLParser