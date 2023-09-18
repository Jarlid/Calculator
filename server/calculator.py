import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)


class CalculatorException(Exception):
    pass


def create_lexer():
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    @lex.TOKEN(r'\d*\.\d*')
    def t_FLOAT(t):
        try:
            t.value = float(t.value)
            return t
        except ValueError:
            raise CalculatorException(f"'.' can't stand alone.")

    @lex.TOKEN(r'\d+')
    def t_NUMBER(t):
        t.value = int(t.value)
        return t

    t_ignore = ' \t\n'

    def t_error(t):
        raise CalculatorException(f"Illegal character '{t.value[0]}'.")

    return lex.lex()


class Calculator:
    def __init__(self, lexer=None):
        def p_expression_plus(p):
            """expression : expression PLUS term"""
            p[0] = p[1] + p[3]

        def p_expression_minus(p):
            """expression : expression MINUS term"""
            p[0] = p[1] - p[3]

        def p_expression_unary_minus(p):
            """expression : MINUS term"""
            p[0] = -p[2]

        def p_expression_term(p):
            """expression : term"""
            p[0] = p[1]

        def p_term_times(p):
            """term : term TIMES factor"""
            p[0] = p[1] * p[3]

        def p_term_div(p):
            """term : term DIVIDE factor"""
            p[0] = p[1] / p[3]

        def p_term_factor(p):
            """term : factor"""
            p[0] = p[1]

        def p_factor_num(p):
            """factor : NUMBER
                      | FLOAT"""
            p[0] = p[1]

        def p_factor_expr(p):
            """factor : LPAREN expression RPAREN"""
            p[0] = p[2]

        def p_error(p):
            raise CalculatorException("Syntax error in input.")

        self.parser = yacc.yacc()
        self.lexer = lexer if lexer is not None else create_lexer()

    def calculate(self, in_str: str) -> int:
        return self.parser.parse(input=in_str, lexer=self.lexer)
