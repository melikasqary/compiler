# Generated from C:/Users/melika/PycharmProjects/pythonProject1/quiz/quiz.g4 by ANTLR 4.13.1
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
        4,1,11,61,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,59,8,1,1,1,
        0,0,2,0,2,0,0,78,0,4,1,0,0,0,2,58,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,
        1,6,1,1,0,0,0,7,8,5,1,0,0,8,9,3,2,1,0,9,10,5,1,0,0,10,59,1,0,0,0,
        11,12,5,2,0,0,12,13,3,2,1,0,13,14,5,2,0,0,14,59,1,0,0,0,15,16,5,
        3,0,0,16,17,3,2,1,0,17,18,5,3,0,0,18,59,1,0,0,0,19,20,5,4,0,0,20,
        21,3,2,1,0,21,22,5,4,0,0,22,59,1,0,0,0,23,24,5,5,0,0,24,25,3,2,1,
        0,25,26,5,5,0,0,26,59,1,0,0,0,27,28,5,6,0,0,28,29,3,2,1,0,29,30,
        5,6,0,0,30,59,1,0,0,0,31,32,5,7,0,0,32,33,3,2,1,0,33,34,5,7,0,0,
        34,59,1,0,0,0,35,36,5,8,0,0,36,37,3,2,1,0,37,38,5,8,0,0,38,59,1,
        0,0,0,39,40,5,9,0,0,40,41,3,2,1,0,41,42,5,9,0,0,42,59,1,0,0,0,43,
        44,5,10,0,0,44,45,3,2,1,0,45,46,5,10,0,0,46,59,1,0,0,0,47,59,5,1,
        0,0,48,59,5,2,0,0,49,59,5,3,0,0,50,59,5,4,0,0,51,59,5,5,0,0,52,59,
        5,6,0,0,53,59,5,7,0,0,54,59,5,8,0,0,55,59,5,9,0,0,56,59,5,10,0,0,
        57,59,1,0,0,0,58,7,1,0,0,0,58,11,1,0,0,0,58,15,1,0,0,0,58,19,1,0,
        0,0,58,23,1,0,0,0,58,27,1,0,0,0,58,31,1,0,0,0,58,35,1,0,0,0,58,39,
        1,0,0,0,58,43,1,0,0,0,58,47,1,0,0,0,58,48,1,0,0,0,58,49,1,0,0,0,
        58,50,1,0,0,0,58,51,1,0,0,0,58,52,1,0,0,0,58,53,1,0,0,0,58,54,1,
        0,0,0,58,55,1,0,0,0,58,56,1,0,0,0,58,57,1,0,0,0,59,3,1,0,0,0,1,58
    ]

class quizParser ( Parser ):

    grammarFileName = "quiz.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'1'", "'2'", "'3'", "'4'", "'5'", "'6'", 
                     "'7'", "'8'", "'9'", "'0'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS" ]

    RULE_palindrome = 0
    RULE_entry = 1

    ruleNames =  [ "palindrome", "entry" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PalindromeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entry(self):
            return self.getTypedRuleContext(quizParser.EntryContext,0)


        def EOF(self):
            return self.getToken(quizParser.EOF, 0)

        def getRuleIndex(self):
            return quizParser.RULE_palindrome

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPalindrome" ):
                listener.enterPalindrome(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPalindrome" ):
                listener.exitPalindrome(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPalindrome" ):
                return visitor.visitPalindrome(self)
            else:
                return visitor.visitChildren(self)




    def palindrome(self):

        localctx = quizParser.PalindromeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_palindrome)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.entry()
            self.state = 5
            self.match(quizParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entry(self):
            return self.getTypedRuleContext(quizParser.EntryContext,0)


        def getRuleIndex(self):
            return quizParser.RULE_entry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntry" ):
                listener.enterEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntry" ):
                listener.exitEntry(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntry" ):
                return visitor.visitEntry(self)
            else:
                return visitor.visitChildren(self)




    def entry(self):

        localctx = quizParser.EntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_entry)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 7
                self.match(quizParser.T__0)
                self.state = 8
                self.entry()
                self.state = 9
                self.match(quizParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.match(quizParser.T__1)
                self.state = 12
                self.entry()
                self.state = 13
                self.match(quizParser.T__1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 15
                self.match(quizParser.T__2)
                self.state = 16
                self.entry()
                self.state = 17
                self.match(quizParser.T__2)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 19
                self.match(quizParser.T__3)
                self.state = 20
                self.entry()
                self.state = 21
                self.match(quizParser.T__3)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 23
                self.match(quizParser.T__4)
                self.state = 24
                self.entry()
                self.state = 25
                self.match(quizParser.T__4)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 27
                self.match(quizParser.T__5)
                self.state = 28
                self.entry()
                self.state = 29
                self.match(quizParser.T__5)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 31
                self.match(quizParser.T__6)
                self.state = 32
                self.entry()
                self.state = 33
                self.match(quizParser.T__6)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 35
                self.match(quizParser.T__7)
                self.state = 36
                self.entry()
                self.state = 37
                self.match(quizParser.T__7)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 39
                self.match(quizParser.T__8)
                self.state = 40
                self.entry()
                self.state = 41
                self.match(quizParser.T__8)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 43
                self.match(quizParser.T__9)
                self.state = 44
                self.entry()
                self.state = 45
                self.match(quizParser.T__9)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 47
                self.match(quizParser.T__0)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 48
                self.match(quizParser.T__1)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 49
                self.match(quizParser.T__2)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 50
                self.match(quizParser.T__3)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 51
                self.match(quizParser.T__4)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 52
                self.match(quizParser.T__5)
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 53
                self.match(quizParser.T__6)
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 54
                self.match(quizParser.T__7)
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 55
                self.match(quizParser.T__8)
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 56
                self.match(quizParser.T__9)
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





