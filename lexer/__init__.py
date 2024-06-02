from ply import lex

from lexer.exceptions import IllegalCharacterError

__all__ = ["tokens", "lexer"]

tokens = (
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LPAREN",
    "RPAREN",
)

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"

t_ignore = " \t"


def t_NUMBER(t):
    r"\d+\|\d+"
    t.value = t.value
    return t


def t_error(t):
    raise IllegalCharacterError(t.value[0])


lexer = lex.lex()
