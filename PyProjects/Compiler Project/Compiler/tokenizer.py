from dataclasses import dataclass
from enum import Enum, auto
from typing import List

class TokenType(Enum):
    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    LPAREN = auto()
    RPAREN = auto()
    IDENTIFIER = auto()
    EQUALS = auto()
    IF = auto()
    ELSE = auto()
    GREATER = auto()
    LESS = auto()
    SEMICOLON = auto()
    LBRACE = auto()    
    RBRACE = auto()

@dataclass
class Token:
    type: TokenType
    value: str
    line: int
    column: int

class Tokenizer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = self.text[0] if text else None
        self.line = 1
        self.column = 1

    def error(self):
        raise Exception(f'Invalid character at line {self.line}, column {self.column}')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
            if self.current_char == '\n':
                self.line += 1
                self.column = 0
            else:
                self.column += 1

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def number(self) -> Token:
        result = ''
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(TokenType.NUMBER, result, self.line, self.column)

    def identifier(self) -> Token:
        result = ''
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        
        # Check for keywords
        if result == 'if':
            return Token(TokenType.IF, result, self.line, self.column)
        elif result == 'else':
            return Token(TokenType.ELSE, result, self.line, self.column)
        
        return Token(TokenType.IDENTIFIER, result, self.line, self.column)

    def get_next_token(self) -> Token:
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return self.number()

            if self.current_char.isalpha():
                return self.identifier()

            if self.current_char == '+':
                token = Token(TokenType.PLUS, '+', self.line, self.column)
                self.advance()
                return token

            if self.current_char == '-':
                token = Token(TokenType.MINUS, '-', self.line, self.column)
                self.advance()
                return token

            if self.current_char == '*':
                token = Token(TokenType.MULTIPLY, '*', self.line, self.column)
                self.advance()
                return token

            if self.current_char == '/':
                token = Token(TokenType.DIVIDE, '/', self.line, self.column)
                self.advance()
                return token

            if self.current_char == '(':
                token = Token(TokenType.LPAREN, '(', self.line, self.column)
                self.advance()
                return token

            if self.current_char == ')':
                token = Token(TokenType.RPAREN, ')', self.line, self.column)
                self.advance()
                return token

            if self.current_char == '=':
                token = Token(TokenType.EQUALS, '=', self.line, self.column)
                self.advance()
                return token

            if self.current_char == '>':
                token = Token(TokenType.GREATER, '>', self.line, self.column)
                self.advance()
                return token

            if self.current_char == '<':
                token = Token(TokenType.LESS, '<', self.line, self.column)
                self.advance()
                return token

            if self.current_char == ';':
                token = Token(TokenType.SEMICOLON, ';', self.line, self.column)
                self.advance()
                return token

            if self.current_char == '{':
                token = Token(TokenType.LBRACE, '{', self.line, self.column)
                self.advance()
                return token

            if self.current_char == '}':
                token = Token(TokenType.RBRACE, '}', self.line, self.column)
                self.advance()
                return token

            self.error()

        return None