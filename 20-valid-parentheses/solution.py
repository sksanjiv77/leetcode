class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        d = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in range(len(s)):
            if s[i] in d:
                stack.append(s[i])
            elif stack and s[i] == d[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack)==0
    
            
