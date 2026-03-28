class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            stack.append(token)
            while stack[-1] in ['+', '-', '*', '/']:
                operation = stack.pop()
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(str(int(eval(first_num + operation + second_num))))

        return int(stack[0])