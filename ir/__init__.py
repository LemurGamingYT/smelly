from pathlib import Path

from antlr4 import CommonTokenStream, InputStream

from ir.parser.smellyVisitor import smellyVisitor
from ir.parser.smellyParser import smellyParser
from ir.parser.smellyLexer import smellyLexer
from c_ast import *


class IRBuilder(smellyVisitor):
    def build(self, file: Path) -> Program:
        tokens = CommonTokenStream(smellyLexer(InputStream(file.read_text('utf-8'))))
        tree = smellyParser(tokens).parse()
        return self.visitParse(tree)
    
    @staticmethod
    def pos(ctx) -> Position:
        if hasattr(ctx, 'line') and hasattr(ctx, 'column'):
            return Position(ctx.line, ctx.column)
        elif hasattr(ctx, 'start'):
            return Position(ctx.start.line, ctx.start.column)
        elif hasattr(ctx, 'symbol'):
            return Position(ctx.symbol.line, ctx.symbol.column)
    
    
    def visitParse(self, ctx: smellyParser.ParseContext) -> Program:
        stmts = []
        for stmt in ctx.stmt():
            stmts.append(self.visitStmt(stmt))
        
        return Program(Position(0, 0), stmts)
    
    def visitType(self, ctx: smellyParser.TypeContext) -> str:
        return ctx.getText()
    
    def visitArg(self, ctx: smellyParser.ArgContext) -> Arg:
        return Arg(self.pos(ctx), self.visitExpr(ctx.expr()))
    
    def visitArgs(self, ctx: smellyParser.ArgsContext) -> list[Arg]:
        return [self.visitArg(arg) for arg in ctx.arg()]
    
    def visitParam(self, ctx: smellyParser.ParamContext) -> Param:
        return Param(self.pos(ctx), ctx.ID().getText(), self.visitType(ctx.type_()))
    
    def visitParams(self, ctx: smellyParser.ParamsContext) -> list[Param]:
        return [self.visitParam(param) for param in ctx.param()]
    
    def visitBodyStmts(self, ctx: smellyParser.BodyStmtsContext) -> Node:
        if ctx.RETURN() is not None:
            expr = self.visitExpr(ctx.expr())
            return Return(self.pos(ctx), expr)
        elif ctx.stmt() is not None:
            return self.visitStmt(ctx.stmt())
        elif ctx.BREAK() is not None:
            return Break(self.pos(ctx))
        elif ctx.CONTINUE() is not None:
            return Continue(self.pos(ctx))
    
    def visitBody(self, ctx: smellyParser.BodyContext) -> list[Node]:
        return [self.visitBodyStmts(stmt) for stmt in ctx.bodyStmts()]
    
    def visitIfStmt(self, ctx: smellyParser.IfStmtContext) -> If:
        elseifs = {}
        for elseif in ctx.elseifStmt():
            expr, body = self.visitElseifStmt(elseif)
            elseifs[expr] = body
        
        return If(
            self.pos(ctx),
            self.visitExpr(ctx.expr()),
            self.visitBody(ctx.body()),
            self.visitElseStmt(ctx.elseStmt()) if ctx.elseStmt() is not None else None,
            elseifs
        )
    
    def visitElseStmt(self, ctx: smellyParser.ElseStmtContext) -> list[Node]:
        return self.visitBody(ctx.body())
    
    def visitElseifStmt(self, ctx: smellyParser.ElseifStmtContext) -> tuple[Node, list[Node]]:
        return self.visitExpr(ctx.expr()), self.visitBody(ctx.body())
    
    def visitWhileStmt(self, ctx: smellyParser.WhileStmtContext) -> While:
        return While(self.pos(ctx), self.visitExpr(ctx.expr()), self.visitBody(ctx.body()))
    
    def visitVarAssign(self, ctx: smellyParser.VarAssignContext) -> Variable:
        expr = self.visitExpr(ctx.expr())
        type_ = self.visitType(ctx.type_()) if ctx.type_() is not None else None
        
        op = None
        if ctx.ADD() is not None:
            op = '+'
        elif ctx.SUB() is not None:
            op = '-'
        elif ctx.MUL() is not None:
            op = '*'
        elif ctx.DIV() is not None:
            op = '/'
        elif ctx.MOD() is not None:
            op = '%'
        
        return Variable(self.pos(ctx), ctx.ID().getText(), expr, type_, op)
    
    def visitFuncAssign(self, ctx: smellyParser.FuncAssignContext) -> Func:
        return Func(
            self.pos(ctx),
            ctx.ID().getText(),
            self.visitType(ctx.type_()),
            self.visitParams(ctx.params()) if ctx.params() is not None else [],
            self.visitBody(ctx.body())
        )
    
    def visitCall(self, ctx: smellyParser.CallContext) -> Call:
        return Call(
            self.pos(ctx),
            ctx.ID().getText(),
            self.visitArgs(ctx.args()) if ctx.args() is not None else []
        )
    
    def visitAtom(self, ctx: smellyParser.AtomContext) -> Node:
        if ctx.INT() is not None:
            return Constant(self.pos(ctx), ctx.getText(), 'int')
        elif ctx.FLOAT() is not None:
            return Constant(self.pos(ctx), ctx.getText(), 'float')
        elif ctx.STRING() is not None:
            return Constant(self.pos(ctx), ctx.getText(), 'string')
        elif ctx.BOOL() is not None:
            return Constant(self.pos(ctx), ctx.getText(), 'bool')
        elif ctx.NIL() is not None:
            return Constant(self.pos(ctx), ctx.getText(), 'nil')
        elif ctx.ID() is not None:
            return Identifier(self.pos(ctx), ctx.getText())
        elif ctx.LPAREN() is not None:
            return Brackets(self.pos(ctx), self.visitExpr(ctx.expr()))
    
    def visitExpr(self, ctx: smellyParser.ExprContext) -> Node:
        if ctx.atom() is not None:
            return self.visitAtom(ctx.atom())
        elif ctx.call() is not None:
            return self.visitCall(ctx.call())
        elif ctx.DOT() is not None:
            args = []
            if ctx.args() is not None:
                args = self.visitArgs(ctx.args())
            return Attribute(
                self.pos(ctx),
                self.visitExpr(ctx.expr(0)),
                ctx.ID().getText(),
                args if ctx.LPAREN() is not None else None
            )
        elif ctx.op is not None:
            op = ctx.op.text
            left = self.visitExpr(ctx.expr(0))
            right = self.visitExpr(ctx.expr(1))
            return Operation(self.pos(ctx.op), left, op, right)
        elif ctx.uop is not None:
            op = ctx.uop.text
            expr = self.visitExpr(ctx.expr(0))
            return UnaryOperation(self.pos(ctx.uop), op, expr)
        elif ctx.IF() is not None:
            return Ternary(
                self.pos(ctx),
                self.visitExpr(ctx.expr(1)),
                self.visitExpr(ctx.expr(0)),
                self.visitExpr(ctx.expr(2))
            )
