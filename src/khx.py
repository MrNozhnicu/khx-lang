#!/usr/bin/env python3
"""
KHX Programming Language Interpreter
"""

import sys
import re
from enum import Enum, auto
from dataclasses import dataclass
from typing import Any, List, Dict, Optional


class TokenType(Enum):
    # Literals
    NUMBER = auto()
    STRING = auto()
    IDENTIFIER = auto()
    
    # Keywords
    LET = auto()
    FUNC = auto()
    CLASS = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    FOR = auto()
    RETURN = auto()
    MATCH = auto()
    PRINT = auto()
    TRUE = auto()
    FALSE = auto()
    NULL = auto()
    THIS = auto()
    WINDOW = auto()
    BUTTON = auto()
    LABEL = auto()
    INPUT = auto()
    SHOW = auto()
    
    # Operators
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    ASSIGN = auto()
    EQUAL = auto()
    NOT_EQUAL = auto()
    LESS = auto()
    GREATER = auto()
    LESS_EQUAL = auto()
    GREATER_EQUAL = auto()
    AND = auto()
    OR = auto()
    NOT = auto()
    
    # Delimiters
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    COMMA = auto()
    COLON = auto()
    ARROW = auto()
    DOT = auto()
    RANGE = auto()
    
    # Special
    NEWLINE = auto()
    EOF = auto()


@dataclass
class Token:
    type: TokenType
    value: Any
    line: int
    column: int


class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens = []
        
        self.keywords = {
            'let': TokenType.LET,
            'func': TokenType.FUNC,
            'class': TokenType.CLASS,
            'if': TokenType.IF,
            'else': TokenType.ELSE,
            'while': TokenType.WHILE,
            'for': TokenType.FOR,
            'return': TokenType.RETURN,
            'match': TokenType.MATCH,
            'print': TokenType.PRINT,
            'true': TokenType.TRUE,
            'false': TokenType.FALSE,
            'null': TokenType.NULL,
            'this': TokenType.THIS,
            'and': TokenType.AND,
            'or': TokenType.OR,
            'not': TokenType.NOT,
            'window': TokenType.WINDOW,
            'button': TokenType.BUTTON,
            'label': TokenType.LABEL,
            'input': TokenType.INPUT,
            'show': TokenType.SHOW,
        }
    
    def current_char(self) -> Optional[str]:
        if self.pos >= len(self.source):
            return None
        return self.source[self.pos]
    
    def peek_char(self, offset=1) -> Optional[str]:
        pos = self.pos + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]
    
    def advance(self):
        if self.pos < len(self.source) and self.source[self.pos] == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        self.pos += 1
    
    def skip_whitespace(self):
        while self.current_char() and self.current_char() in ' \t\r':
            self.advance()
    
    def skip_comment(self):
        if self.current_char() == '/' and self.peek_char() == '/':
            while self.current_char() and self.current_char() != '\n':
                self.advance()
    
    def read_number(self) -> Token:
        start_col = self.column
        num_str = ''
        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            num_str += self.current_char()
            self.advance()
        
        value = float(num_str) if '.' in num_str else int(num_str)
        return Token(TokenType.NUMBER, value, self.line, start_col)
    
    def read_string(self) -> Token:
        start_col = self.column
        quote = self.current_char()
        self.advance()  # skip opening quote
        
        string_val = ''
        while self.current_char() and self.current_char() != quote:
            if self.current_char() == '\\':
                self.advance()
                if self.current_char() == 'n':
                    string_val += '\n'
                elif self.current_char() == 't':
                    string_val += '\t'
                else:
                    string_val += self.current_char()
            else:
                string_val += self.current_char()
            self.advance()
        
        self.advance()  # skip closing quote
        return Token(TokenType.STRING, string_val, self.line, start_col)
    
    def read_identifier(self) -> Token:
        start_col = self.column
        ident = ''
        while self.current_char() and (self.current_char().isalnum() or self.current_char() == '_'):
            ident += self.current_char()
            self.advance()
        
        token_type = self.keywords.get(ident, TokenType.IDENTIFIER)
        value = ident if token_type == TokenType.IDENTIFIER else None
        return Token(token_type, value, self.line, start_col)
    
    def tokenize(self) -> List[Token]:
        while self.pos < len(self.source):
            self.skip_whitespace()
            
            if not self.current_char():
                break
            
            # Comments
            if self.current_char() == '/' and self.peek_char() == '/':
                self.skip_comment()
                continue
            
            # Newlines
            if self.current_char() == '\n':
                self.advance()
                continue
            
            # Numbers
            if self.current_char().isdigit():
                self.tokens.append(self.read_number())
                continue
            
            # Strings
            if self.current_char() in '"\'':
                self.tokens.append(self.read_string())
                continue
            
            # Identifiers and keywords
            if self.current_char().isalpha() or self.current_char() == '_':
                self.tokens.append(self.read_identifier())
                continue
            
            # Operators and delimiters
            col = self.column
            char = self.current_char()
            
            if char == '+':
                self.tokens.append(Token(TokenType.PLUS, None, self.line, col))
                self.advance()
            elif char == '-' and self.peek_char() == '>':
                self.tokens.append(Token(TokenType.ARROW, None, self.line, col))
                self.advance()
                self.advance()
            elif char == '-':
                self.tokens.append(Token(TokenType.MINUS, None, self.line, col))
                self.advance()
            elif char == '*':
                self.tokens.append(Token(TokenType.MULTIPLY, None, self.line, col))
                self.advance()
            elif char == '/':
                self.tokens.append(Token(TokenType.DIVIDE, None, self.line, col))
                self.advance()
            elif char == '=' and self.peek_char() == '=':
                self.tokens.append(Token(TokenType.EQUAL, None, self.line, col))
                self.advance()
                self.advance()
            elif char == '!':
                self.tokens.append(Token(TokenType.NOT_EQUAL, None, self.line, col))
                self.advance()
                self.advance()
            elif char == '<' and self.peek_char() == '=':
                self.tokens.append(Token(TokenType.LESS_EQUAL, None, self.line, col))
                self.advance()
                self.advance()
            elif char == '<':
                self.tokens.append(Token(TokenType.LESS, None, self.line, col))
                self.advance()
            elif char == '>' and self.peek_char() == '=':
                self.tokens.append(Token(TokenType.GREATER_EQUAL, None, self.line, col))
                self.advance()
                self.advance()
            elif char == '>':
                self.tokens.append(Token(TokenType.GREATER, None, self.line, col))
                self.advance()
            elif char == '=':
                self.tokens.append(Token(TokenType.ASSIGN, None, self.line, col))
                self.advance()
            elif char == '(':
                self.tokens.append(Token(TokenType.LPAREN, None, self.line, col))
                self.advance()
            elif char == ')':
                self.tokens.append(Token(TokenType.RPAREN, None, self.line, col))
                self.advance()
            elif char == '{':
                self.tokens.append(Token(TokenType.LBRACE, None, self.line, col))
                self.advance()
            elif char == '}':
                self.tokens.append(Token(TokenType.RBRACE, None, self.line, col))
                self.advance()
            elif char == ',':
                self.tokens.append(Token(TokenType.COMMA, None, self.line, col))
                self.advance()
            elif char == ':':
                self.tokens.append(Token(TokenType.COLON, None, self.line, col))
                self.advance()
            elif char == '.':
                if self.peek_char() == '.':
                    self.tokens.append(Token(TokenType.RANGE, None, self.line, col))
                    self.advance()
                    self.advance()
                else:
                    self.tokens.append(Token(TokenType.DOT, None, self.line, col))
                    self.advance()
            else:
                raise SyntaxError(f"Неизвестный символ '{char}' на строке {self.line}:{col}")
        
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens


class ASTNode:
    pass


@dataclass
class NumberNode(ASTNode):
    value: float


@dataclass
class StringNode(ASTNode):
    value: str


@dataclass
class BoolNode(ASTNode):
    value: bool


@dataclass
class NullNode(ASTNode):
    pass


@dataclass
class IdentifierNode(ASTNode):
    name: str


@dataclass
class BinaryOpNode(ASTNode):
    left: ASTNode
    operator: TokenType
    right: ASTNode


@dataclass
class UnaryOpNode(ASTNode):
    operator: TokenType
    operand: ASTNode


@dataclass
class AssignNode(ASTNode):
    name: str
    value: ASTNode
    type_hint: Optional[str] = None


@dataclass
class FunctionDefNode(ASTNode):
    name: str
    params: List[tuple]
    body: List[ASTNode]
    return_type: Optional[str] = None


@dataclass
class FunctionCallNode(ASTNode):
    name: str
    args: List[ASTNode]


@dataclass
class ReturnNode(ASTNode):
    value: Optional[ASTNode]


@dataclass
class IfNode(ASTNode):
    condition: ASTNode
    then_body: List[ASTNode]
    else_body: Optional[List[ASTNode]] = None


@dataclass
class WhileNode(ASTNode):
    condition: ASTNode
    body: List[ASTNode]


@dataclass
class PrintNode(ASTNode):
    value: ASTNode


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
    
    def current_token(self) -> Token:
        if self.pos >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[self.pos]
    
    def peek_token(self, offset=1) -> Token:
        pos = self.pos + offset
        if pos >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[pos]
    
    def advance(self):
        self.pos += 1
    
    def expect(self, token_type: TokenType):
        if self.current_token().type != token_type:
            raise SyntaxError(f"Ожидался {token_type}, получен {self.current_token().type}")
        token = self.current_token()
        self.advance()
        return token
    
    def parse(self) -> List[ASTNode]:
        statements = []
        while self.current_token().type != TokenType.EOF:
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        return statements
    
    def parse_statement(self) -> Optional[ASTNode]:
        token = self.current_token()
        
        if token.type == TokenType.LET:
            return self.parse_assignment()
        elif token.type == TokenType.FUNC:
            return self.parse_function_def()
        elif token.type == TokenType.IF:
            return self.parse_if()
        elif token.type == TokenType.WHILE:
            return self.parse_while()
        elif token.type == TokenType.RETURN:
            return self.parse_return()
        elif token.type == TokenType.PRINT:
            return self.parse_print()
        elif token.type == TokenType.IDENTIFIER:
            if self.peek_token().type == TokenType.LPAREN:
                return self.parse_function_call()
            elif self.peek_token().type == TokenType.ASSIGN:
                return self.parse_reassignment()
        
        return None
    
    def parse_assignment(self) -> AssignNode:
        self.expect(TokenType.LET)
        name = self.expect(TokenType.IDENTIFIER).value
        
        type_hint = None
        if self.current_token().type == TokenType.COLON:
            self.advance()
            type_hint = self.expect(TokenType.IDENTIFIER).value
        
        self.expect(TokenType.ASSIGN)
        value = self.parse_expression()
        
        return AssignNode(name, value, type_hint)
    
    def parse_reassignment(self) -> AssignNode:
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.ASSIGN)
        value = self.parse_expression()
        return AssignNode(name, value)
    
    def parse_function_def(self) -> FunctionDefNode:
        self.expect(TokenType.FUNC)
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.LPAREN)
        
        params = []
        while self.current_token().type != TokenType.RPAREN:
            param_name = self.expect(TokenType.IDENTIFIER).value
            param_type = None
            if self.current_token().type == TokenType.COLON:
                self.advance()
                param_type = self.expect(TokenType.IDENTIFIER).value
            params.append((param_name, param_type))
            
            if self.current_token().type == TokenType.COMMA:
                self.advance()
        
        self.expect(TokenType.RPAREN)
        
        return_type = None
        if self.current_token().type == TokenType.ARROW:
            self.advance()
            return_type = self.expect(TokenType.IDENTIFIER).value
        
        self.expect(TokenType.LBRACE)
        body = []
        while self.current_token().type != TokenType.RBRACE:
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
        self.expect(TokenType.RBRACE)
        
        return FunctionDefNode(name, params, body, return_type)
    
    def parse_function_call(self) -> FunctionCallNode:
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.LPAREN)
        
        args = []
        while self.current_token().type != TokenType.RPAREN:
            args.append(self.parse_expression())
            if self.current_token().type == TokenType.COMMA:
                self.advance()
        
        self.expect(TokenType.RPAREN)
        return FunctionCallNode(name, args)
    
    def parse_if(self) -> IfNode:
        self.expect(TokenType.IF)
        self.expect(TokenType.LPAREN)
        condition = self.parse_expression()
        self.expect(TokenType.RPAREN)
        self.expect(TokenType.LBRACE)
        
        then_body = []
        while self.current_token().type != TokenType.RBRACE:
            stmt = self.parse_statement()
            if stmt:
                then_body.append(stmt)
        self.expect(TokenType.RBRACE)
        
        else_body = None
        if self.current_token().type == TokenType.ELSE:
            self.advance()
            self.expect(TokenType.LBRACE)
            else_body = []
            while self.current_token().type != TokenType.RBRACE:
                stmt = self.parse_statement()
                if stmt:
                    else_body.append(stmt)
            self.expect(TokenType.RBRACE)
        
        return IfNode(condition, then_body, else_body)
    
    def parse_while(self) -> WhileNode:
        self.expect(TokenType.WHILE)
        self.expect(TokenType.LPAREN)
        condition = self.parse_expression()
        self.expect(TokenType.RPAREN)
        self.expect(TokenType.LBRACE)
        
        body = []
        while self.current_token().type != TokenType.RBRACE:
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
        self.expect(TokenType.RBRACE)
        
        return WhileNode(condition, body)
    
    def parse_return(self) -> ReturnNode:
        self.expect(TokenType.RETURN)
        value = None
        if self.current_token().type not in [TokenType.RBRACE, TokenType.EOF]:
            value = self.parse_expression()
        return ReturnNode(value)
    
    def parse_print(self) -> PrintNode:
        self.expect(TokenType.PRINT)
        self.expect(TokenType.LPAREN)
        value = self.parse_expression()
        self.expect(TokenType.RPAREN)
        return PrintNode(value)
    
    def parse_expression(self) -> ASTNode:
        return self.parse_logical_or()
    
    def parse_logical_or(self) -> ASTNode:
        left = self.parse_logical_and()
        
        while self.current_token().type == TokenType.OR:
            op = self.current_token().type
            self.advance()
            right = self.parse_logical_and()
            left = BinaryOpNode(left, op, right)
        
        return left
    
    def parse_logical_and(self) -> ASTNode:
        left = self.parse_comparison()
        
        while self.current_token().type == TokenType.AND:
            op = self.current_token().type
            self.advance()
            right = self.parse_comparison()
            left = BinaryOpNode(left, op, right)
        
        return left
    
    def parse_comparison(self) -> ASTNode:
        left = self.parse_additive()
        
        while self.current_token().type in [TokenType.EQUAL, TokenType.NOT_EQUAL,
                                            TokenType.LESS, TokenType.GREATER,
                                            TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL]:
            op = self.current_token().type
            self.advance()
            right = self.parse_additive()
            left = BinaryOpNode(left, op, right)
        
        return left
    
    def parse_additive(self) -> ASTNode:
        left = self.parse_multiplicative()
        
        while self.current_token().type in [TokenType.PLUS, TokenType.MINUS]:
            op = self.current_token().type
            self.advance()
            right = self.parse_multiplicative()
            left = BinaryOpNode(left, op, right)
        
        return left
    
    def parse_multiplicative(self) -> ASTNode:
        left = self.parse_unary()
        
        while self.current_token().type in [TokenType.MULTIPLY, TokenType.DIVIDE]:
            op = self.current_token().type
            self.advance()
            right = self.parse_unary()
            left = BinaryOpNode(left, op, right)
        
        return left
    
    def parse_unary(self) -> ASTNode:
        if self.current_token().type in [TokenType.MINUS, TokenType.NOT]:
            op = self.current_token().type
            self.advance()
            operand = self.parse_unary()
            return UnaryOpNode(op, operand)
        
        return self.parse_primary()
    
    def parse_primary(self) -> ASTNode:
        token = self.current_token()
        
        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        elif token.type == TokenType.STRING:
            self.advance()
            return StringNode(token.value)
        elif token.type == TokenType.TRUE:
            self.advance()
            return BoolNode(True)
        elif token.type == TokenType.FALSE:
            self.advance()
            return BoolNode(False)
        elif token.type == TokenType.NULL:
            self.advance()
            return NullNode()
        elif token.type == TokenType.IDENTIFIER:
            if self.peek_token().type == TokenType.LPAREN:
                return self.parse_function_call()
            else:
                self.advance()
                return IdentifierNode(token.value)
        elif token.type == TokenType.LPAREN:
            self.advance()
            expr = self.parse_expression()
            self.expect(TokenType.RPAREN)
            return expr
        
        raise SyntaxError(f"Неожиданный токен: {token.type}")


class Interpreter:
    def __init__(self):
        self.global_scope = {}
        self.local_scopes = []
        self.return_value = None
    
    def get_variable(self, name: str):
        for scope in reversed(self.local_scopes):
            if name in scope:
                return scope[name]
        if name in self.global_scope:
            return self.global_scope[name]
        raise NameError(f"Переменная '{name}' не определена")
    
    def set_variable(self, name: str, value: Any):
        if self.local_scopes:
            self.local_scopes[-1][name] = value
        else:
            self.global_scope[name] = value
    
    def execute(self, nodes: List[ASTNode]):
        for node in nodes:
            self.eval_node(node)
            if self.return_value is not None:
                break
    
    def eval_node(self, node: ASTNode) -> Any:
        if isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, StringNode):
            return node.value
        elif isinstance(node, BoolNode):
            return node.value
        elif isinstance(node, NullNode):
            return None
        elif isinstance(node, IdentifierNode):
            return self.get_variable(node.name)
        elif isinstance(node, BinaryOpNode):
            return self.eval_binary_op(node)
        elif isinstance(node, UnaryOpNode):
            return self.eval_unary_op(node)
        elif isinstance(node, AssignNode):
            value = self.eval_node(node.value)
            self.set_variable(node.name, value)
            return value
        elif isinstance(node, FunctionDefNode):
            self.set_variable(node.name, node)
            return None
        elif isinstance(node, FunctionCallNode):
            return self.eval_function_call(node)
        elif isinstance(node, ReturnNode):
            self.return_value = self.eval_node(node.value) if node.value else None
            return self.return_value
        elif isinstance(node, IfNode):
            return self.eval_if(node)
        elif isinstance(node, WhileNode):
            return self.eval_while(node)
        elif isinstance(node, PrintNode):
            value = self.eval_node(node.value)
            print(value)
            return None
        
        return None
    
    def eval_binary_op(self, node: BinaryOpNode) -> Any:
        left = self.eval_node(node.left)
        right = self.eval_node(node.right)
        
        if node.operator == TokenType.PLUS:
            return left + right
        elif node.operator == TokenType.MINUS:
            return left - right
        elif node.operator == TokenType.MULTIPLY:
            return left * right
        elif node.operator == TokenType.DIVIDE:
            return left / right
        elif node.operator == TokenType.EQUAL:
            return left == right
        elif node.operator == TokenType.NOT_EQUAL:
            return left != right
        elif node.operator == TokenType.LESS:
            return left < right
        elif node.operator == TokenType.GREATER:
            return left > right
        elif node.operator == TokenType.LESS_EQUAL:
            return left <= right
        elif node.operator == TokenType.GREATER_EQUAL:
            return left >= right
        elif node.operator == TokenType.AND:
            return left and right
        elif node.operator == TokenType.OR:
            return left or right
    
    def eval_unary_op(self, node: UnaryOpNode) -> Any:
        operand = self.eval_node(node.operand)
        
        if node.operator == TokenType.MINUS:
            return -operand
        elif node.operator == TokenType.NOT:
            return not operand
    
    def eval_function_call(self, node: FunctionCallNode) -> Any:
        func = self.get_variable(node.name)
        
        if not isinstance(func, FunctionDefNode):
            raise TypeError(f"'{node.name}' не является функцией")
        
        if len(node.args) != len(func.params):
            raise TypeError(f"Функция '{node.name}' ожидает {len(func.params)} аргументов, получено {len(node.args)}")
        
        # Create new scope
        new_scope = {}
        for (param_name, _), arg in zip(func.params, node.args):
            new_scope[param_name] = self.eval_node(arg)
        
        self.local_scopes.append(new_scope)
        self.return_value = None
        
        for stmt in func.body:
            self.eval_node(stmt)
            if self.return_value is not None:
                break
        
        result = self.return_value
        self.return_value = None
        self.local_scopes.pop()
        
        return result
    
    def eval_if(self, node: IfNode):
        condition = self.eval_node(node.condition)
        
        if condition:
            for stmt in node.then_body:
                self.eval_node(stmt)
                if self.return_value is not None:
                    break
        elif node.else_body:
            for stmt in node.else_body:
                self.eval_node(stmt)
                if self.return_value is not None:
                    break
    
    def eval_while(self, node: WhileNode):
        while self.eval_node(node.condition):
            for stmt in node.body:
                self.eval_node(stmt)
                if self.return_value is not None:
                    return


def main():
    if len(sys.argv) < 2:
        print("Использование: python khx.py <файл.khx>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            source = f.read()
        
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        interpreter = Interpreter()
        interpreter.execute(ast)
        
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
