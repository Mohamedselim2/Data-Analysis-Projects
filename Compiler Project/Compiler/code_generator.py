from typing import List, Dict
from .parser import ASTNode, BinaryOp, Number, Variable, Assignment, IfStatement

class CodeGenerator:
    def __init__(self):
        self.instructions = []
        self.variables: Dict[str, float] = {}
        self.label_count = 0

    def generate(self, nodes: List[ASTNode]) -> List[str]:
        self.instructions = []
        for node in nodes:
            self.visit(node)
        return self.instructions

    def get_new_label(self) -> str:
        self.label_count += 1
        return f'L{self.label_count}'

    def visit(self, node: ASTNode):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.generic_visit)
        return method(node)

    def generic_visit(self, node: ASTNode):
        raise Exception(f'No visit_{type(node).__name__} method')

    def visit_Number(self, node: Number):
        self.instructions.append(f'PUSH {node.value}')

    def visit_BinaryOp(self, node: BinaryOp):
        self.visit(node.left)
        self.visit(node.right)
        
        op_map = {
            'PLUS': 'ADD',
            'MINUS': 'SUB',
            'MULTIPLY': 'MUL',
            'DIVIDE': 'DIV',
            'LESS': 'LT',
            'GREATER': 'GT'
        }
        
        self.instructions.append(op_map[node.op.type.name])

    def visit_Variable(self, node: Variable):
        if node.name not in self.variables:
            raise Exception(f'Undefined variable: {node.name}')
        self.instructions.append(f'LOAD {node.name}')

    def visit_Assignment(self, node: Assignment):
        self.visit(node.value)
        self.instructions.append(f'STORE {node.name}')
        self.variables[node.name] = 0  # Initial value, will be updated during execution

    def visit_IfStatement(self, node: IfStatement):
        self.visit(node.condition)
        
        else_label = self.get_new_label()
        end_label = self.get_new_label()
        
        self.instructions.append(f'JZ {else_label}')
        
        for stmt in node.if_body:
            self.visit(stmt)
        
        self.instructions.append(f'JMP {end_label}')
        self.instructions.append(f'{else_label}:')
        
        if node.else_body:
            for stmt in node.else_body:
                self.visit(stmt)
        
        self.instructions.append(f'{end_label}:')