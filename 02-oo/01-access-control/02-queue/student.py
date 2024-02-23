class Queue:
    def __init__(self):
        self.que = []

    def add(self, item):
        self.que.append(item)

    def next(self):
        name = self.que[0]
        self.que.pop(0)
        return name

    def is_empty(self):
        return len(self.que) == 0


queue = Queue()

queue.add("Alice")  # Alice arrives first
queue.add("Bob")  # Then Bob
queue.add("Charlie")  # And Charlie as third

print(queue.next())  # Alice arrived first, so she's the first to be served next
print(queue.next())  # This must return Bob
queue.next()
