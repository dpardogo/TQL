import sys
from antlr4 import *
from dist.TQLLexer import TQLLexer
from dist.TQLParser import TQLParser
from dist.TQLListener import TQLListener
from visitor import visitor



def main(argv):
    
    print("TQL V0.2.0")
    while True:
        inputstr = input("TQL> ")

        lexer = TQLLexer(InputStream(inputstr))
        stream = CommonTokenStream(lexer)
        parser = TQLParser(stream)
        tree = parser.program()

        obj=visitor()
        obj.visit(tree)
if __name__ == '__main__':
    main(sys.argv)