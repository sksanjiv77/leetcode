class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if not self.q: #queue is empty
            self.q.append(x)
        else:
            self.q = self.helper(self.q, x)
            
        
    def helper(self, arr, x):
        return [x] + arr
            
            

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # a = self.q[0]
        # self.q = self.q[1:]
        # return a
        return self.q.pop(0)
    def top(self) -> int:
        """
        Get the top element.
        """
        a = self.q[0]
        
        return a

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()