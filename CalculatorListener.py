# Generated from Calculator.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete listener for a parse tree produced by CalculatorParser.
class CalculatorListener(ParseTreeListener):

    # Enter a parse tree produced by CalculatorParser#calc.
    def enterCalc(self, ctx:CalculatorParser.CalcContext):
        pass

    # Exit a parse tree produced by CalculatorParser#calc.
    def exitCalc(self, ctx:CalculatorParser.CalcContext):
        pass


    # Enter a parse tree produced by CalculatorParser#number.
    def enterNumber(self, ctx:CalculatorParser.NumberContext):
        pass

    # Exit a parse tree produced by CalculatorParser#number.
    def exitNumber(self, ctx:CalculatorParser.NumberContext):
        pass


    # Enter a parse tree produced by CalculatorParser#infixExpr.
    def enterInfixExpr(self, ctx:CalculatorParser.InfixExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#infixExpr.
    def exitInfixExpr(self, ctx:CalculatorParser.InfixExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#plusOrMinusExpr.
    def enterPlusOrMinusExpr(self, ctx:CalculatorParser.PlusOrMinusExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#plusOrMinusExpr.
    def exitPlusOrMinusExpr(self, ctx:CalculatorParser.PlusOrMinusExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#parensExpr.
    def enterParensExpr(self, ctx:CalculatorParser.ParensExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#parensExpr.
    def exitParensExpr(self, ctx:CalculatorParser.ParensExprContext):
        pass



del CalculatorParser