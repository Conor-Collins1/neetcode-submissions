class MinStack:

    def __init__(self):

        self.items = []
        self.min = []
        

    def push(self, val: int) -> None:
        
        self.items.append(val)
        if not self.min:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)
        

    def pop(self) -> None:
        if self.min:

            if self.min[-1] == self.items[-1]:
                self.min.pop()
        self.items.pop()
        
        

    def top(self) -> int:
        return self.items[-1]

        

    def getMin(self) -> int:
        if self.min:
            return self.min[-1]
        else:
             return 0
