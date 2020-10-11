class Solution:
    def removeOuterParentheses(self, S):
        stack = []
        output = ""
        start, end = 0, 0
        for char in S:
            if char == '(':
                stack.append(char)
            else:
                stack = stack[:-1]
            if len(stack) == 0:
                p = self.removeOuter(S, start, end)
                # print start,end
                # print p
                output += p
                start = end + 1
            end += 1
        
        return output
    def removeOuter(self, S, start, end):
        return S[start + 1:end]
