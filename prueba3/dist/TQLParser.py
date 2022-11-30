# Generated from TQL.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,48,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,3,2,26,8,2,
        1,2,1,2,1,2,3,2,31,8,2,1,2,5,2,34,8,2,10,2,12,2,37,9,2,1,2,1,2,1,
        3,1,3,3,3,43,8,3,1,4,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,0,47,0,11,1,0,
        0,0,2,17,1,0,0,0,4,22,1,0,0,0,6,40,1,0,0,0,8,44,1,0,0,0,10,12,3,
        2,1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,
        15,1,0,0,0,15,16,5,0,0,1,16,1,1,0,0,0,17,18,3,8,4,0,18,19,3,6,3,
        0,19,20,3,4,2,0,20,21,5,8,0,0,21,3,1,0,0,0,22,35,5,1,0,0,23,25,5,
        6,0,0,24,26,5,7,0,0,25,24,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,0,27,
        28,5,2,0,0,28,30,5,6,0,0,29,31,5,7,0,0,30,29,1,0,0,0,30,31,1,0,0,
        0,31,32,1,0,0,0,32,34,5,3,0,0,33,23,1,0,0,0,34,37,1,0,0,0,35,33,
        1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,5,4,0,0,
        39,5,1,0,0,0,40,42,5,6,0,0,41,43,5,7,0,0,42,41,1,0,0,0,42,43,1,0,
        0,0,43,7,1,0,0,0,44,45,5,5,0,0,45,46,5,7,0,0,46,9,1,0,0,0,5,13,25,
        30,35,42
    ]

class TQLParser ( Parser ):

    grammarFileName = "TQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "':'", "';'", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "CREATE", "WORD", "WHITESPACE", "NEWLINE" ]

    RULE_program = 0
    RULE_line = 1
    RULE_specifications = 2
    RULE_name = 3
    RULE_command = 4

    ruleNames =  [ "program", "line", "specifications", "name", "command" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    CREATE=5
    WORD=6
    WHITESPACE=7
    NEWLINE=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TQLParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TQLParser.LineContext)
            else:
                return self.getTypedRuleContext(TQLParser.LineContext,i)


        def getRuleIndex(self):
            return TQLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = TQLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.line()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5):
                    break

            self.state = 15
            self.match(TQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(TQLParser.CommandContext,0)


        def name(self):
            return self.getTypedRuleContext(TQLParser.NameContext,0)


        def specifications(self):
            return self.getTypedRuleContext(TQLParser.SpecificationsContext,0)


        def NEWLINE(self):
            return self.getToken(TQLParser.NEWLINE, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = TQLParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.command()
            self.state = 18
            self.name()
            self.state = 19
            self.specifications()
            self.state = 20
            self.match(TQLParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecificationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(TQLParser.WORD)
            else:
                return self.getToken(TQLParser.WORD, i)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(TQLParser.WHITESPACE)
            else:
                return self.getToken(TQLParser.WHITESPACE, i)

        def getRuleIndex(self):
            return TQLParser.RULE_specifications

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecifications" ):
                listener.enterSpecifications(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecifications" ):
                listener.exitSpecifications(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecifications" ):
                return visitor.visitSpecifications(self)
            else:
                return visitor.visitChildren(self)




    def specifications(self):

        localctx = TQLParser.SpecificationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_specifications)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(TQLParser.T__0)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 23
                self.match(TQLParser.WORD)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 24
                    self.match(TQLParser.WHITESPACE)


                self.state = 27
                self.match(TQLParser.T__1)
                self.state = 28
                self.match(TQLParser.WORD)
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 29
                    self.match(TQLParser.WHITESPACE)


                self.state = 32
                self.match(TQLParser.T__2)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(TQLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(TQLParser.WORD, 0)

        def WHITESPACE(self):
            return self.getToken(TQLParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = TQLParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(TQLParser.WORD)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 41
                self.match(TQLParser.WHITESPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(TQLParser.CREATE, 0)

        def WHITESPACE(self):
            return self.getToken(TQLParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = TQLParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(TQLParser.CREATE)
            self.state = 45
            self.match(TQLParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





