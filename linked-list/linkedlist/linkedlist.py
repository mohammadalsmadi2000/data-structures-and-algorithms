class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        result = ""
        current = self.head
        while current:
            result += f"{{ {current.value} }} -> "
            current = current.next
        result += "NULL"
        return result


if __name__ == '__main__':
    list = LinkedList()
    list.insert(10)
    list.insert(20)
    list.insert(30)
    list.insert(40)


    str(list.to_string())
    print(list.to_string())