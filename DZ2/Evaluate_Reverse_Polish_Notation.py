class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            else:
                stack.append(token)
            while stack[-1] in ['+', '-', '*', '/']:
                operation = stack.pop()
                second_num = stack.pop()
                first_num = stack.pop()
                match operation:
                    case '+':
                        stack.append(first_num + second_num)
                    case '-':
                        stack.append(first_num - second_num)
                    case '*':
                        stack.append(first_num * second_num)
                    case '/':
                        stack.append(int(first_num / second_num))

        return int(stack[0])
