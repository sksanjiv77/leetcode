class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.first = []
        self.second = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.first.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.second:
            return self.second.pop()
        else:
            while self.first:
                elem = self.first.pop()
                self.second.append(elem)
            return self.second.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.second:
            return self.second[-1]
        else:
            while self.first:
                elem = self.first.pop()
                self.second.append(elem)
            return self.second[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.first or self.second:
            return False
        return True
    

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()