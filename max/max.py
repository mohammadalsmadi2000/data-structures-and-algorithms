class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.stack:
            return None

        popped_value = self.stack.pop()

        if popped_value == self.max_stack[-1]:
            self.max_stack.pop()

        return popped_value

    def getMax(self):
        return self.max_stack[-1] if self.max_stack else None
