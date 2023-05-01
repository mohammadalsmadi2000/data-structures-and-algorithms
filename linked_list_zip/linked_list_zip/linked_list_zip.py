class Node:
    """
    It will store the data and the reference to the next node
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    create a sequence of Nodes
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        insert value into LinkedList as node
        """
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            self.head = node
            self.head.next = current

    def includes(self, key):
        search_element = Node(key)
        current = self.head
        while current:
            if current.value == search_element.value:
                return True
            current = current.next
        return False

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = node

    def insert_before(self, value, new_value):
        node = Node(new_value)
        if self.head.value == value:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current.next:
                if current.next.value == value:
                    node.next = current.next
                    current.next = node
                    break

                current = current.next
            if current.next is None:
                raise ValueError(f'node with value {value} it is not founded')

    def insert_after(self, value, new_value):
        node = Node(new_value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current:
                if current.value == value:
                    node.next = current.next
                    current.next = node
                    break
                current = current.next

            if current is None:
                raise ValueError(f'node with value {value} it is not founded')

    def to_string(self):
        """
        to  represent all the values in the Linked List, formatted
        """
        current = self.head
        formatting = ''
        opening = '{'
        closing = '}'
        while current:
            formatting += f'{opening}{current.value}{closing} -> '
            current = current.next
        formatting += 'NULL'
        return formatting


def zipLists(list1, list2):
    """
    Zips two linked lists together into one so that the nodes alternate between the two lists.

    Args:
    - list1: First linked list to be zipped.
    - list2: Second linked list to be zipped.

    Returns:
    - A new linked list that contains the zipped nodes from the input lists.

    This function modifies the input linked lists in-place and does not create any new nodes.
    """

    point1 = list1.head
    point2 = list2.head
    while point1 != None and point2 != None:
        next1 = point1.next
        next2 = point2.next
        point2.next = next1
        point1.next = point2
        point1 = next1
        point2 = next2
        list2.head = point2

    if point2:
        list1.Append(point2.data)
    return list1.to_string()


if __name__ == '__main__':
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)
    print()

    list2 = LinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(4)
    print()

    list1.to_string()
    list2.to_string()

    print(zipLists(list1, list2))
