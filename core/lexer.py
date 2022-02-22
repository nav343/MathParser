from sly import Lexer

class MyLexer(Lexer):
    tokens = { NAME, NUMBER }
    ignore = ' \t'
    literals = { '=', '+', '-', '*', '/', '(', ')'  }
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1