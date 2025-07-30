from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.append(val)

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.buffer.popleft()
            print(f"Dequeued: {removed_item}")
            return removed_item
        else:
            print("Queue is empty. Cannot dequeue.")
            return None

    def front(self):
        return self.buffer[-1]

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
    
    def display(self):
        return "Queue: ", list(self.buffer)


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

    print(q.display())
    print()

    print(q.size())
    print()

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print()

    print(q.size())

    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)

    print(q.display())

    q.dequeue()
    print("Front: ", q.front())

    print(q.display())
