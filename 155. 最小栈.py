class MinStack:

    def __init__(self):
        self.stack = []


    def push(self, val):
        self.stack.append(val)


    def pop(self):
        self.stack.pop()


    def top(self):
        return self.stack[-1]


    def getMin(self):
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
minStack = None
input1 = ["MinStack","push","push","push","getMin","pop","top","getMin"]
input2 = [[],[-2],[0],[-3],[],[],[],[]]
for i in range(len(input1)):
    if input1[i] == "MinStack":
        minStack = MinStack()
    elif input1[i] == "push":
        minStack.push(input2[i][0])
    elif input1[i] == "getMin":
        print(minStack.getMin())
    elif input1[i] == "pop":
        minStack.pop()
    elif input1[i] == "top":
        print(minStack.top())
    print(input1[i],input2[i], minStack.stack)