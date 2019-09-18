class Solution:
    def evalRPN(self, tokens):
        oper_mapping = {
            "*": lambda a: lambda b: a * b,
            "/": lambda a: lambda b: b / a,
            "-": lambda a: lambda b: b - a,
            "+": lambda a: lambda b: a + b,
        }
        stack_oper = []
        while tokens:
            tok = tokens.pop()
            if tok in oper_mapping:
                stack_oper.append(oper_mapping[tok])
            else:
                expression = int(tok)
                while stack_oper:
                    operand = stack_oper.pop()
                    operand = operand(expression)
                    if callable(operand):
                        stack_oper.append(operand)
                        break
                    else:
                        expression = int(operand)
        return expression