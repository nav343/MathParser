from core.lexer import MyLexer
from core.parser import MyParser

if __name__ == '__main__':
    lexer = MyLexer()
    parser = MyParser()

    while True:
        try:
            data = input('>> ')
        except EOFError:
            break
        if data:
            parser.parse(lexer.tokenize(data))