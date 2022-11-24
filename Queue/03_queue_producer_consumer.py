import threading
import time

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

shared_buffer = Queue()

def Producer(val):

    for element in val:
        print("Producer Produced : ", element)
        shared_buffer.enqueue(element)
        time.sleep(0.5)   

def Consumer():
    time.sleep(1)
    while True:
        data = shared_buffer.dequeue()
        print("Consumer Consumed : ", data)
        time.sleep(2)
        if(shared_buffer.size() == 0):
            break


if __name__ == "__main__":

    data = ['Wildcraft', 'Lavie', 'Hidesign', 'Tommy Hilfiger', 'Allen Solly']

    t1 = threading.Thread(target=Producer, args=(data, ))
    t2 = threading.Thread(target=Consumer)

    t1.start()
    t2.start()

