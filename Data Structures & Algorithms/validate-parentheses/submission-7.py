class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        close_to_open = {
            ')': '(',
            ']': '[',
            '}' : '{'
        }

        stack = []
         
        for symbol in s:
            if symbol in '([{':
                stack.append(symbol)
            else:
                if not stack or stack[-1] != close_to_open[symbol]:
                    return False
                stack.pop()
        
        return not stack