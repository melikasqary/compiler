# Generated from C:/Users/melika/PycharmProjects/pythonProject1/hw3/hw3.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .hw3Parser import hw3Parser
else:
    from hw3Parser import hw3Parser

# This class defines a complete listener for a parse tree produced by hw3Parser.
class hw3Listener(ParseTreeListener):

    # Enter a parse tree produced by hw3Parser#emails.
    def enterEmails(self, ctx:hw3Parser.EmailsContext):
        pass

    # Exit a parse tree produced by hw3Parser#emails.
    def exitEmails(self, ctx:hw3Parser.EmailsContext):
        pass


    # Enter a parse tree produced by hw3Parser#email.
    def enterEmail(self, ctx:hw3Parser.EmailContext):
        pass

    # Exit a parse tree produced by hw3Parser#email.
    def exitEmail(self, ctx:hw3Parser.EmailContext):
        pass


    # Enter a parse tree produced by hw3Parser#melli_number.
    def enterMelli_number(self, ctx:hw3Parser.Melli_numberContext):
        pass

    # Exit a parse tree produced by hw3Parser#melli_number.
    def exitMelli_number(self, ctx:hw3Parser.Melli_numberContext):
        pass


    # Enter a parse tree produced by hw3Parser#url.
    def enterUrl(self, ctx:hw3Parser.UrlContext):
        pass

    # Exit a parse tree produced by hw3Parser#url.
    def exitUrl(self, ctx:hw3Parser.UrlContext):
        pass



del hw3Parser