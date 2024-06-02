class Queue():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.arr = [None] * maxsize
        self.front = 0
        self.rear = -1
        self.item_number = 0
    
    def insert(self, data):
        # ラップアラウンドするにはコメントアウトを外す
        # if self.rear == self.maxsize - 1:
        #     self.rear = -1
        self.rear += 1
        self.arr[self.rear] = data
        self.item_number += 1
    
    def remove(self):
        temp = self.arr[self.front]
        self.front += 1
        # ラップアラウンドするにはコメントアウトを外す
        # if self.front == self.maxsize:
        #     self.front = 0
        self.item_number -= 1
        return temp
    
    def peek(self):
        return self.arr[self.front]
    
    def is_empty(self):
        if self.item_number == 0:
            return True
        else:
            return False
    
    def is_full(self):
        if self.item_number == self.maxsize:
            return True
        else:
            return False

if __name__ == "__main__":
    q = Queue(5)

    i = 1
    while not q.is_full():
        q.insert(i)
        i += 1

    print("peek: " + str(q.peek()))

    while not q.is_empty():
        print(q.remove())
