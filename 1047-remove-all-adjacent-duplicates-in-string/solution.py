class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for char in S:
            if not stack or char != stack[-1]:
                 stack.append(char)
            else:
                stack = stack[:-1]
        return "".join(stack)
        
        