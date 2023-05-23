import sys
from antlr4 import *
from CalculatorLexer import CalculatorLexer
from CalculatorParser import CalculatorParser


def main(argv):

    in_stream = InputStream("-9*(-1+7)/2")

    # if len(sys.argv) > 1:
    #     in_stream = FileStream(sys.argv[1])
    # else:
    #     in_stream = InputStream(sys.stdin.readline())

    lexer = CalculatorLexer(in_stream)
    tokens = CommonTokenStream(lexer)
    parser = CalculatorParser(tokens)
    tree = parser.calc()
    print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    main(sys.argv)
