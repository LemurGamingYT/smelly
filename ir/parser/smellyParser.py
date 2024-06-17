# Generated from ir/smelly.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,206,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,0,
        41,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,52,8,2,1,3,1,3,1,
        3,1,3,1,3,3,3,59,8,3,1,4,1,4,5,4,63,8,4,10,4,12,4,66,9,4,1,4,1,4,
        1,5,1,5,1,5,1,5,5,5,74,8,5,10,5,12,5,77,9,5,1,5,3,5,80,8,5,1,6,1,
        6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,98,
        8,9,1,9,1,9,1,9,3,9,103,8,9,1,9,1,9,1,10,3,10,108,8,10,1,10,1,10,
        3,10,112,8,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,5,12,122,8,
        12,10,12,12,12,125,9,12,1,13,1,13,1,13,1,14,1,14,1,14,5,14,133,8,
        14,10,14,12,14,136,9,14,1,15,1,15,1,15,3,15,141,8,15,1,15,1,15,1,
        16,1,16,1,16,3,16,148,8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,3,16,162,8,16,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,3,17,171,8,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,3,17,196,8,17,1,17,3,17,199,8,17,5,17,201,8,17,10,17,12,
        17,204,9,17,1,17,0,1,34,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,0,5,1,0,15,19,1,0,15,16,1,0,17,19,1,0,20,25,1,0,26,27,
        224,0,39,1,0,0,0,2,44,1,0,0,0,4,51,1,0,0,0,6,58,1,0,0,0,8,60,1,0,
        0,0,10,69,1,0,0,0,12,81,1,0,0,0,14,86,1,0,0,0,16,89,1,0,0,0,18,93,
        1,0,0,0,20,107,1,0,0,0,22,116,1,0,0,0,24,118,1,0,0,0,26,126,1,0,
        0,0,28,129,1,0,0,0,30,137,1,0,0,0,32,161,1,0,0,0,34,170,1,0,0,0,
        36,38,3,4,2,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,
        0,0,0,40,42,1,0,0,0,41,39,1,0,0,0,42,43,5,0,0,1,43,1,1,0,0,0,44,
        45,5,14,0,0,45,3,1,0,0,0,46,52,3,18,9,0,47,52,3,16,8,0,48,52,3,10,
        5,0,49,52,3,20,10,0,50,52,3,34,17,0,51,46,1,0,0,0,51,47,1,0,0,0,
        51,48,1,0,0,0,51,49,1,0,0,0,51,50,1,0,0,0,52,5,1,0,0,0,53,59,3,4,
        2,0,54,55,5,6,0,0,55,59,3,34,17,0,56,59,5,7,0,0,57,59,5,5,0,0,58,
        53,1,0,0,0,58,54,1,0,0,0,58,56,1,0,0,0,58,57,1,0,0,0,59,7,1,0,0,
        0,60,64,5,34,0,0,61,63,3,6,3,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,
        1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,64,1,0,0,0,67,68,5,35,0,0,
        68,9,1,0,0,0,69,70,5,1,0,0,70,71,3,34,17,0,71,75,3,8,4,0,72,74,3,
        12,6,0,73,72,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,
        79,1,0,0,0,77,75,1,0,0,0,78,80,3,14,7,0,79,78,1,0,0,0,79,80,1,0,
        0,0,80,11,1,0,0,0,81,82,5,2,0,0,82,83,5,1,0,0,83,84,3,34,17,0,84,
        85,3,8,4,0,85,13,1,0,0,0,86,87,5,2,0,0,87,88,3,8,4,0,88,15,1,0,0,
        0,89,90,5,4,0,0,90,91,3,34,17,0,91,92,3,8,4,0,92,17,1,0,0,0,93,94,
        5,3,0,0,94,95,5,14,0,0,95,97,5,32,0,0,96,98,3,28,14,0,97,96,1,0,
        0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,102,5,33,0,0,100,101,5,36,0,0,
        101,103,3,2,1,0,102,100,1,0,0,0,102,103,1,0,0,0,103,104,1,0,0,0,
        104,105,3,8,4,0,105,19,1,0,0,0,106,108,3,2,1,0,107,106,1,0,0,0,107,
        108,1,0,0,0,108,109,1,0,0,0,109,111,5,14,0,0,110,112,7,0,0,0,111,
        110,1,0,0,0,111,112,1,0,0,0,112,113,1,0,0,0,113,114,5,31,0,0,114,
        115,3,34,17,0,115,21,1,0,0,0,116,117,3,34,17,0,117,23,1,0,0,0,118,
        123,3,22,11,0,119,120,5,30,0,0,120,122,3,22,11,0,121,119,1,0,0,0,
        122,125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,25,1,0,0,0,125,
        123,1,0,0,0,126,127,3,2,1,0,127,128,5,14,0,0,128,27,1,0,0,0,129,
        134,3,26,13,0,130,131,5,30,0,0,131,133,3,26,13,0,132,130,1,0,0,0,
        133,136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,29,1,0,0,0,136,
        134,1,0,0,0,137,138,5,14,0,0,138,140,5,32,0,0,139,141,3,24,12,0,
        140,139,1,0,0,0,140,141,1,0,0,0,141,142,1,0,0,0,142,143,5,33,0,0,
        143,31,1,0,0,0,144,145,3,2,1,0,145,147,5,34,0,0,146,148,3,24,12,
        0,147,146,1,0,0,0,147,148,1,0,0,0,148,149,1,0,0,0,149,150,5,35,0,
        0,150,162,1,0,0,0,151,162,5,9,0,0,152,162,5,10,0,0,153,162,5,11,
        0,0,154,162,5,12,0,0,155,162,5,13,0,0,156,162,5,14,0,0,157,158,5,
        32,0,0,158,159,3,34,17,0,159,160,5,33,0,0,160,162,1,0,0,0,161,144,
        1,0,0,0,161,151,1,0,0,0,161,152,1,0,0,0,161,153,1,0,0,0,161,154,
        1,0,0,0,161,155,1,0,0,0,161,156,1,0,0,0,161,157,1,0,0,0,162,33,1,
        0,0,0,163,164,6,17,-1,0,164,171,3,30,15,0,165,171,3,32,16,0,166,
        167,5,28,0,0,167,171,3,34,17,7,168,169,5,16,0,0,169,171,3,34,17,
        6,170,163,1,0,0,0,170,165,1,0,0,0,170,166,1,0,0,0,170,168,1,0,0,
        0,171,202,1,0,0,0,172,173,10,5,0,0,173,174,7,1,0,0,174,201,3,34,
        17,6,175,176,10,4,0,0,176,177,7,2,0,0,177,201,3,34,17,5,178,179,
        10,3,0,0,179,180,7,3,0,0,180,201,3,34,17,4,181,182,10,2,0,0,182,
        183,7,4,0,0,183,201,3,34,17,3,184,185,10,1,0,0,185,186,5,1,0,0,186,
        187,3,34,17,0,187,188,5,2,0,0,188,189,3,34,17,2,189,201,1,0,0,0,
        190,191,10,10,0,0,191,192,5,29,0,0,192,198,5,14,0,0,193,195,5,32,
        0,0,194,196,3,24,12,0,195,194,1,0,0,0,195,196,1,0,0,0,196,197,1,
        0,0,0,197,199,5,33,0,0,198,193,1,0,0,0,198,199,1,0,0,0,199,201,1,
        0,0,0,200,172,1,0,0,0,200,175,1,0,0,0,200,178,1,0,0,0,200,181,1,
        0,0,0,200,184,1,0,0,0,200,190,1,0,0,0,201,204,1,0,0,0,202,200,1,
        0,0,0,202,203,1,0,0,0,203,35,1,0,0,0,204,202,1,0,0,0,20,39,51,58,
        64,75,79,97,102,107,111,123,134,140,147,161,170,195,198,200,202
    ]

class smellyParser ( Parser ):

    grammarFileName = "smelly.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'func'", "'while'", 
                     "'break'", "'return'", "'continue'", "'''", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'nil'", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'>'", "'<'", "'>='", "'<='", "'&&'", "'||'", "'!'", 
                     "'.'", "','", "'='", "'('", "')'", "'{'", "'}'", "'->'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FUNC", "WHILE", "BREAK", 
                      "RETURN", "CONTINUE", "APOSTROPHE", "INT", "FLOAT", 
                      "STRING", "BOOL", "NIL", "ID", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "EEQ", "NEQ", "GT", "LT", "GTE", "LTE", 
                      "AND", "OR", "NOT", "DOT", "COMMA", "ASSIGN", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "RETURNS", "COMMENT", 
                      "WHITESPACE" ]

    RULE_parse = 0
    RULE_type = 1
    RULE_stmt = 2
    RULE_bodyStmts = 3
    RULE_body = 4
    RULE_ifStmt = 5
    RULE_elseifStmt = 6
    RULE_elseStmt = 7
    RULE_whileStmt = 8
    RULE_funcAssign = 9
    RULE_varAssign = 10
    RULE_arg = 11
    RULE_args = 12
    RULE_param = 13
    RULE_params = 14
    RULE_call = 15
    RULE_atom = 16
    RULE_expr = 17

    ruleNames =  [ "parse", "type", "stmt", "bodyStmts", "body", "ifStmt", 
                   "elseifStmt", "elseStmt", "whileStmt", "funcAssign", 
                   "varAssign", "arg", "args", "param", "params", "call", 
                   "atom", "expr" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FUNC=3
    WHILE=4
    BREAK=5
    RETURN=6
    CONTINUE=7
    APOSTROPHE=8
    INT=9
    FLOAT=10
    STRING=11
    BOOL=12
    NIL=13
    ID=14
    ADD=15
    SUB=16
    MUL=17
    DIV=18
    MOD=19
    EEQ=20
    NEQ=21
    GT=22
    LT=23
    GTE=24
    LTE=25
    AND=26
    OR=27
    NOT=28
    DOT=29
    COMMA=30
    ASSIGN=31
    LPAREN=32
    RPAREN=33
    LBRACE=34
    RBRACE=35
    RETURNS=36
    COMMENT=37
    WHITESPACE=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(smellyParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(smellyParser.StmtContext)
            else:
                return self.getTypedRuleContext(smellyParser.StmtContext,i)


        def getRuleIndex(self):
            return smellyParser.RULE_parse

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParse" ):
                return visitor.visitParse(self)
            else:
                return visitor.visitChildren(self)




    def parse(self):

        localctx = smellyParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4563500570) != 0):
                self.state = 36
                self.stmt()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(smellyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(smellyParser.ID, 0)

        def getRuleIndex(self):
            return smellyParser.RULE_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = smellyParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(smellyParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcAssign(self):
            return self.getTypedRuleContext(smellyParser.FuncAssignContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(smellyParser.WhileStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(smellyParser.IfStmtContext,0)


        def varAssign(self):
            return self.getTypedRuleContext(smellyParser.VarAssignContext,0)


        def expr(self):
            return self.getTypedRuleContext(smellyParser.ExprContext,0)


        def getRuleIndex(self):
            return smellyParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = smellyParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.funcAssign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.whileStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.ifStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.varAssign()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyStmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(smellyParser.StmtContext,0)


        def RETURN(self):
            return self.getToken(smellyParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(smellyParser.ExprContext,0)


        def CONTINUE(self):
            return self.getToken(smellyParser.CONTINUE, 0)

        def BREAK(self):
            return self.getToken(smellyParser.BREAK, 0)

        def getRuleIndex(self):
            return smellyParser.RULE_bodyStmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodyStmts" ):
                return visitor.visitBodyStmts(self)
            else:
                return visitor.visitChildren(self)




    def bodyStmts(self):

        localctx = smellyParser.BodyStmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bodyStmts)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 9, 10, 11, 12, 13, 14, 16, 28, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.stmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(smellyParser.RETURN)
                self.state = 55
                self.expr(0)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.match(smellyParser.CONTINUE)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.match(smellyParser.BREAK)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(smellyParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(smellyParser.RBRACE, 0)

        def bodyStmts(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(smellyParser.BodyStmtsContext)
            else:
                return self.getTypedRuleContext(smellyParser.BodyStmtsContext,i)


        def getRuleIndex(self):
            return smellyParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = smellyParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(smellyParser.LBRACE)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4563500794) != 0):
                self.state = 61
                self.bodyStmts()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(smellyParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(smellyParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(smellyParser.ExprContext,0)


        def body(self):
            return self.getTypedRuleContext(smellyParser.BodyContext,0)


        def elseifStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(smellyParser.ElseifStmtContext)
            else:
                return self.getTypedRuleContext(smellyParser.ElseifStmtContext,i)


        def elseStmt(self):
            return self.getTypedRuleContext(smellyParser.ElseStmtContext,0)


        def getRuleIndex(self):
            return smellyParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = smellyParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(smellyParser.IF)
            self.state = 70
            self.expr(0)
            self.state = 71
            self.body()
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 72
                    self.elseifStmt() 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 78
                self.elseStmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(smellyParser.ELSE, 0)

        def IF(self):
            return self.getToken(smellyParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(smellyParser.ExprContext,0)


        def body(self):
            return self.getTypedRuleContext(smellyParser.BodyContext,0)


        def getRuleIndex(self):
            return smellyParser.RULE_elseifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseifStmt" ):
                return visitor.visitElseifStmt(self)
            else:
                return visitor.visitChildren(self)




    def elseifStmt(self):

        localctx = smellyParser.ElseifStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_elseifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(smellyParser.ELSE)
            self.state = 82
            self.match(smellyParser.IF)
            self.state = 83
            self.expr(0)
            self.state = 84
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(smellyParser.ELSE, 0)

        def body(self):
            return self.getTypedRuleContext(smellyParser.BodyContext,0)


        def getRuleIndex(self):
            return smellyParser.RULE_elseStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStmt" ):
                return visitor.visitElseStmt(self)
            else:
                return visitor.visitChildren(self)




    def elseStmt(self):

        localctx = smellyParser.ElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elseStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(smellyParser.ELSE)
            self.state = 87
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(smellyParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(smellyParser.ExprContext,0)


        def body(self):
            return self.getTypedRuleContext(smellyParser.BodyContext,0)


        def getRuleIndex(self):
            return smellyParser.RULE_whileStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = smellyParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(smellyParser.WHILE)
            self.state = 90
            self.expr(0)
            self.state = 91
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(smellyParser.FUNC, 0)

        def ID(self):
            return self.getToken(smellyParser.ID, 0)

        def LPAREN(self):
            return self.getToken(smellyParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(smellyParser.RPAREN, 0)

        def body(self):
            return self.getTypedRuleContext(smellyParser.BodyContext,0)


        def params(self):
            return self.getTypedRuleContext(smellyParser.ParamsContext,0)


        def RETURNS(self):
            return self.getToken(smellyParser.RETURNS, 0)

        def type_(self):
            return self.getTypedRuleContext(smellyParser.TypeContext,0)


        def getRuleIndex(self):
            return smellyParser.RULE_funcAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncAssign" ):
                return visitor.visitFuncAssign(self)
            else:
                return visitor.visitChildren(self)




    def funcAssign(self):

        localctx = smellyParser.FuncAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcAssign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(smellyParser.FUNC)
            self.state = 94
            self.match(smellyParser.ID)
            self.state = 95
            self.match(smellyParser.LPAREN)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 96
                self.params()


            self.state = 99
            self.match(smellyParser.RPAREN)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 100
                self.match(smellyParser.RETURNS)
                self.state = 101
                self.type_()


            self.state = 104
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(smellyParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(smellyParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(smellyParser.ExprContext,0)


        def type_(self):
            return self.getTypedRuleContext(smellyParser.TypeContext,0)


        def ADD(self):
            return self.getToken(smellyParser.ADD, 0)

        def SUB(self):
            return self.getToken(smellyParser.SUB, 0)

        def MUL(self):
            return self.getToken(smellyParser.MUL, 0)

        def DIV(self):
            return self.getToken(smellyParser.DIV, 0)

        def MOD(self):
            return self.getToken(smellyParser.MOD, 0)

        def getRuleIndex(self):
            return smellyParser.RULE_varAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarAssign" ):
                return visitor.visitVarAssign(self)
            else:
                return visitor.visitChildren(self)




    def varAssign(self):

        localctx = smellyParser.VarAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_varAssign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 106
                self.type_()


            self.state = 109
            self.match(smellyParser.ID)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1015808) != 0):
                self.state = 110
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1015808) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 113
            self.match(smellyParser.ASSIGN)
            self.state = 114
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(smellyParser.ExprContext,0)


        def getRuleIndex(self):
            return smellyParser.RULE_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = smellyParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(smellyParser.ArgContext)
            else:
                return self.getTypedRuleContext(smellyParser.ArgContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(smellyParser.COMMA)
            else:
                return self.getToken(smellyParser.COMMA, i)

        def getRuleIndex(self):
            return smellyParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = smellyParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.arg()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 119
                self.match(smellyParser.COMMA)
                self.state = 120
                self.arg()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(smellyParser.TypeContext,0)


        def ID(self):
            return self.getToken(smellyParser.ID, 0)

        def getRuleIndex(self):
            return smellyParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = smellyParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.type_()
            self.state = 127
            self.match(smellyParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(smellyParser.ParamContext)
            else:
                return self.getTypedRuleContext(smellyParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(smellyParser.COMMA)
            else:
                return self.getToken(smellyParser.COMMA, i)

        def getRuleIndex(self):
            return smellyParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = smellyParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.param()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 130
                self.match(smellyParser.COMMA)
                self.state = 131
                self.param()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(smellyParser.ID, 0)

        def LPAREN(self):
            return self.getToken(smellyParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(smellyParser.RPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(smellyParser.ArgsContext,0)


        def getRuleIndex(self):
            return smellyParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = smellyParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(smellyParser.ID)
            self.state = 138
            self.match(smellyParser.LPAREN)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4563500544) != 0):
                self.state = 139
                self.args()


            self.state = 142
            self.match(smellyParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(smellyParser.TypeContext,0)


        def LBRACE(self):
            return self.getToken(smellyParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(smellyParser.RBRACE, 0)

        def args(self):
            return self.getTypedRuleContext(smellyParser.ArgsContext,0)


        def INT(self):
            return self.getToken(smellyParser.INT, 0)

        def FLOAT(self):
            return self.getToken(smellyParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(smellyParser.STRING, 0)

        def BOOL(self):
            return self.getToken(smellyParser.BOOL, 0)

        def NIL(self):
            return self.getToken(smellyParser.NIL, 0)

        def ID(self):
            return self.getToken(smellyParser.ID, 0)

        def LPAREN(self):
            return self.getToken(smellyParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(smellyParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(smellyParser.RPAREN, 0)

        def getRuleIndex(self):
            return smellyParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = smellyParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.type_()
                self.state = 145
                self.match(smellyParser.LBRACE)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4563500544) != 0):
                    self.state = 146
                    self.args()


                self.state = 149
                self.match(smellyParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(smellyParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                self.match(smellyParser.FLOAT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 153
                self.match(smellyParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 154
                self.match(smellyParser.BOOL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 155
                self.match(smellyParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 156
                self.match(smellyParser.ID)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 157
                self.match(smellyParser.LPAREN)
                self.state = 158
                self.expr(0)
                self.state = 159
                self.match(smellyParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.uop = None # Token
            self.op = None # Token

        def call(self):
            return self.getTypedRuleContext(smellyParser.CallContext,0)


        def atom(self):
            return self.getTypedRuleContext(smellyParser.AtomContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(smellyParser.ExprContext)
            else:
                return self.getTypedRuleContext(smellyParser.ExprContext,i)


        def NOT(self):
            return self.getToken(smellyParser.NOT, 0)

        def SUB(self):
            return self.getToken(smellyParser.SUB, 0)

        def ADD(self):
            return self.getToken(smellyParser.ADD, 0)

        def MUL(self):
            return self.getToken(smellyParser.MUL, 0)

        def DIV(self):
            return self.getToken(smellyParser.DIV, 0)

        def MOD(self):
            return self.getToken(smellyParser.MOD, 0)

        def EEQ(self):
            return self.getToken(smellyParser.EEQ, 0)

        def NEQ(self):
            return self.getToken(smellyParser.NEQ, 0)

        def GT(self):
            return self.getToken(smellyParser.GT, 0)

        def LT(self):
            return self.getToken(smellyParser.LT, 0)

        def GTE(self):
            return self.getToken(smellyParser.GTE, 0)

        def LTE(self):
            return self.getToken(smellyParser.LTE, 0)

        def AND(self):
            return self.getToken(smellyParser.AND, 0)

        def OR(self):
            return self.getToken(smellyParser.OR, 0)

        def IF(self):
            return self.getToken(smellyParser.IF, 0)

        def ELSE(self):
            return self.getToken(smellyParser.ELSE, 0)

        def DOT(self):
            return self.getToken(smellyParser.DOT, 0)

        def ID(self):
            return self.getToken(smellyParser.ID, 0)

        def LPAREN(self):
            return self.getToken(smellyParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(smellyParser.RPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(smellyParser.ArgsContext,0)


        def getRuleIndex(self):
            return smellyParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = smellyParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 164
                self.call()
                pass

            elif la_ == 2:
                self.state = 165
                self.atom()
                pass

            elif la_ == 3:
                self.state = 166
                localctx.uop = self.match(smellyParser.NOT)
                self.state = 167
                self.expr(7)
                pass

            elif la_ == 4:
                self.state = 168
                localctx.uop = self.match(smellyParser.SUB)
                self.state = 169
                self.expr(6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 202
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 200
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = smellyParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 172
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 173
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 174
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = smellyParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 175
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 176
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 177
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = smellyParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 178
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 179
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 180
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = smellyParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 181
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 182
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 183
                        self.expr(3)
                        pass

                    elif la_ == 5:
                        localctx = smellyParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 184
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 185
                        self.match(smellyParser.IF)
                        self.state = 186
                        self.expr(0)
                        self.state = 187
                        self.match(smellyParser.ELSE)
                        self.state = 188
                        self.expr(2)
                        pass

                    elif la_ == 6:
                        localctx = smellyParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 190
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 191
                        self.match(smellyParser.DOT)
                        self.state = 192
                        self.match(smellyParser.ID)
                        self.state = 198
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                        if la_ == 1:
                            self.state = 193
                            self.match(smellyParser.LPAREN)
                            self.state = 195
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4563500544) != 0):
                                self.state = 194
                                self.args()


                            self.state = 197
                            self.match(smellyParser.RPAREN)


                        pass

             
                self.state = 204
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         




