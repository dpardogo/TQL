import sys
from antlr4 import *

from dist.TQLParser import TQLParser

from dist.TQLListener import TQLListener
from dist.TQLVisitor import TQLVisitor

class visitor(TQLVisitor):
    def __init__(self,output):
        self.output=output
        
    def visitLine(self, ctx: TQLParser.LineContext):
        self.output.write("esto es una linea\n")
        return super().visitLine(ctx)

    def visitCreate_query(self, ctx: TQLParser.Create_queryContext):
        self.output.write("esto es una creación\n")
        print(ctx.name)
        return super().visitCreate_query(ctx)