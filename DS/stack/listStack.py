class ListStack:
    def __init__(self):
        self.__stack = []

    def push(self, x):
        self.__stack.append(x)

    def pop(self):
        return self.__stack.pop()

    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__stack[-1]

    # Problem 02: push_front, pop_front, top_front
    def push_front(self, x):
        self.__stack.insert(0,x)
    def pop_front(self):
        self.__stack.pop(0)
    def top_front(self):
        if self.isEmpty():
            return None
        else:
            return self.__stack[0]

    def isEmpty(self) -> bool:
        return not bool(self.__stack)

    def popAll(self):
        self.__stack.clear() 

    def printStack(self):
        print("Stack from top:", end = ' ')
        for i in range(len(self.__stack)-1, -1, -1):
            print(self.__stack[i], end = ' ')
        print()

# 코드 6-6