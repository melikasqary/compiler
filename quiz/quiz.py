from antlr4 import *
from quizLexer import quizLexer
from quizParser import quizParser


def check_palindrome(input_string):
    # Create an input stream of characters from the input string
    input_stream = InputStream(input_string)

    # Create a lexer that reads from the input stream
    lexer = quizLexer(input_stream)

    # Create a stream of tokens from the lexer
    token_stream = CommonTokenStream(lexer)

    # Create a parser that reads from the token stream
    parser = quizParser(token_stream)

    # Invoke the starting rule called "palindrome"
    tree = parser.palindrome()

    # Return whether the input is a palindrome or not
    return parser.getNumberOfSyntaxErrors() == 0


# Example usage:
input_string = "1221"
is_palindrome = check_palindrome(input_string)
print(f"Is '{input_string}' a palindrome? {is_palindrome}")