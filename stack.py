class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

stack = Stack()
while True:
    action = input("Enter 'push', 'pop', 'peek', or 'exit': ")
    if action == 'push':
        item = input("Enter item to push: ")
        stack.push(item)
        print(f"Pushed: {item}")
    elif action == 'pop':
        item = stack.pop()
        print(f"Popped: {item}" if item else "Stack is empty")
    elif action == 'peek':
        item = stack.peek()
        print(f"Top item: {item}" if item else "Stack is empty")
    elif action == 'exit':
        break
    else:
        print("Invalid action")
