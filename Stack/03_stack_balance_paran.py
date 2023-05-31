'''
Use a stack to check whether or not a string has
balanced usage of parenthesis.

Example:
    (), ()(), (({{[]}})) <== Balanced.
    ((),  {{{)}], [][]]] <== Not Balanced.

Balanced Example: {[]}

Non-Balanced Example: (()

Non-Balanced Example: ]]
'''

class Stack():
    
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

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    
    elif p1 == "{" and p2 == "}":
        return True

    elif p1 == "[" and p2 == "]":
        return True

    else:
        return False



def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while(index < len(paren_string)) and is_balanced:
        paren = paren_string[index]
        operparan = "{[("
        if paren in operparan:
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False

        index += 1

    if s.is_empty() and is_balanced:
        print("String is Balanced")
        return True
    else:
        print("String is not Balanced")
        return False


def is_paren_balanced_2nd_approach(s: str) -> bool:
    Map = {
        ")": "(", 
        "]": "[", 
        "}": "{"
    }
    stack = []

    for c in s:
        if c in Map:
            if stack and stack[-1] == Map[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False


if __name__ == "__main__":

    print(is_paren_balanced("()")) # Balanced paran
    print(is_paren_balanced_2nd_approach("()")) # Balanced paran
    print("\n")

    print(is_paren_balanced("(([{{{([])}}}]))")) # this is also balanced but complicated
    print(is_paren_balanced_2nd_approach("(([{{{([])}}}]))")) # this is also balanced but complicated
    print("\n")

    print(is_paren_balanced("[[}")) # its Not Balanced
    print(is_paren_balanced_2nd_approach("[[}")) # its Not Balanced
    print("\n")

    print(is_paren_balanced("(([[])}[}]))")) # this is Not Balanced
    print(is_paren_balanced_2nd_approach("(([[])}[}]))")) # this is Not Balanced
    print("\n")

    print(is_paren_balanced("()[]{}")) # this is Not Balanced
    print(is_paren_balanced_2nd_approach("()[]{}")) # this is Not Balanced
    print("\n")

    print(is_paren_balanced("(]")) # this is Not Balanced
    print(is_paren_balanced_2nd_approach("(]")) # this is Not Balanced

