from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return
        
        return self.buffer.pop()

    def front(self):
        return self.buffer[-1]

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print(f"The {i} number is : ",front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()



if __name__ == "__main__":
    produce_binary_numbers(10)

    # q = Queue()
    # q.enqueue("1")
    # q.enqueue("2")
    # q.enqueue("3")
    # print(q.front())
    # print(q.front())