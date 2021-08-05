from collections import deque

class MyStack:
    def __init__(self):
        self.items = []

    def empty(self):
         return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
         return self.items.pop()

    def top(self):
        return self.items[-1]

class MyQueue:
    def __init__(self):
        self.items = deque([])

    def empty(self):
         return self.items == deque([])

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
         return self.items.pop()

    def front(self):
        return self.items[-1]

s = MyStack()
print(s.empty())
s.push(5)
s.push(8)
print(s.pop())
s.push(3)
print(s.empty())
print(s.top())
print(s.pop())
print(s.pop())
print(s.pop())


"""q = MyQueue()
print(q.empty())
q.enqueue(5)
q.enqueue(8)
print(q.dequeue())
q.enqueue(3)
print(q.empty())
print(q.front())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())"""
