class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        temp = []
        while(self.array):
            temp.append(self.array.pop())
        self.array.append(x)
        while(temp):
            self.array.append(temp.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.array.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.array[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.array