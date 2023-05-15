from collections import deque

def validate_brackets(string):
    stack = []
    queue = deque()
    opening_brackets = '({['
    closing_brackets = ')}]'
    bracket_pairs = {'(': ')', '{': '}', '[': ']'}
    
    for char in string:
        if char in opening_brackets:
            stack.append(char)
            queue.append(char)
        elif char in closing_brackets:
            if not stack or bracket_pairs[stack.pop()] != char:
                return False
            queue.append(char)
    
    return len(stack) == 0 and len(queue) % 2 == 0

if __name__=="__main__":
    print(validate_brackets('{}'))  # True
    print(validate_brackets('{}(){}'))  # True
    print(validate_brackets('()[[Extra Characters]]'))  # True
    print(validate_brackets('(){}[[]]'))  # True
    print(validate_brackets('{}{Code}[Fellows](())'))  # True
    print(validate_brackets('[({}]'))  # False
    print(validate_brackets('(]('))  # False
    print(validate_brackets('{(})'))  # False
