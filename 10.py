"""

#question
Write a Python program to create a class named Stack with methods for pushing and
popping elements from the stack. Also, implement an iterator for the Stack class that
returns the elements in LIFO (last in first out) order.

"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None 
    def is_empty(self):
        return len(self.items) == 0

    def __iter__(self):
        return iter(self.items[::-1])

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Elements popped from the stack (LIFO order):")
for item in stack:
    print(item)

popped_item = stack.pop()
if popped_item is not None:
    print(f"Popped item: {popped_item}")
else:
    print("Stack is empty.")

stack.push(4)

print("\nRemaining elements in the stack (LIFO order):")
for item in stack:
    print(item)
