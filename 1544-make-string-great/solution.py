class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            else:
                if self.destroy(char, stack):
                    stack = stack[:-1]
                else:
                    stack.append(char)
        return "".join(stack)
    
    def destroy(self, char, stack):
        prev = stack[-1]
        return abs(ord(prev) - ord(char)) == 32
             