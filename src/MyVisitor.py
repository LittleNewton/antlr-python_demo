from antlr4 import *
from CalculatorLexer import CalculatorLexer
from CalculatorParser import CalculatorParser
from CalculatorVisitor import CalculatorVisitor


class EvalVisitor(CalculatorVisitor):
    def visitNumber(self, ctx: CalculatorParser.NumberContext):
        return int(ctx.NUM().getText())

    def visitPlusOrMinusExpr(self, ctx: CalculatorParser.PlusOrMinusExprContext):
        value = self.visit(ctx.expr())
        if ctx.PLUS():
            return value
        else:
            return -value

    def visitParensExpr(self, ctx: CalculatorParser.ParensExprContext):
        return self.visit(ctx.expr())

    def visitInfixExpr(self, ctx: CalculatorParser.InfixExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        operator = ctx.op.text

        if operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        elif operator == '+':
            return left + right
        elif operator == '-':
            return left - right

        return 0


def evaluate(expression):
    lexer = CalculatorLexer(InputStream(expression))
    tokens = CommonTokenStream(lexer)
    parser = CalculatorParser(tokens)
    tree = parser.calc()

    visitor = EvalVisitor()
    result = visitor.visit(tree)
    return result


def main():
    print("Calculator Program")
    print("Enter 'q' to quit")

    while True:
        expression = input("Enter an arithmetic expression: ")
        if expression == "q":
            break

        try:
            result = evaluate(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    main()
