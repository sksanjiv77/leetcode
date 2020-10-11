class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for d in logs:
            if d == './':
                pass
            elif d == '../':
                stack = stack[:-1]
            else:
                stack.append(d)
        return len(stack)
            