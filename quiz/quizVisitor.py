# Generated from C:/Users/melika/PycharmProjects/pythonProject1/quiz/quiz.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .quizParser import quizParser
else:
    from quizParser import quizParser

# This class defines a complete generic visitor for a parse tree produced by quizParser.

class quizVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by quizParser#palindrome.
    def visitPalindrome(self, ctx:quizParser.PalindromeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by quizParser#entry.
    def visitEntry(self, ctx:quizParser.EntryContext):
        return self.visitChildren(ctx)



del quizParser