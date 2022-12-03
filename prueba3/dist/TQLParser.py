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
        4,1,41,311,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,1,0,4,0,74,8,0,11,0,12,0,75,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,98,8,1,1,2,1,2,1,2,1,2,3,2,104,8,2,1,3,1,3,1,3,1,3,3,3,110,
        8,3,1,3,3,3,113,8,3,1,3,1,3,3,3,117,8,3,1,4,1,4,1,4,1,4,5,4,123,
        8,4,10,4,12,4,126,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,137,
        8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,146,8,6,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,3,7,157,8,7,1,8,1,8,1,8,1,8,1,8,3,8,164,8,8,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,3,9,173,8,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,3,10,182,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        3,11,193,8,11,1,12,1,12,1,12,1,12,3,12,199,8,12,1,12,1,12,1,12,1,
        13,1,13,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,
        15,217,8,15,10,15,12,15,220,9,15,1,15,1,15,1,16,1,16,1,16,1,16,1,
        16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,3,
        18,241,8,18,1,18,1,18,1,18,1,19,1,19,1,19,3,19,249,8,19,1,20,1,20,
        1,20,1,20,1,21,1,21,1,21,1,21,5,21,259,8,21,10,21,12,21,262,9,21,
        1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,26,
        1,26,1,26,3,26,279,8,26,1,27,1,27,1,28,1,28,1,29,1,29,1,29,1,30,
        1,30,1,30,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,
        1,33,1,33,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,0,0,36,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,60,62,64,66,68,70,0,4,1,0,28,29,1,0,39,40,1,0,26,27,
        1,0,38,39,314,0,73,1,0,0,0,2,97,1,0,0,0,4,99,1,0,0,0,6,105,1,0,0,
        0,8,118,1,0,0,0,10,129,1,0,0,0,12,138,1,0,0,0,14,147,1,0,0,0,16,
        158,1,0,0,0,18,165,1,0,0,0,20,174,1,0,0,0,22,183,1,0,0,0,24,194,
        1,0,0,0,26,203,1,0,0,0,28,205,1,0,0,0,30,207,1,0,0,0,32,223,1,0,
        0,0,34,229,1,0,0,0,36,236,1,0,0,0,38,248,1,0,0,0,40,250,1,0,0,0,
        42,254,1,0,0,0,44,265,1,0,0,0,46,267,1,0,0,0,48,269,1,0,0,0,50,271,
        1,0,0,0,52,273,1,0,0,0,54,280,1,0,0,0,56,282,1,0,0,0,58,284,1,0,
        0,0,60,287,1,0,0,0,62,290,1,0,0,0,64,293,1,0,0,0,66,298,1,0,0,0,
        68,303,1,0,0,0,70,305,1,0,0,0,72,74,3,2,1,0,73,72,1,0,0,0,74,75,
        1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,1,1,0,0,0,77,98,3,4,2,0,78,
        98,3,10,5,0,79,98,3,12,6,0,80,98,3,14,7,0,81,98,3,16,8,0,82,98,3,
        18,9,0,83,98,3,22,11,0,84,98,3,20,10,0,85,98,3,30,15,0,86,98,3,32,
        16,0,87,98,3,34,17,0,88,98,3,36,18,0,89,98,3,56,28,0,90,98,3,58,
        29,0,91,98,3,68,34,0,92,98,3,62,31,0,93,98,3,60,30,0,94,98,3,64,
        32,0,95,98,3,66,33,0,96,98,3,70,35,0,97,77,1,0,0,0,97,78,1,0,0,0,
        97,79,1,0,0,0,97,80,1,0,0,0,97,81,1,0,0,0,97,82,1,0,0,0,97,83,1,
        0,0,0,97,84,1,0,0,0,97,85,1,0,0,0,97,86,1,0,0,0,97,87,1,0,0,0,97,
        88,1,0,0,0,97,89,1,0,0,0,97,90,1,0,0,0,97,91,1,0,0,0,97,92,1,0,0,
        0,97,93,1,0,0,0,97,94,1,0,0,0,97,95,1,0,0,0,97,96,1,0,0,0,98,3,1,
        0,0,0,99,100,5,9,0,0,100,101,5,10,0,0,101,103,3,52,26,0,102,104,
        3,6,3,0,103,102,1,0,0,0,103,104,1,0,0,0,104,5,1,0,0,0,105,109,3,
        8,4,0,106,107,5,11,0,0,107,108,5,40,0,0,108,110,5,12,0,0,109,106,
        1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,113,3,42,21,0,112,111,
        1,0,0,0,112,113,1,0,0,0,113,116,1,0,0,0,114,115,5,30,0,0,115,117,
        7,0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,7,1,0,0,0,118,119,5,
        1,0,0,119,124,5,39,0,0,120,121,5,2,0,0,121,123,5,39,0,0,122,120,
        1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,127,
        1,0,0,0,126,124,1,0,0,0,127,128,5,3,0,0,128,9,1,0,0,0,129,130,5,
        13,0,0,130,131,5,28,0,0,131,132,5,31,0,0,132,133,5,10,0,0,133,136,
        3,26,13,0,134,137,3,52,26,0,135,137,3,42,21,0,136,134,1,0,0,0,136,
        135,1,0,0,0,137,11,1,0,0,0,138,139,5,13,0,0,139,140,5,29,0,0,140,
        141,5,31,0,0,141,142,5,10,0,0,142,145,3,26,13,0,143,146,3,52,26,
        0,144,146,3,42,21,0,145,143,1,0,0,0,145,144,1,0,0,0,146,13,1,0,0,
        0,147,148,5,13,0,0,148,149,5,29,0,0,149,150,5,14,0,0,150,151,3,26,
        13,0,151,152,5,31,0,0,152,153,5,10,0,0,153,156,3,28,14,0,154,157,
        3,52,26,0,155,157,3,42,21,0,156,154,1,0,0,0,156,155,1,0,0,0,157,
        15,1,0,0,0,158,159,5,17,0,0,159,160,5,10,0,0,160,163,3,52,26,0,161,
        162,5,30,0,0,162,164,7,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,
        17,1,0,0,0,165,166,5,17,0,0,166,167,5,28,0,0,167,168,5,31,0,0,168,
        169,5,10,0,0,169,172,3,26,13,0,170,173,3,52,26,0,171,173,3,42,21,
        0,172,170,1,0,0,0,172,171,1,0,0,0,173,19,1,0,0,0,174,175,5,17,0,
        0,175,176,5,29,0,0,176,177,5,31,0,0,177,178,5,10,0,0,178,181,3,26,
        13,0,179,182,3,52,26,0,180,182,3,42,21,0,181,179,1,0,0,0,181,180,
        1,0,0,0,182,21,1,0,0,0,183,184,5,17,0,0,184,185,5,29,0,0,185,186,
        5,23,0,0,186,187,3,26,13,0,187,188,5,31,0,0,188,189,5,10,0,0,189,
        192,3,28,14,0,190,193,3,52,26,0,191,193,3,42,21,0,192,190,1,0,0,
        0,192,191,1,0,0,0,193,23,1,0,0,0,194,198,5,17,0,0,195,199,5,39,0,
        0,196,199,3,8,4,0,197,199,3,42,21,0,198,195,1,0,0,0,198,196,1,0,
        0,0,198,197,1,0,0,0,199,200,1,0,0,0,200,201,5,18,0,0,201,202,3,46,
        23,0,202,25,1,0,0,0,203,204,5,38,0,0,204,27,1,0,0,0,205,206,5,38,
        0,0,206,29,1,0,0,0,207,208,5,21,0,0,208,209,5,12,0,0,209,210,7,1,
        0,0,210,211,5,18,0,0,211,212,3,46,23,0,212,213,5,4,0,0,213,218,3,
        40,20,0,214,215,5,2,0,0,215,217,3,40,20,0,216,214,1,0,0,0,217,220,
        1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,221,1,0,0,0,220,218,
        1,0,0,0,221,222,5,5,0,0,222,31,1,0,0,0,223,224,5,15,0,0,224,225,
        5,10,0,0,225,226,3,46,23,0,226,227,5,19,0,0,227,228,5,39,0,0,228,
        33,1,0,0,0,229,230,5,20,0,0,230,231,3,44,22,0,231,232,5,23,0,0,232,
        233,3,48,24,0,233,234,5,18,0,0,234,235,3,46,23,0,235,35,1,0,0,0,
        236,237,5,25,0,0,237,240,7,2,0,0,238,239,5,23,0,0,239,241,3,48,24,
        0,240,238,1,0,0,0,240,241,1,0,0,0,241,242,1,0,0,0,242,243,5,18,0,
        0,243,244,3,46,23,0,244,37,1,0,0,0,245,249,5,39,0,0,246,249,5,40,
        0,0,247,249,3,42,21,0,248,245,1,0,0,0,248,246,1,0,0,0,248,247,1,
        0,0,0,249,39,1,0,0,0,250,251,5,39,0,0,251,252,5,6,0,0,252,253,3,
        38,19,0,253,41,1,0,0,0,254,255,5,7,0,0,255,260,3,52,26,0,256,257,
        5,2,0,0,257,259,3,52,26,0,258,256,1,0,0,0,259,262,1,0,0,0,260,258,
        1,0,0,0,260,261,1,0,0,0,261,263,1,0,0,0,262,260,1,0,0,0,263,264,
        5,8,0,0,264,43,1,0,0,0,265,266,5,39,0,0,266,45,1,0,0,0,267,268,7,
        3,0,0,268,47,1,0,0,0,269,270,7,3,0,0,270,49,1,0,0,0,271,272,5,39,
        0,0,272,51,1,0,0,0,273,278,5,38,0,0,274,275,5,1,0,0,275,276,3,54,
        27,0,276,277,5,3,0,0,277,279,1,0,0,0,278,274,1,0,0,0,278,279,1,0,
        0,0,279,53,1,0,0,0,280,281,5,39,0,0,281,55,1,0,0,0,282,283,5,32,
        0,0,283,57,1,0,0,0,284,285,5,33,0,0,285,286,5,34,0,0,286,59,1,0,
        0,0,287,288,5,33,0,0,288,289,5,28,0,0,289,61,1,0,0,0,290,291,5,33,
        0,0,291,292,5,10,0,0,292,63,1,0,0,0,293,294,5,33,0,0,294,295,5,29,
        0,0,295,296,5,31,0,0,296,297,5,28,0,0,297,65,1,0,0,0,298,299,5,33,
        0,0,299,300,5,29,0,0,300,301,5,31,0,0,301,302,5,10,0,0,302,67,1,
        0,0,0,303,304,5,35,0,0,304,69,1,0,0,0,305,306,5,36,0,0,306,307,5,
        18,0,0,307,308,5,37,0,0,308,309,5,38,0,0,309,71,1,0,0,0,20,75,97,
        103,109,112,116,124,136,145,156,163,172,181,192,198,218,240,248,
        260,278
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
                      "PHASE", "SUMMARY", "TEAM", "PLAYER", "CONTENDER", 
                      "IN", "CLEAR", "LIST", "DATA", "EXIT", "LOAD", "PATH", 
                      "STRING", "WORD", "INTEGER", "WHITESPACE" ]

    RULE_program = 0
    RULE_line = 1
    RULE_create_query = 2
    RULE_specifications = 3
    RULE_attributes = 4
    RULE_add_team = 5
    RULE_add_single_player = 6
    RULE_add_player = 7
    RULE_delete_tournament = 8
    RULE_delete_team = 9
    RULE_delete_single_player = 10
    RULE_delete_player = 11
    RULE_delete_query = 12
    RULE_add_fs = 13
    RULE_add_ss = 14
    RULE_modify_query = 15
    RULE_organize_query = 16
    RULE_report_query = 17
    RULE_show_query = 18
    RULE_dtype = 19
    RULE_pair = 20
    RULE_list = 21
    RULE_a_identifier = 22
    RULE_t_identifier = 23
    RULE_p_identifier = 24
    RULE_identifier = 25
    RULE_name = 26
    RULE_abbr = 27
    RULE_clear = 28
    RULE_list_data = 29
    RULE_list_team = 30
    RULE_list_tournament = 31
    RULE_list_player_team = 32
    RULE_list_single_players = 33
    RULE_exit = 34
    RULE_read_file = 35

    ruleNames =  [ "program", "line", "create_query", "specifications", 
                   "attributes", "add_team", "add_single_player", "add_player", 
                   "delete_tournament", "delete_team", "delete_single_player", 
                   "delete_player", "delete_query", "add_fs", "add_ss", 
                   "modify_query", "organize_query", "report_query", "show_query", 
                   "dtype", "pair", "list", "a_identifier", "t_identifier", 
                   "p_identifier", "identifier", "name", "abbr", "clear", 
                   "list_data", "list_team", "list_tournament", "list_player_team", 
                   "list_single_players", "exit", "read_file" ]

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
    TEAM=28
    PLAYER=29
    CONTENDER=30
    IN=31
    CLEAR=32
    LIST=33
    DATA=34
    EXIT=35
    LOAD=36
    PATH=37
    STRING=38
    WORD=39
    INTEGER=40
    WHITESPACE=41

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
            self.state = 73 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self.line()
                self.state = 75 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 116000989696) != 0):
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


        def add_team(self):
            return self.getTypedRuleContext(TQLParser.Add_teamContext,0)


        def add_single_player(self):
            return self.getTypedRuleContext(TQLParser.Add_single_playerContext,0)


        def add_player(self):
            return self.getTypedRuleContext(TQLParser.Add_playerContext,0)


        def delete_tournament(self):
            return self.getTypedRuleContext(TQLParser.Delete_tournamentContext,0)


        def delete_team(self):
            return self.getTypedRuleContext(TQLParser.Delete_teamContext,0)


        def delete_player(self):
            return self.getTypedRuleContext(TQLParser.Delete_playerContext,0)


        def delete_single_player(self):
            return self.getTypedRuleContext(TQLParser.Delete_single_playerContext,0)


        def modify_query(self):
            return self.getTypedRuleContext(TQLParser.Modify_queryContext,0)


        def organize_query(self):
            return self.getTypedRuleContext(TQLParser.Organize_queryContext,0)


        def report_query(self):
            return self.getTypedRuleContext(TQLParser.Report_queryContext,0)


        def show_query(self):
            return self.getTypedRuleContext(TQLParser.Show_queryContext,0)


        def clear(self):
            return self.getTypedRuleContext(TQLParser.ClearContext,0)


        def list_data(self):
            return self.getTypedRuleContext(TQLParser.List_dataContext,0)


        def exit(self):
            return self.getTypedRuleContext(TQLParser.ExitContext,0)


        def list_tournament(self):
            return self.getTypedRuleContext(TQLParser.List_tournamentContext,0)


        def list_team(self):
            return self.getTypedRuleContext(TQLParser.List_teamContext,0)


        def list_player_team(self):
            return self.getTypedRuleContext(TQLParser.List_player_teamContext,0)


        def list_single_players(self):
            return self.getTypedRuleContext(TQLParser.List_single_playersContext,0)


        def read_file(self):
            return self.getTypedRuleContext(TQLParser.Read_fileContext,0)


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
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.create_query()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.add_team()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self.add_single_player()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 80
                self.add_player()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 81
                self.delete_tournament()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 82
                self.delete_team()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 83
                self.delete_player()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 84
                self.delete_single_player()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 85
                self.modify_query()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 86
                self.organize_query()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 87
                self.report_query()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 88
                self.show_query()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 89
                self.clear()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 90
                self.list_data()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 91
                self.exit()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 92
                self.list_tournament()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 93
                self.list_team()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 94
                self.list_player_team()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 95
                self.list_single_players()
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 96
                self.read_file()
                pass


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
            self.state = 99
            self.match(TQLParser.CREATE)
            self.state = 100
            self.match(TQLParser.TOURNAMENT)
            self.state = 101
            self.name()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 102
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


        def CONTENDER(self):
            return self.getToken(TQLParser.CONTENDER, 0)

        def TEAM(self):
            return self.getToken(TQLParser.TEAM, 0)

        def PLAYER(self):
            return self.getToken(TQLParser.PLAYER, 0)

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
            self.state = 105
            self.attributes()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 106
                self.match(TQLParser.WITH)
                self.state = 107
                self.match(TQLParser.INTEGER)
                self.state = 108
                self.match(TQLParser.PARTICIPANT)


            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 111
                self.list_()


            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 114
                self.match(TQLParser.CONTENDER)
                self.state = 115
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
            self.state = 118
            self.match(TQLParser.T__0)
            self.state = 119
            self.match(TQLParser.WORD)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 120
                self.match(TQLParser.T__1)
                self.state = 121
                self.match(TQLParser.WORD)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self.match(TQLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_teamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(TQLParser.ADD, 0)

        def TEAM(self):
            return self.getToken(TQLParser.TEAM, 0)

        def IN(self):
            return self.getToken(TQLParser.IN, 0)

        def TOURNAMENT(self):
            return self.getToken(TQLParser.TOURNAMENT, 0)

        def add_fs(self):
            return self.getTypedRuleContext(TQLParser.Add_fsContext,0)


        def name(self):
            return self.getTypedRuleContext(TQLParser.NameContext,0)


        def list_(self):
            return self.getTypedRuleContext(TQLParser.ListContext,0)


        def getRuleIndex(self):
            return TQLParser.RULE_add_team

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_team" ):
                listener.enterAdd_team(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_team" ):
                listener.exitAdd_team(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_team" ):
                return visitor.visitAdd_team(self)
            else:
                return visitor.visitChildren(self)




    def add_team(self):

        localctx = TQLParser.Add_teamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_add_team)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(TQLParser.ADD)
            self.state = 130
            self.match(TQLParser.TEAM)
            self.state = 131
            self.match(TQLParser.IN)
            self.state = 132
            self.match(TQLParser.TOURNAMENT)
            self.state = 133
            self.add_fs()
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.state = 134
                self.name()
                pass
            elif token in [7]:
                self.state = 135
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


    class Add_single_playerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(TQLParser.ADD, 0)

        def PLAYER(self):
            return self.getToken(TQLParser.PLAYER, 0)

        def IN(self):
            return self.getToken(TQLParser.IN, 0)

        def TOURNAMENT(self):
            return self.getToken(TQLParser.TOURNAMENT, 0)

        def add_fs(self):
            return self.getTypedRuleContext(TQLParser.Add_fsContext,0)


        def name(self):
            return self.getTypedRuleContext(TQLParser.NameContext,0)


        def list_(self):
            return self.getTypedRuleContext(TQLParser.ListContext,0)


        def getRuleIndex(self):
            return TQLParser.RULE_add_single_player

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_single_player" ):
                listener.enterAdd_single_player(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_single_player" ):
                listener.exitAdd_single_player(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_single_player" ):
                return visitor.visitAdd_single_player(self)
            else:
                return visitor.visitChildren(self)




    def add_single_player(self):

        localctx = TQLParser.Add_single_playerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_add_single_player)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(TQLParser.ADD)
            self.state = 139
            self.match(TQLParser.PLAYER)
            self.state = 140
            self.match(TQLParser.IN)
            self.state = 141
            self.match(TQLParser.TOURNAMENT)
            self.state = 142
            self.add_fs()
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.state = 143
                self.name()
                pass
            elif token in [7]:
                self.state = 144
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


    class Add_playerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(TQLParser.ADD, 0)

        def PLAYER(self):
            return self.getToken(TQLParser.PLAYER, 0)

        def TO(self):
            return self.getToken(TQLParser.TO, 0)

        def add_fs(self):
            return self.getTypedRuleContext(TQLParser.Add_fsContext,0)


        def IN(self):
            return self.getToken(TQLParser.IN, 0)

        def TOURNAMENT(self):
            return self.getToken(TQLParser.TOURNAMENT, 0)

        def add_ss(self):
            return self.getTypedRuleContext(TQLParser.Add_ssContext,0)


        def name(self):
            return self.getTypedRuleContext(TQLParser.NameContext,0)


        def list_(self):
            return self.getTypedRuleContext(TQLParser.ListContext,0)


        def getRuleIndex(self):
            return TQLParser.RULE_add_player

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_player" ):
                listener.enterAdd_player(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_player" ):
                listener.exitAdd_player(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_player" ):
                return visitor.visitAdd_player(self)
            else:
                return visitor.visitChildren(self)




    def add_player(self):

        localctx = TQLParser.Add_playerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_add_player)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(TQLParser.ADD)
            self.state = 148
            self.match(TQLParser.PLAYER)
            self.state = 149
            self.match(TQLParser.TO)
            self.state = 150
            self.add_fs()
            self.state = 151
            self.match(TQLParser.IN)
            self.state = 152
            self.match(TQLParser.TOURNAMENT)
            self.state = 153
            self.add_ss()
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.state = 154
                self.name()
                pass
            elif token in [7]:
                self.state = 155
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


    class Delete_tournamentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(TQLParser.DELETE, 0)

        def TOURNAMENT(self):
            return self.getToken(TQLParser.TOURNAMENT, 0)

        def name(self):
            return self.getTypedRuleContext(TQLParser.NameContext,0)


        def CONTENDER(self):
            return self.getToken(TQLParser.CONTENDER, 0)

        def TEAM(self):
            return self.getToken(TQLParser.TEAM, 0)

        def PLAYER(self):
            return self.getToken(TQLParser.PLAYER, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_delete_tournament

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete_tournament" ):
                listener.enterDelete_tournament(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete_tournament" ):
                listener.exitDelete_tournament(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelete_tournament" ):
                return visitor.visitDelete_tournament(self)
            else:
                return visitor.visitChildren(self)




    def delete_tournament(self):

        localctx = TQLParser.Delete_tournamentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_delete_tournament)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(TQLParser.DELETE)
            self.state = 159
            self.match(TQLParser.TOURNAMENT)
            self.state = 160
            self.name()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 161
                self.match(TQLParser.CONTENDER)
                self.state = 162
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


    class Delete_teamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(TQLParser.DELETE, 0)

        def TEAM(self):
            return self.getToken(TQLParser.TEAM, 0)

        def IN(self):
            return self.getToken(TQLParser.IN, 0)

        def TOURNAMENT(self):
            return self.getToken(TQLParser.TOURNAMENT, 0)

        def add_fs(self):
            return self.getTypedRuleContext(TQLParser.Add_fsContext,0)


        def name(self):
            return self.getTypedRuleContext(TQLParser.NameContext,0)


        def list_(self):
            return self.getTypedRuleContext(TQLParser.ListContext,0)


        def getRuleIndex(self):
            return TQLParser.RULE_delete_team

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete_team" ):
                listener.enterDelete_team(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete_team" ):
                listener.exitDelete_team(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelete_team" ):
                return visitor.visitDelete_team(self)
            else:
                return visitor.visitChildren(self)




    def delete_team(self):

        localctx = TQLParser.Delete_teamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_delete_team)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(TQLParser.DELETE)
            self.state = 166
            self.match(TQLParser.TEAM)
            self.state = 167
            self.match(TQLParser.IN)
            self.state = 168
            self.match(TQLParser.TOURNAMENT)
            self.state = 169
            self.add_fs()
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.state = 170
                self.name()
                pass
            elif token in [7]:
                self.state = 171
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


    class Delete_single_playerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(TQLParser.DELETE, 0)

        def PLAYER(self):
            return self.getToken(TQLParser.PLAYER, 0)

        def IN(self):
            return self.getToken(TQLParser.IN, 0)

        def TOURNAMENT(self):
            return self.getToken(TQLParser.TOURNAMENT, 0)

        def add_fs(self):
            return self.getTypedRuleContext(TQLParser.Add_fsContext,0)


        def name(self):
            return self.getTypedRuleContext(TQLParser.NameContext,0)


        def list_(self):
            return self.getTypedRuleContext(TQLParser.ListContext,0)


        def getRuleIndex(self):
            return TQLParser.RULE_delete_single_player

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete_single_player" ):
                listener.enterDelete_single_player(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete_single_player" ):
                listener.exitDelete_single_player(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelete_single_player" ):
                return visitor.visitDelete_single_player(self)
            else:
                return visitor.visitChildren(self)




    def delete_single_player(self):

        localctx = TQLParser.Delete_single_playerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_delete_single_player)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(TQLParser.DELETE)
            self.state = 175
            self.match(TQLParser.PLAYER)
            self.state = 176
            self.match(TQLParser.IN)
            self.state = 177
            self.match(TQLParser.TOURNAMENT)
            self.state = 178
            self.add_fs()
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.state = 179
                self.name()
                pass
            elif token in [7]:
                self.state = 180
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


    class Delete_playerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(TQLParser.DELETE, 0)

        def PLAYER(self):
            return self.getToken(TQLParser.PLAYER, 0)

        def OF(self):
            return self.getToken(TQLParser.OF, 0)

        def add_fs(self):
            return self.getTypedRuleContext(TQLParser.Add_fsContext,0)


        def IN(self):
            return self.getToken(TQLParser.IN, 0)

        def TOURNAMENT(self):
            return self.getToken(TQLParser.TOURNAMENT, 0)

        def add_ss(self):
            return self.getTypedRuleContext(TQLParser.Add_ssContext,0)


        def name(self):
            return self.getTypedRuleContext(TQLParser.NameContext,0)


        def list_(self):
            return self.getTypedRuleContext(TQLParser.ListContext,0)


        def getRuleIndex(self):
            return TQLParser.RULE_delete_player

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete_player" ):
                listener.enterDelete_player(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete_player" ):
                listener.exitDelete_player(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelete_player" ):
                return visitor.visitDelete_player(self)
            else:
                return visitor.visitChildren(self)




    def delete_player(self):

        localctx = TQLParser.Delete_playerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_delete_player)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(TQLParser.DELETE)
            self.state = 184
            self.match(TQLParser.PLAYER)
            self.state = 185
            self.match(TQLParser.OF)
            self.state = 186
            self.add_fs()
            self.state = 187
            self.match(TQLParser.IN)
            self.state = 188
            self.match(TQLParser.TOURNAMENT)
            self.state = 189
            self.add_ss()
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.state = 190
                self.name()
                pass
            elif token in [7]:
                self.state = 191
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
        self.enterRule(localctx, 24, self.RULE_delete_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(TQLParser.DELETE)
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.state = 195
                self.match(TQLParser.WORD)
                pass
            elif token in [1]:
                self.state = 196
                self.attributes()
                pass
            elif token in [7]:
                self.state = 197
                self.list_()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 200
            self.match(TQLParser.FROM)
            self.state = 201
            self.t_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_fsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TQLParser.STRING, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_add_fs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_fs" ):
                listener.enterAdd_fs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_fs" ):
                listener.exitAdd_fs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_fs" ):
                return visitor.visitAdd_fs(self)
            else:
                return visitor.visitChildren(self)




    def add_fs(self):

        localctx = TQLParser.Add_fsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_add_fs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(TQLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_ssContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TQLParser.STRING, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_add_ss

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_ss" ):
                listener.enterAdd_ss(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_ss" ):
                listener.exitAdd_ss(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_ss" ):
                return visitor.visitAdd_ss(self)
            else:
                return visitor.visitChildren(self)




    def add_ss(self):

        localctx = TQLParser.Add_ssContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_add_ss)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(TQLParser.STRING)
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
        self.enterRule(localctx, 30, self.RULE_modify_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(TQLParser.MODIFY)
            self.state = 208
            self.match(TQLParser.PARTICIPANT)
            self.state = 209
            _la = self._input.LA(1)
            if not(_la==39 or _la==40):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 210
            self.match(TQLParser.FROM)
            self.state = 211
            self.t_identifier()
            self.state = 212
            self.match(TQLParser.T__3)
            self.state = 213
            self.pair()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 214
                self.match(TQLParser.T__1)
                self.state = 215
                self.pair()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 221
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
        self.enterRule(localctx, 32, self.RULE_organize_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(TQLParser.ORGANIZE)
            self.state = 224
            self.match(TQLParser.TOURNAMENT)
            self.state = 225
            self.t_identifier()
            self.state = 226
            self.match(TQLParser.BY)
            self.state = 227
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
        self.enterRule(localctx, 34, self.RULE_report_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(TQLParser.REPORT)
            self.state = 230
            self.a_identifier()
            self.state = 231
            self.match(TQLParser.OF)
            self.state = 232
            self.p_identifier()
            self.state = 233
            self.match(TQLParser.FROM)
            self.state = 234
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
        self.enterRule(localctx, 36, self.RULE_show_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(TQLParser.SHOW)
            self.state = 237
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 238
                self.match(TQLParser.OF)
                self.state = 239
                self.p_identifier()


            self.state = 242
            self.match(TQLParser.FROM)
            self.state = 243
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
        self.enterRule(localctx, 38, self.RULE_dtype)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(TQLParser.WORD)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.match(TQLParser.INTEGER)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 247
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
        self.enterRule(localctx, 40, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(TQLParser.WORD)
            self.state = 251
            self.match(TQLParser.T__5)
            self.state = 252
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
        self.enterRule(localctx, 42, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(TQLParser.T__6)
            self.state = 255
            self.name()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 256
                self.match(TQLParser.T__1)
                self.state = 257
                self.name()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 263
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
        self.enterRule(localctx, 44, self.RULE_a_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
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
        self.enterRule(localctx, 46, self.RULE_t_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
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
        self.enterRule(localctx, 48, self.RULE_p_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
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
        self.enterRule(localctx, 50, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
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
        self.enterRule(localctx, 52, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(TQLParser.STRING)
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 274
                self.match(TQLParser.T__0)
                self.state = 275
                self.abbr()
                self.state = 276
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
        self.enterRule(localctx, 54, self.RULE_abbr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(TQLParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClearContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLEAR(self):
            return self.getToken(TQLParser.CLEAR, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_clear

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClear" ):
                listener.enterClear(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClear" ):
                listener.exitClear(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClear" ):
                return visitor.visitClear(self)
            else:
                return visitor.visitChildren(self)




    def clear(self):

        localctx = TQLParser.ClearContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_clear)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(TQLParser.CLEAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_dataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST(self):
            return self.getToken(TQLParser.LIST, 0)

        def DATA(self):
            return self.getToken(TQLParser.DATA, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_list_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_data" ):
                listener.enterList_data(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_data" ):
                listener.exitList_data(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_data" ):
                return visitor.visitList_data(self)
            else:
                return visitor.visitChildren(self)




    def list_data(self):

        localctx = TQLParser.List_dataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_list_data)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(TQLParser.LIST)
            self.state = 285
            self.match(TQLParser.DATA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_teamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST(self):
            return self.getToken(TQLParser.LIST, 0)

        def TEAM(self):
            return self.getToken(TQLParser.TEAM, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_list_team

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_team" ):
                listener.enterList_team(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_team" ):
                listener.exitList_team(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_team" ):
                return visitor.visitList_team(self)
            else:
                return visitor.visitChildren(self)




    def list_team(self):

        localctx = TQLParser.List_teamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_list_team)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(TQLParser.LIST)
            self.state = 288
            self.match(TQLParser.TEAM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_tournamentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST(self):
            return self.getToken(TQLParser.LIST, 0)

        def TOURNAMENT(self):
            return self.getToken(TQLParser.TOURNAMENT, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_list_tournament

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_tournament" ):
                listener.enterList_tournament(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_tournament" ):
                listener.exitList_tournament(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_tournament" ):
                return visitor.visitList_tournament(self)
            else:
                return visitor.visitChildren(self)




    def list_tournament(self):

        localctx = TQLParser.List_tournamentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_list_tournament)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(TQLParser.LIST)
            self.state = 291
            self.match(TQLParser.TOURNAMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_player_teamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST(self):
            return self.getToken(TQLParser.LIST, 0)

        def PLAYER(self):
            return self.getToken(TQLParser.PLAYER, 0)

        def IN(self):
            return self.getToken(TQLParser.IN, 0)

        def TEAM(self):
            return self.getToken(TQLParser.TEAM, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_list_player_team

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_player_team" ):
                listener.enterList_player_team(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_player_team" ):
                listener.exitList_player_team(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_player_team" ):
                return visitor.visitList_player_team(self)
            else:
                return visitor.visitChildren(self)




    def list_player_team(self):

        localctx = TQLParser.List_player_teamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_list_player_team)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(TQLParser.LIST)
            self.state = 294
            self.match(TQLParser.PLAYER)
            self.state = 295
            self.match(TQLParser.IN)
            self.state = 296
            self.match(TQLParser.TEAM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_single_playersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST(self):
            return self.getToken(TQLParser.LIST, 0)

        def PLAYER(self):
            return self.getToken(TQLParser.PLAYER, 0)

        def IN(self):
            return self.getToken(TQLParser.IN, 0)

        def TOURNAMENT(self):
            return self.getToken(TQLParser.TOURNAMENT, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_list_single_players

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_single_players" ):
                listener.enterList_single_players(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_single_players" ):
                listener.exitList_single_players(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_single_players" ):
                return visitor.visitList_single_players(self)
            else:
                return visitor.visitChildren(self)




    def list_single_players(self):

        localctx = TQLParser.List_single_playersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_list_single_players)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(TQLParser.LIST)
            self.state = 299
            self.match(TQLParser.PLAYER)
            self.state = 300
            self.match(TQLParser.IN)
            self.state = 301
            self.match(TQLParser.TOURNAMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXIT(self):
            return self.getToken(TQLParser.EXIT, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_exit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExit" ):
                listener.enterExit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExit" ):
                listener.exitExit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExit" ):
                return visitor.visitExit(self)
            else:
                return visitor.visitChildren(self)




    def exit(self):

        localctx = TQLParser.ExitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(TQLParser.EXIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_fileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOAD(self):
            return self.getToken(TQLParser.LOAD, 0)

        def FROM(self):
            return self.getToken(TQLParser.FROM, 0)

        def PATH(self):
            return self.getToken(TQLParser.PATH, 0)

        def STRING(self):
            return self.getToken(TQLParser.STRING, 0)

        def getRuleIndex(self):
            return TQLParser.RULE_read_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead_file" ):
                listener.enterRead_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead_file" ):
                listener.exitRead_file(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead_file" ):
                return visitor.visitRead_file(self)
            else:
                return visitor.visitChildren(self)




    def read_file(self):

        localctx = TQLParser.Read_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_read_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(TQLParser.LOAD)
            self.state = 306
            self.match(TQLParser.FROM)
            self.state = 307
            self.match(TQLParser.PATH)
            self.state = 308
            self.match(TQLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





