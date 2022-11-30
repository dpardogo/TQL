# Generated from TQL.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,68,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,
        4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,
        6,46,8,6,1,7,1,7,1,7,4,7,51,8,7,11,7,12,7,52,1,8,4,8,56,8,8,11,8,
        12,8,57,1,9,3,9,61,8,9,1,9,1,9,4,9,65,8,9,11,9,12,9,66,0,0,10,1,
        1,3,2,5,3,7,4,9,0,11,0,13,5,15,6,17,7,19,8,1,0,3,1,0,97,122,1,0,
        65,90,2,0,9,9,32,32,73,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,1,21,1,
        0,0,0,3,23,1,0,0,0,5,25,1,0,0,0,7,27,1,0,0,0,9,29,1,0,0,0,11,31,
        1,0,0,0,13,45,1,0,0,0,15,50,1,0,0,0,17,55,1,0,0,0,19,64,1,0,0,0,
        21,22,5,40,0,0,22,2,1,0,0,0,23,24,5,58,0,0,24,4,1,0,0,0,25,26,5,
        59,0,0,26,6,1,0,0,0,27,28,5,41,0,0,28,8,1,0,0,0,29,30,7,0,0,0,30,
        10,1,0,0,0,31,32,7,1,0,0,32,12,1,0,0,0,33,34,5,67,0,0,34,35,5,82,
        0,0,35,36,5,69,0,0,36,37,5,65,0,0,37,38,5,84,0,0,38,46,5,69,0,0,
        39,40,5,99,0,0,40,41,5,114,0,0,41,42,5,101,0,0,42,43,5,97,0,0,43,
        44,5,116,0,0,44,46,5,101,0,0,45,33,1,0,0,0,45,39,1,0,0,0,46,14,1,
        0,0,0,47,51,3,9,4,0,48,51,3,11,5,0,49,51,5,95,0,0,50,47,1,0,0,0,
        50,48,1,0,0,0,50,49,1,0,0,0,51,52,1,0,0,0,52,50,1,0,0,0,52,53,1,
        0,0,0,53,16,1,0,0,0,54,56,7,2,0,0,55,54,1,0,0,0,56,57,1,0,0,0,57,
        55,1,0,0,0,57,58,1,0,0,0,58,18,1,0,0,0,59,61,5,13,0,0,60,59,1,0,
        0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,65,5,10,0,0,63,65,5,13,0,0,64,
        60,1,0,0,0,64,63,1,0,0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,
        0,67,20,1,0,0,0,8,0,45,50,52,57,60,64,66,0
    ]

class TQLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    CREATE = 5
    WORD = 6
    WHITESPACE = 7
    NEWLINE = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "':'", "';'", "')'" ]

    symbolicNames = [ "<INVALID>",
            "CREATE", "WORD", "WHITESPACE", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "LOWERCASE", "UPPERCASE", 
                  "CREATE", "WORD", "WHITESPACE", "NEWLINE" ]

    grammarFileName = "TQL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

