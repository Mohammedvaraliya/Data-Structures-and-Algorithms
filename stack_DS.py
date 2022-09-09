'''
Stack Data structure
D
C
B
A
'''

class stack():
    
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]   

    def get_Stack(self):
        return self.items

s = stack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")
print(s.get_Stack())
s.pop()
print(s.get_Stack())
print(s.is_empty())
print(s.peek())

print("\n")

s2 = stack()
s2.push(1)
s2.push(2)
s2.push(3)
s2.push(4)
print(s2.get_Stack())
s2.pop()
print(s2.get_Stack())
print(s2.peek())
print(s2.is_empty())

