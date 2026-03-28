class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open = ['(', '{', '[']

        close = [')', '}', ']']

        for item in s:
            if item in open:
                stack.append(item)
            else:
                if stack == []:
                    return False
                droped = stack.pop()
                if droped in open and close.index(item) == open.index(droped):
                    continue
                return False
        return stack == []
