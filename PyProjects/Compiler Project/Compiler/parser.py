from dataclasses import dataclass
from typing import List, Optional
from .tokenizer import Token, TokenType

@dataclass
class ASTNode:
    pass

@dataclass
class BinaryOp(ASTNode):
    left: ASTNode
    op: Token
    right: ASTNode

@dataclass
class Number(ASTNode):
    token: Token
    value: float

@dataclass
class Variable(ASTNode):
    token: Token
    name: str

@dataclass
class Assignment(ASTNode):
    name: str
    value: ASTNode

@dataclass
class IfStatement(ASTNode):
    condition: ASTNode
    if_body: List[ASTNode]
    else_body: Optional[List[ASTNode]]

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        self.current_token = tokens[0] if tokens else None

    def error(self):
        raise Exception('Invalid syntax')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.tokens) - 1:
            self.current_token = None
        else:
            self.current_token = self.tokens[self.pos]

    def eat(self, token_type: TokenType):
        if self.current_token and self.current_token.type == token_type:
            self.advance()
        else:
            self.error()

    def factor(self) -> ASTNode:
        token = self.current_token
        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return Number(token, float(token.value))
        elif token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
            return Variable(token, token.value)
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node
        self.error()

    def term(self) -> ASTNode:
        node = self.factor()

        while self.current_token and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            token = self.current_token
            if token.type == TokenType.MULTIPLY:
                self.eat(TokenType.MULTIPLY)
            else:
                self.eat(TokenType.DIVIDE)

            node = BinaryOp(left=node, op=token, right=self.factor())

        return node

    def expr(self) -> ASTNode:
        node = self.term()

        while self.current_token and self.current_token.type in (TokenType.PLUS, TokenType.MINUS, TokenType.GREATER, TokenType.LESS):
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)
            elif token.type == TokenType.GREATER:
                self.eat(TokenType.GREATER)
            else:
                self.eat(TokenType.LESS)

            node = BinaryOp(left=node, op=token, right=self.term())

        return node

    def assignment(self) -> ASTNode:
        var_token = self.current_token
        var_name = var_token.value
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.EQUALS)
        expr = self.expr()
        self.eat(TokenType.SEMICOLON)
        return Assignment(var_name, expr)

    def block(self) -> List[ASTNode]:
        statements = []
        self.eat(TokenType.LBRACE)
        
        while self.current_token and self.current_token.type != TokenType.RBRACE:
            if self.current_token.type == TokenType.IDENTIFIER:
                statements.append(self.assignment())
            else:
                statements.append(self.expr())
                if self.current_token and self.current_token.type == TokenType.SEMICOLON:
                    self.eat(TokenType.SEMICOLON)
        
        self.eat(TokenType.RBRACE)
        return statements

    def if_statement(self) -> ASTNode:
        self.eat(TokenType.IF)
        condition = self.expr()
        if_body = self.block()
        
        else_body = None
        if self.current_token and self.current_token.type == TokenType.ELSE:
            self.eat(TokenType.ELSE)
            else_body = self.block()

        return IfStatement(condition, if_body, else_body)

    def parse(self) -> List[ASTNode]:
        nodes = []
        while self.current_token:
            if self.current_token.type == TokenType.IF:
                nodes.append(self.if_statement())
            elif self.current_token.type == TokenType.IDENTIFIER:
                nodes.append(self.assignment())
            else:
                nodes.append(self.expr())
                if self.current_token and self.current_token.type == TokenType.SEMICOLON:
                    self.eat(TokenType.SEMICOLON)
        
        return nodes