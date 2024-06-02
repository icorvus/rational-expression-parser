from fractions import Fraction

from ply import yacc

from lexer import tokens  # noqa: F401
from parser_.exceptions import ParsingError


def parse_fraction(value):
    numerator, denominator = map(int, value.split("|"))
    return Fraction(numerator, denominator)


# Definicja reguł gramatyki
def p_expression_plus(p):
    "expression : expression PLUS term"
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    "expression : expression MINUS term"
    p[0] = p[1] - p[3]


def p_expression_term(p):
    "expression : term"
    p[0] = p[1]


def p_term_times(p):
    "term : term TIMES factor"
    p[0] = p[1] * p[3]


def p_term_divide(p):
    "term : term DIVIDE factor"
    p[0] = p[1] / p[3]


def p_term_factor(p):
    "term : factor"
    p[0] = p[1]


def p_factor_negative_number(p):
    "factor : MINUS NUMBER"
    p[0] = -parse_fraction(p[2])


def p_factor_number(p):
    "factor : NUMBER"
    p[0] = parse_fraction(p[1])


def p_factor_expr(p):
    "factor : LPAREN expression RPAREN"
    p[0] = p[2]


def p_error(p):
    raise ParsingError(p)


parser = yacc.yacc()
