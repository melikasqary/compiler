import re
from antlr4 import FileStream
from hw3Lexer import hw3Lexer 


def national_code_check(code):
    code = str(code)
    if not 8 <= len(code) <= 10 or not code.isnumeric():
        return False

    code = '0' * (10 - len(code)) + code
    total = 0
    control_digit = int(code[-1])

    for digit, index in zip(code, range(10, 1, -1)):
        total += int(digit) * index

    reminder = total % 11

    valid = (reminder < 2 and reminder == control_digit) or (11 - reminder == control_digit)

    if valid:
        print(code)
    return valid


def validate_postal_code(postal_code):
    pattern = r'\b(?!(\d)\1{3})[13-9]{4}[1346-9][013-9]{5}\b'
    return bool(re.fullmatch(pattern, postal_code))


def main():
    input_file = "input.txt"
    input_stream = FileStream(input_file)
    lexer = hw3Lexer (input_stream)

    for token in lexer.getAllTokens():
        if (token.type == 6):
            if national_code_check(token.text):
                continue

            national_code_check(token.text)

            if validate_postal_code(token.text):
                print(token.text)

        elif (token.type == 7):
            print(token.text)

        elif (token.type == 8):
            try:
                float(token.text.replace(".", ""))
                print(token.text)
            except:
                print(token.text)


if __name__ == "__main__":

    main()