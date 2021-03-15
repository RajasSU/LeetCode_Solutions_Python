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
        