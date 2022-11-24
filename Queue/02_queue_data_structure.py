from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.append(val)

    def dequeue(self):
        return self.buffer.pop()

    def peek(self):
        return self.buffer[-1]

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


if __name__ == "__main__":

    q = Queue()

    q.enqueue({
        'company': 'India Mart',
        'timestamp': '22 nov, 10.12 AM',
        'price': 935.6
    })
    q.enqueue({
        'company': 'India Mart',
        'timestamp': '23 nov, 10.13 AM',
        'price': 879.4
    })
    q.enqueue({
        'company': 'India Mart',
        'timestamp': '24 nov, 10.14 AM',
        'price': 1198.3
    })

    print(q.buffer)
    print("\n")

    print(q.size())
    print("\n")

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print("\n")

    print(q.size())
