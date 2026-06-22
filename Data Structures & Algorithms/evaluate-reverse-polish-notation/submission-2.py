class Stack:
    def __init__(self):
        self.s = []

    def __len__(self):
        return len(self.s)

    def pop(self):
        return self.s.pop()

    def push(self, elem):
        self.s.append(elem)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        stack = Stack()
        ops = ['+', '-', '*', '/']   
        for token in tokens:
            if token not in ops:
                stack.push(int(token))
            else:
                num_2 = stack.pop()
                num_1 = stack.pop()
                result = self.exec_op(num_1, num_2, token)
                stack.push(result)
        return stack.pop()
    
    def exec_op(self, num_1, num_2, token):
        if token == '+':
            return num_1 + num_2
        elif token == '-':
            return num_1 - num_2
        elif token == '*':
            return num_1 * num_2
        elif token == '/':
            return int(float(num_1) / num_2)
