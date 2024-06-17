# Generated from ir/smelly.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .smellyParser import smellyParser
else:
    from smellyParser import smellyParser

# This class defines a complete generic visitor for a parse tree produced by smellyParser.

class smellyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by smellyParser#parse.
    def visitParse(self, ctx:smellyParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#type.
    def visitType(self, ctx:smellyParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#stmt.
    def visitStmt(self, ctx:smellyParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#bodyStmts.
    def visitBodyStmts(self, ctx:smellyParser.BodyStmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#body.
    def visitBody(self, ctx:smellyParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#ifStmt.
    def visitIfStmt(self, ctx:smellyParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#elseifStmt.
    def visitElseifStmt(self, ctx:smellyParser.ElseifStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#elseStmt.
    def visitElseStmt(self, ctx:smellyParser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#whileStmt.
    def visitWhileStmt(self, ctx:smellyParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#funcAssign.
    def visitFuncAssign(self, ctx:smellyParser.FuncAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#varAssign.
    def visitVarAssign(self, ctx:smellyParser.VarAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#arg.
    def visitArg(self, ctx:smellyParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#args.
    def visitArgs(self, ctx:smellyParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#param.
    def visitParam(self, ctx:smellyParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#params.
    def visitParams(self, ctx:smellyParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#call.
    def visitCall(self, ctx:smellyParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#atom.
    def visitAtom(self, ctx:smellyParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by smellyParser#expr.
    def visitExpr(self, ctx:smellyParser.ExprContext):
        return self.visitChildren(ctx)



del smellyParser