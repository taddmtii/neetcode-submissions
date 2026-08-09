class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        openToClose = {
            '(': ')',
            '[': ']',
            '{' : '}'
        }

        stack = []
        seen = []
        for symbol in s:
            stack.append(symbol)
        
        for _ in range(len(stack)):
            # Peek at the last element (top of the stack)
            elem = stack[-1]
            if elem in [')', ']', '}']:
                seen.append(elem)
                stack.pop()
            else:
                if seen:
                    elem = stack.pop()
                    close = seen.pop()
                    if openToClose[elem] != close:
                        return False
        
        return stack == seen