import sys
from antlr4 import *
from dist.TQLLexer import TQLLexer
from dist.TQLParser import TQLParser
from visitor import visitor


def main(argv):
    input = FileStream(argv[1])

    lexer = TQLLexer(input)
    stream = CommonTokenStream(lexer)
    parser = TQLParser(stream)
    tree = parser.program()
    output = open("output.txt","w")
    
    obj=visitor(output)
    obj.visit(tree)
        
    output.close()      
if __name__ == '__main__':
    main(sys.argv)