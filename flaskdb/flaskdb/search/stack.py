class Stack():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.arr = [None] * maxsize
        self.top = -1

    def push(self, data):
        self.top = self.top + 1
        self.arr[self.top] = data

    def pop(self):
        a = self.arr[self.top]
        self.top = self.top -1
        return a

    def peek(self):
        return self.arr[self.top]

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def is_full(self):
        if self.top == self.maxsize - 1:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Stack(5)

    i = 1
    while not s.is_full():
        s.push(i)
        i += 1

    print("peek: " + str(s.peek()))

    while not s.is_empty():
        print(s.pop())
