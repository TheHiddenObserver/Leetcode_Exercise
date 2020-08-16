class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')':
                if not stack:
                    return False
                else:
                    if stack.pop() != '(':
                        return False
            elif c == ']':
                if not stack:
                    return False
                else:
                    if stack.pop() != '[':
                        return False
            elif c == '}':
                if not stack:
                    return False
                else:
                    if stack.pop() != '{':
                        return False
        if stack:
            return False
        return True
