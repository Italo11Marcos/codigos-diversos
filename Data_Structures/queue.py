class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)