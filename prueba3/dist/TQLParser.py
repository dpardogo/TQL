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
        4,1,32,173,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        4,0,42,8,0,11,0,12,0,43,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,
        2,1,2,1,2,1,2,3,2,59,8,2,1,3,1,3,1,3,1,3,3,3,65,8,3,1,3,3,3,68,8,
        3,1,4,1,4,1,4,1,4,5,4,74,8,4,10,4,12,4,77,9,4,1,4,1,4,1,5,1,5,1,
        5,1,5,1,5,1,5,3,5,87,8,5,1,6,1,6,1,6,1,6,3,6,93,8,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,107,8,7,10,7,12,7,110,9,
        7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        10,1,10,1,10,1,10,3,10,131,8,10,1,10,1,10,1,10,1,11,1,11,1,11,3,
        11,139,8,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,5,13,149,8,13,
        10,13,12,13,152,9,13,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,17,
        1,17,1,18,1,18,1,18,1,18,1,18,3,18,169,8,18,1,19,1,19,1,19,0,0,20,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,3,1,0,29,
        30,1,0,26,27,1,0,28,29,172,0,41,1,0,0,0,2,52,1,0,0,0,4,54,1,0,0,
        0,6,60,1,0,0,0,8,69,1,0,0,0,10,80,1,0,0,0,12,88,1,0,0,0,14,97,1,
        0,0,0,16,113,1,0,0,0,18,119,1,0,0,0,20,126,1,0,0,0,22,138,1,0,0,
        0,24,140,1,0,0,0,26,144,1,0,0,0,28,155,1,0,0,0,30,157,1,0,0,0,32,
        159,1,0,0,0,34,161,1,0,0,0,36,163,1,0,0,0,38,170,1,0,0,0,40,42,3,
        2,1,0,41,40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,
        1,1,0,0,0,45,53,3,4,2,0,46,53,3,10,5,0,47,53,3,12,6,0,48,53,3,14,
        7,0,49,53,3,16,8,0,50,53,3,18,9,0,51,53,3,20,10,0,52,45,1,0,0,0,
        52,46,1,0,0,0,52,47,1,0,0,0,52,48,1,0,0,0,52,49,1,0,0,0,52,50,1,
        0,0,0,52,51,1,0,0,0,53,3,1,0,0,0,54,55,5,9,0,0,55,56,5,10,0,0,56,
        58,3,36,18,0,57,59,3,6,3,0,58,57,1,0,0,0,58,59,1,0,0,0,59,5,1,0,
        0,0,60,64,3,8,4,0,61,62,5,11,0,0,62,63,5,30,0,0,63,65,5,12,0,0,64,
        61,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,68,3,26,13,0,67,66,1,0,
        0,0,67,68,1,0,0,0,68,7,1,0,0,0,69,70,5,1,0,0,70,75,5,29,0,0,71,72,
        5,2,0,0,72,74,5,29,0,0,73,71,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,
        75,76,1,0,0,0,76,78,1,0,0,0,77,75,1,0,0,0,78,79,5,3,0,0,79,9,1,0,
        0,0,80,81,5,13,0,0,81,82,5,12,0,0,82,83,5,14,0,0,83,86,3,30,15,0,
        84,87,3,36,18,0,85,87,3,26,13,0,86,84,1,0,0,0,86,85,1,0,0,0,87,11,
        1,0,0,0,88,92,5,17,0,0,89,93,5,29,0,0,90,93,3,8,4,0,91,93,3,26,13,
        0,92,89,1,0,0,0,92,90,1,0,0,0,92,91,1,0,0,0,93,94,1,0,0,0,94,95,
        5,18,0,0,95,96,3,30,15,0,96,13,1,0,0,0,97,98,5,21,0,0,98,99,5,12,
        0,0,99,100,7,0,0,0,100,101,5,18,0,0,101,102,3,30,15,0,102,103,5,
        4,0,0,103,108,3,24,12,0,104,105,5,2,0,0,105,107,3,24,12,0,106,104,
        1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,111,
        1,0,0,0,110,108,1,0,0,0,111,112,5,5,0,0,112,15,1,0,0,0,113,114,5,
        15,0,0,114,115,5,10,0,0,115,116,3,30,15,0,116,117,5,19,0,0,117,118,
        5,29,0,0,118,17,1,0,0,0,119,120,5,20,0,0,120,121,3,28,14,0,121,122,
        5,23,0,0,122,123,3,32,16,0,123,124,5,18,0,0,124,125,3,30,15,0,125,
        19,1,0,0,0,126,127,5,25,0,0,127,130,7,1,0,0,128,129,5,23,0,0,129,
        131,3,32,16,0,130,128,1,0,0,0,130,131,1,0,0,0,131,132,1,0,0,0,132,
        133,5,18,0,0,133,134,3,30,15,0,134,21,1,0,0,0,135,139,5,29,0,0,136,
        139,5,30,0,0,137,139,3,26,13,0,138,135,1,0,0,0,138,136,1,0,0,0,138,
        137,1,0,0,0,139,23,1,0,0,0,140,141,5,29,0,0,141,142,5,6,0,0,142,
        143,3,22,11,0,143,25,1,0,0,0,144,145,5,7,0,0,145,150,3,36,18,0,146,
        147,5,2,0,0,147,149,3,36,18,0,148,146,1,0,0,0,149,152,1,0,0,0,150,
        148,1,0,0,0,150,151,1,0,0,0,151,153,1,0,0,0,152,150,1,0,0,0,153,
        154,5,8,0,0,154,27,1,0,0,0,155,156,5,29,0,0,156,29,1,0,0,0,157,158,
        7,2,0,0,158,31,1,0,0,0,159,160,7,2,0,0,160,33,1,0,0,0,161,162,5,
        29,0,0,162,35,1,0,0,0,163,168,5,28,0,0,164,165,5,1,0,0,165,166,3,
        38,19,0,166,167,5,3,0,0,167,169,1,0,0,0,168,164,1,0,0,0,168,169,
        1,0,0,0,169,37,1,0,0,0,170,171,5,29,0,0,171,39,1,0,0,0,13,43,52,
        58,64,67,75,86,92,108,130,138,150,168
    ]

class TQLParser ( Parser ):

    grammarFileName = "TQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'{'", "'}'", "':'", 
                     "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "CREATE", "TOURNAMENT", "WITH", "PARTICIPANT", 
                      "ADD", "TO", "ORGANIZE", "ATTRIBUTE", "DELETE", "FROM", 
                      "BY", "REPORT", "MODIFY", "MATCH", "OF", "ID", "SHOW", 
                      "PHASE", "SUMMARY", "STRING", "WORD", "INTEGER", "WHITESPACE", 
                      "NEWLINE" ]

    RULE_program = 0
    RULE_line = 1
    RULE_create_query = 2
    RULE_specifications = 3
    RULE_attributes = 4
    RULE_add_query = 5
    RULE_delete_query = 6
    RULE_modify_query = 7
    RULE_organize_query = 8
    RULE_report_query = 9
    RULE_show_query = 10
    RULE_dtype = 11
    RULE_pair = 12
    RULE_list = 13
    RULE_a_identifier = 14
    RULE_t_identifier = 15
    RULE_p_identifier = 16
    RULE_identifier = 17
    RULE_name = 18
    RULE_abbr = 19

    ruleNames =  [ "program", "line", "create_query", "specifications", 
                   "attributes", "add_query", "delete_query", "modify_query", 
                   "organize_query", "report_query", "show_query", "dtype", 
                   "pair", "list", "a_identifier", "t_identifier", "p_identifier", 
                   "identifier", "name", "abbr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    CREATE=9
    TOURNAMENT=10
    WITH=11
    PARTICIPANT=12
    ADD=13
    TO=14
    ORGANIZE=15
    ATTRIBUTE=16
    DELETE=17
    FROM=18
    BY=19
    REPORT=20
    MODIFY=21
    MATCH=22
    OF=23
    ID=24
    SHOW=25
    PHASE=26
    SUMMARY=27
    STRING=28
    WORD=29
    INTEGER=30
    WHITESPACE=31
    NEWLINE=32

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
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.line()
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 36872704) != 0):
                    break

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

        def create_query(self):
            return self.getTypedRuleContext(TQLParser.Create_queryContext,0)


        def add_query(self):
            return self.getTypedRuleContext(TQLParser.Add_queryContext,0)


        def delete_query(self):
            return self.getTypedRuleContext(TQLParser.Delete_queryContext,0)


        def modify_query(self):
            return self.getTypedRuleContext(TQLParser.Modify_queryContext,0)


        def organize_query(self):
            return self.getTypedRuleContext(TQLParser.Organize_queryContext,0)


        def report_query(self):
            return self.getTypedRuleContext(TQLParser.Report_queryContext,0)


        def show_query(self):
            return self.getTypedRuleContext(TQLParser.Show_queryContext,0)


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
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.create_query()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.add_query()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.delete_query()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.modify_query()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.organize_query()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 6)
                self.state = 50
                self.report_query()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 7)
                self.state = 51
                self.show_query()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Create_queryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(TQLParser.CREATE, 0)

        def TOURNAMENT(self):
            return self.getToken(TQLParser.TOURNAMENT, 0)

        def name(self):
            return self.getTypedRuleContext(TQLParser.NameContext,0)


        def specifications(self):
            return self.getTypedRuleContext(TQLParser.SpecificationsContext,0)


        def getRuleIndex(self):
            return TQLParser.RULE_create_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate_query" ):
                listener.enterCreate_query(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate_query" ):
                listener.exitCreate_query(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreate_query" ):
                return visitor.visitCreate_query(self)
            else:
                return visitor.visitChildren(self)




    def create_query(self):

        localctx = TQLParser.Create_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_create_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(TQLParser.CREATE)
            self.state = 55
            self.match(TQLParser.TOURNAMENT)
            self.state = 56
            self.name()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 57
                self.specifications()


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

        def attributes(self):
            return self.getTypedRuleContext(TQLParser.AttributesContext,0)


        def WITH(self):
            return self.getToken(TQLParser.WITH, 0)

        def INTEGER(self):
            return self.getToken(TQLParser.INTEGER, 0)

        def PARTICIPANT(self):
            return self.getToken(TQLParser.PARTICIPANT, 0)

        def list_(self):
            return self.getTypedRuleContext(TQLParser.ListContext,0)


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
        self.enterRule(localctx, 6, self.RULE_specifications)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.attributes()
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 61
                self.match(TQLParser.WITH)
                self.state = 62
                self.match(TQLParser.INTEGER)
                self.state = 63
                self.match(TQLParser.PARTICIPANT)


            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 66
                self.list_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(TQLParser.WORD)
            else:
                return self.getToken(TQLParser.WORD, i)

        def getRuleIndex(self):
            return TQLParser.RULE_attributes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributes" ):
                listener.enterAttributes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributes" ):
                listener.exitAttributes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributes" ):
                return visitor.visitAttributes(self)
            else:
                return visitor.visitChildren(self)




    def attributes(self):

        localctx = TQLParser.AttributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attributes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(TQLParser.T__0)
            self.state = 70
            self.match(TQLParser.WORD)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 71
                self.match(TQLParser.T__1)
                self.state = 72
                self.match(TQLParser.WORD)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(TQLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_queryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(TQLParser.ADD, 0)

        def PARTICIPANT(self):
            return self.getToken(TQLParser.PARTICIPANT, 0)

        def TO(self):
            return self.getToken(TQLParser.TO, 0)

        def t_identifier(self):
            return self.getTypedRuleContext(TQLParser.T_identifierContext,0)


        def name(self):
            return self.getTypedRuleContext(TQLParser.NameContext,0)


        def list_(self):
            return self.getTypedRuleContext(TQLParser.ListContext,0)


        def getRuleIndex(self):
            return TQLParser.RULE_add_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_query" ):
                listener.enterAdd_query(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_query" ):
                listener.exitAdd_query(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_query" ):
                return visitor.visitAdd_query(self)
            else:
                return visitor.visitChildren(self)




    def add_query(self):

        localctx = TQLParser.Add_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_add_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(TQLParser.ADD)
            self.state = 81
            self.match(TQLParser.PARTICIPANT)
            self.state = 82
            self.match(TQLParser.TO)
            self.state = 83
            self.t_identifier()
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.state = 84
                self.name()
                pass
            elif token in [7]:
                self.state = 85
                self.list_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Delete_queryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(TQLParser.DELETE, 0)

        def FROM(self):
            return self.getToken(TQLParser.FROM, 0)

        def t_identifier(self):
            return self.getTypedRuleContext(TQLParser.T_identifierContext,0)


        def WORD(self):
            return self.getToken(TQLParser.WORD, 0)

        def attributes(self):
            return self.getTypedRuleContext(TQLParser.AttributesContext,0)


        def list_(self):
            return self.getTypedRuleContext(TQLParser.ListContext,0)


        def getRuleIndex(self):
            return TQLParser.RULE_delete_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete_query" ):
                listener.enterDelete_query(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete_query" ):
                listener.exitDelete_query(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelete_query" ):
                return visitor.visitDelete_query(self)
            else:
                return visitor.visitChildren(self)




    def delete_query(self):

        localctx = TQLParser.Delete_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_delete_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(TQLParser.DELETE)
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.state = 89
                self.match(TQLParser.WORD)
                pass
            elif token in [1]:
                self.state = 90
                self.attributes()
                pass
            elif token in [7]:
                self.state = 91
                self.list_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 94
            self.match(TQLParser.FROM)
            self.state = 95
            self.t_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Modify_queryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODIFY(self):
            return self.getToken(TQLParser.MODIFY, 0)

        def PARTICIPANT(self):
            return self.getToken(TQLParser.PARTICIPANT, 0)

        def FROM(self):
            return self.getToken(TQLParser.FROM, 0)

        def t_identifier(self):
            return self.getTypedRuleContext(TQLParser.T_identifierContext,0)


        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TQLParser.PairContext)
            else:
                return self.getTypedRuleContext(TQLParser.PairContext,i)


        def WORD(self):
            return self.getToken(TQLParser.WORD, 0)

        def INTEGER(self):
            return self.getToken(TQLParser.INTEGER, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_modify_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModify_query" ):
                listener.enterModify_query(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModify_query" ):
                listener.exitModify_query(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModify_query" ):
                return visitor.visitModify_query(self)
            else:
                return visitor.visitChildren(self)




    def modify_query(self):

        localctx = TQLParser.Modify_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_modify_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(TQLParser.MODIFY)
            self.state = 98
            self.match(TQLParser.PARTICIPANT)
            self.state = 99
            _la = self._input.LA(1)
            if not(_la==29 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 100
            self.match(TQLParser.FROM)
            self.state = 101
            self.t_identifier()
            self.state = 102
            self.match(TQLParser.T__3)
            self.state = 103
            self.pair()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 104
                self.match(TQLParser.T__1)
                self.state = 105
                self.pair()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self.match(TQLParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Organize_queryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORGANIZE(self):
            return self.getToken(TQLParser.ORGANIZE, 0)

        def TOURNAMENT(self):
            return self.getToken(TQLParser.TOURNAMENT, 0)

        def t_identifier(self):
            return self.getTypedRuleContext(TQLParser.T_identifierContext,0)


        def BY(self):
            return self.getToken(TQLParser.BY, 0)

        def WORD(self):
            return self.getToken(TQLParser.WORD, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_organize_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrganize_query" ):
                listener.enterOrganize_query(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrganize_query" ):
                listener.exitOrganize_query(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrganize_query" ):
                return visitor.visitOrganize_query(self)
            else:
                return visitor.visitChildren(self)




    def organize_query(self):

        localctx = TQLParser.Organize_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_organize_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(TQLParser.ORGANIZE)
            self.state = 114
            self.match(TQLParser.TOURNAMENT)
            self.state = 115
            self.t_identifier()
            self.state = 116
            self.match(TQLParser.BY)
            self.state = 117
            self.match(TQLParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Report_queryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPORT(self):
            return self.getToken(TQLParser.REPORT, 0)

        def a_identifier(self):
            return self.getTypedRuleContext(TQLParser.A_identifierContext,0)


        def OF(self):
            return self.getToken(TQLParser.OF, 0)

        def p_identifier(self):
            return self.getTypedRuleContext(TQLParser.P_identifierContext,0)


        def FROM(self):
            return self.getToken(TQLParser.FROM, 0)

        def t_identifier(self):
            return self.getTypedRuleContext(TQLParser.T_identifierContext,0)


        def getRuleIndex(self):
            return TQLParser.RULE_report_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReport_query" ):
                listener.enterReport_query(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReport_query" ):
                listener.exitReport_query(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReport_query" ):
                return visitor.visitReport_query(self)
            else:
                return visitor.visitChildren(self)




    def report_query(self):

        localctx = TQLParser.Report_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_report_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(TQLParser.REPORT)
            self.state = 120
            self.a_identifier()
            self.state = 121
            self.match(TQLParser.OF)
            self.state = 122
            self.p_identifier()
            self.state = 123
            self.match(TQLParser.FROM)
            self.state = 124
            self.t_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Show_queryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHOW(self):
            return self.getToken(TQLParser.SHOW, 0)

        def FROM(self):
            return self.getToken(TQLParser.FROM, 0)

        def t_identifier(self):
            return self.getTypedRuleContext(TQLParser.T_identifierContext,0)


        def PHASE(self):
            return self.getToken(TQLParser.PHASE, 0)

        def SUMMARY(self):
            return self.getToken(TQLParser.SUMMARY, 0)

        def OF(self):
            return self.getToken(TQLParser.OF, 0)

        def p_identifier(self):
            return self.getTypedRuleContext(TQLParser.P_identifierContext,0)


        def getRuleIndex(self):
            return TQLParser.RULE_show_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShow_query" ):
                listener.enterShow_query(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShow_query" ):
                listener.exitShow_query(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShow_query" ):
                return visitor.visitShow_query(self)
            else:
                return visitor.visitChildren(self)




    def show_query(self):

        localctx = TQLParser.Show_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_show_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(TQLParser.SHOW)
            self.state = 127
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 128
                self.match(TQLParser.OF)
                self.state = 129
                self.p_identifier()


            self.state = 132
            self.match(TQLParser.FROM)
            self.state = 133
            self.t_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(TQLParser.WORD, 0)

        def INTEGER(self):
            return self.getToken(TQLParser.INTEGER, 0)

        def list_(self):
            return self.getTypedRuleContext(TQLParser.ListContext,0)


        def getRuleIndex(self):
            return TQLParser.RULE_dtype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDtype" ):
                listener.enterDtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDtype" ):
                listener.exitDtype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDtype" ):
                return visitor.visitDtype(self)
            else:
                return visitor.visitChildren(self)




    def dtype(self):

        localctx = TQLParser.DtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dtype)
        try:
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(TQLParser.WORD)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.match(TQLParser.INTEGER)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.list_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(TQLParser.WORD, 0)

        def dtype(self):
            return self.getTypedRuleContext(TQLParser.DtypeContext,0)


        def getRuleIndex(self):
            return TQLParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)




    def pair(self):

        localctx = TQLParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(TQLParser.WORD)
            self.state = 141
            self.match(TQLParser.T__5)
            self.state = 142
            self.dtype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TQLParser.NameContext)
            else:
                return self.getTypedRuleContext(TQLParser.NameContext,i)


        def getRuleIndex(self):
            return TQLParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = TQLParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(TQLParser.T__6)
            self.state = 145
            self.name()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 146
                self.match(TQLParser.T__1)
                self.state = 147
                self.name()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self.match(TQLParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class A_identifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(TQLParser.WORD, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_a_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA_identifier" ):
                listener.enterA_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA_identifier" ):
                listener.exitA_identifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA_identifier" ):
                return visitor.visitA_identifier(self)
            else:
                return visitor.visitChildren(self)




    def a_identifier(self):

        localctx = TQLParser.A_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_a_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(TQLParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_identifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TQLParser.STRING, 0)

        def WORD(self):
            return self.getToken(TQLParser.WORD, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_t_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_identifier" ):
                listener.enterT_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_identifier" ):
                listener.exitT_identifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_identifier" ):
                return visitor.visitT_identifier(self)
            else:
                return visitor.visitChildren(self)




    def t_identifier(self):

        localctx = TQLParser.T_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_t_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class P_identifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TQLParser.STRING, 0)

        def WORD(self):
            return self.getToken(TQLParser.WORD, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_p_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_identifier" ):
                listener.enterP_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_identifier" ):
                listener.exitP_identifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_identifier" ):
                return visitor.visitP_identifier(self)
            else:
                return visitor.visitChildren(self)




    def p_identifier(self):

        localctx = TQLParser.P_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_p_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(TQLParser.WORD, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = TQLParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(TQLParser.WORD)
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

        def STRING(self):
            return self.getToken(TQLParser.STRING, 0)

        def abbr(self):
            return self.getTypedRuleContext(TQLParser.AbbrContext,0)


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
        self.enterRule(localctx, 36, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(TQLParser.STRING)
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 164
                self.match(TQLParser.T__0)
                self.state = 165
                self.abbr()
                self.state = 166
                self.match(TQLParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AbbrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(TQLParser.WORD, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_abbr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbbr" ):
                listener.enterAbbr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbbr" ):
                listener.exitAbbr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbbr" ):
                return visitor.visitAbbr(self)
            else:
                return visitor.visitChildren(self)




    def abbr(self):

        localctx = TQLParser.AbbrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_abbr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(TQLParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





