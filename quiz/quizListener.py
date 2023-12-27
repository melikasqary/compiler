# Generated from C:/Users/melika/PycharmProjects/pythonProject1/quiz/quiz.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .quizParser import quizParser
else:
    from quizParser import quizParser

# This class defines a complete listener for a parse tree produced by quizParser.
class quizListener(ParseTreeListener):

    # Enter a parse tree produced by quizParser#palindrome.
    def enterPalindrome(self, ctx:quizParser.PalindromeContext):
        pass

    # Exit a parse tree produced by quizParser#palindrome.
    def exitPalindrome(self, ctx:quizParser.PalindromeContext):
        pass


    # Enter a parse tree produced by quizParser#entry.
    def enterEntry(self, ctx:quizParser.EntryContext):
        pass

    # Exit a parse tree produced by quizParser#entry.
    def exitEntry(self, ctx:quizParser.EntryContext):
        pass



del quizParser