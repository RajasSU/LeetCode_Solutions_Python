'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.minimum = None

    def push(self, x: int) -> None:
        self.data.append(x)
        

    def pop(self) -> None:
        self.data.pop()
        

    def top(self) -> int:
        idx= len(self.data)-1
        top= self.data[idx]
        return top
        

    def getMin(self) -> int:
        m= min(self.data)
        return m
        