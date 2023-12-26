# import pip
# pip.main(['install','antlr4-python3-runtime'])

from antlr4 import *
from ArithmeticLexer import ArithmeticLexer
from ArithmeticParser import ArithmeticParser

# Create an input stream from your arithmetic expression
arithmetic_expression = "(4 + 2) * 3 / 5"
input_stream = InputStream(arithmetic_expression)

# Create a lexer that feeds off the input stream
lexer = ArithmeticLexer(input_stream)
token_stream = CommonTokenStream(lexer)

# Create a parser that feeds off the token stream
parser = ArithmeticParser(token_stream)

# Start parsing from the 'expression' rule
arithmetic_tree = parser.expression()

# Print the parse tree for debugging
print(arithmetic_tree.toStringTree(recog=parser))

# You can now traverse the parse tree and perform any further processing or evaluation that you need
# For example, you can write a visitor pattern to evaluate the arithmetic expression
