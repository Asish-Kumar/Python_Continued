class Queue:
    def __init__(self):
        self.queue = list()

    def put(self, elem):
        self.queue.append(elem)

    def get(self):
        return self.queue.pop(0)


class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop(-1)


stack = Stack()
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.pop())
