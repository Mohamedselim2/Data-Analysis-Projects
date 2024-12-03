from typing import List, Dict


class VirtualMachine:
    def __init__(self):
        self.stack: List[float] = []
        self.variables: Dict[str, float] = {}
        self.instruction_pointer = 0
        self.labels: Dict[str, int] = {}

    def execute(self, instructions: List[str]) -> List[str]:
        output = []

        # First pass: collect label positions
        for i, instr in enumerate(instructions):
            if instr.endswith(':'):
                self.labels[instr[:-1]] = i

        self.instruction_pointer = 0
        while self.instruction_pointer < len(instructions):
            instr = instructions[self.instruction_pointer]

            # Skip labels
            if instr.endswith(':'):
                self.instruction_pointer += 1
                continue

            parts = instr.split()
            command = parts[0]

            if command == 'PUSH':
                self.stack.append(float(parts[1]))
            elif command == 'POP':
                self.stack.pop()
            elif command == 'ADD':
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
            elif command == 'SUB':
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a - b)
            elif command == 'MUL':
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a * b)
            elif command == 'DIV':
                b = self.stack.pop()
                a = self.stack.pop()
                if b == 0:
                    raise Exception('Division by zero')
                self.stack.append(a / b)
            elif command == 'LT':
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(1.0 if a < b else 0.0)
            elif command == 'GT':
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(1.0 if a > b else 0.0)
            elif command == 'STORE':
                self.variables[parts[1]] = self.stack.pop()
                output.append(f'{parts[1]} = {self.variables[parts[1]]}')
            elif command == 'LOAD':
                self.stack.append(self.variables[parts[1]])
            elif command == 'JMP':
                self.instruction_pointer = self.labels[parts[1]]
                continue
            elif command == 'JZ':
                if self.stack.pop() == 0:
                    self.instruction_pointer = self.labels[parts[1]]
                    continue

            self.instruction_pointer += 1

        return output
