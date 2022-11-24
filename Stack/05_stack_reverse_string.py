from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def reverse_string(string):
    stack = Stack()

    for char in string:
        stack.push(char)

    str = ''
    while stack.size() != 0:
        str += stack.pop()

    return str



if __name__ == "__main__":

    str1 = "You can do it."
    str2 = "ofCourse"

    print(reverse_string(str1))
    print(reverse_string(str2))