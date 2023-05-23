# Generated from Calculator.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete generic visitor for a parse tree produced by CalculatorParser.

class CalculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculatorParser#calc.
    def visitCalc(self, ctx:CalculatorParser.CalcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#number.
    def visitNumber(self, ctx:CalculatorParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#infixExpr.
    def visitInfixExpr(self, ctx:CalculatorParser.InfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#plusOrMinusExpr.
    def visitPlusOrMinusExpr(self, ctx:CalculatorParser.PlusOrMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#parensExpr.
    def visitParensExpr(self, ctx:CalculatorParser.ParensExprContext):
        return self.visitChildren(ctx)



del CalculatorParser