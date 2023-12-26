# Generated from C:/Users/melika/PycharmProjects/pythonProject1/hw2/Arithmetic.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ArithmeticParser import ArithmeticParser
else:
    from ArithmeticParser import ArithmeticParser

# This class defines a complete listener for a parse tree produced by ArithmeticParser.
class ArithmeticListener(ParseTreeListener):

    # Enter a parse tree produced by ArithmeticParser#expression.
    def enterExpression(self, ctx:ArithmeticParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#expression.
    def exitExpression(self, ctx:ArithmeticParser.ExpressionContext):
        pass



del ArithmeticParser