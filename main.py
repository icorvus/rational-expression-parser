import sys

from lexer import lexer
from lexer.exceptions import IllegalCharacterError
from parser_ import parser
from parser_.exceptions import ParsingError


def main():
    correct_statements = 0

    while True:
        user_input = input()
        try:
            result = parser.parse(user_input, lexer=lexer)
        except (IllegalCharacterError, ParsingError, ZeroDivisionError):
            print(
                "Invalid expression, number of correctly evaluated expressions: "
                f"{correct_statements}"
            )
            sys.exit()
        else:
            print(f"{result.numerator}|{result.denominator}")
            correct_statements += 1


if __name__ == "__main__":
    main()
