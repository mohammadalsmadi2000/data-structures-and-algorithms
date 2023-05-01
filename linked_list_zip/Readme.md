# Zip Linked Lists
## Challenge Description
Given two linked lists, zip the two lists together into one so that the nodes alternate between the two lists.

## Whiteboard Process

### Problem Statement
Given two linked lists list1 and list2, implement a function zipLists that combines the two linked lists into a single linked list by alternating nodes from each list. The function should return a reference to the head of the zipped list.

### Examples Visualization

![t1-5088](https://user-images.githubusercontent.com/60603704/235455259-46b1c28b-3c09-4224-8755-043f92c77584.png)
Example 1:

```
Input:
list1: {1} -> {3} -> {2} -> NULL
list2: {5} -> {9} -> {4} -> NULL

Output:
{1} -> {5} -> {3} -> {9} -> {2} -> {4} -> NULL

```

### Algorithm
1. Initialize two pointers point1 and point2 to the heads of list1 and list2 respectively.
2. While point1 and point2 are not None, do the following:
* Save the next node after point1 and point2 in next1 and next2 respectively.
* Set the next pointer of point2 to next1.
* Set the next pointer of point1 to point2.
* Update point1 to next1 and point2 to next2.
* Update the head of list2 to point2.
3. If there are any remaining nodes in list2, append them to the end of list1.
4. Return the head of list1.


### Big O Analysis
The time complexity of this algorithm is O(n), where n is the length of the shorter of the two input linked lists. This is because the algorithm iterates over each node in the shorter list exactly once, performing constant-time operations on each node.

The space complexity of this algorithm is O(1), as the algorithm only uses a constant amount of extra memory regardless of the input size. Specifically, it uses a constant number of pointers and temporary variables to keep track of the state of the algorithm, but does not create any new linked list nodes or other data structures.

Overall, this algorithm is both time and space efficient, and can be used to efficiently combine two linked lists in a manner that alternates their nodes.

## Approach & Efficiency
We can solve this problem by using two pointers to traverse both linked lists and connect their nodes together in a new linked list. We will iterate over the nodes of the linked lists until one of them reaches the end. At each iteration, we will connect the current node of the second list to the next node of the first list, and the current node of the first list to the current node of the second list. We will also update the pointers to the next nodes accordingly.

The time complexity of this approach is O(n), where n is the length of the shorter linked list, because we only need to iterate over the nodes of the shorter list. The space complexity is O(1), because we are not creating any new nodes, just rearranging the pointers.

## Solution
To use the zipLists function, create two linked lists and call the function with the two lists as arguments:
```
list1 = LinkedList()
list1.insert(1)
list1.insert(3)
list1.insert(2)

list2 = LinkedList()
list2.insert(5)
list2.insert(9)
list2.insert(4)

result = zipLists(list1, list2)
print(result)  # {1} -> {5} -> {3} -> {9} -> {2} -> {4} -> NULL

```
This will return a new linked list that contains the nodes from the two input linked lists zipped together. The nodes alternate between the two lists, starting with the first node of the first list. If one of the input lists is longer than the other, the remaining nodes are appended to the end of the resulting list.

# Stretch Goal
To merge two sorted linked lists into a single sorted linked list, we can modify the zipLists function as follows:
```
def mergeLists(list1, list2):
    """
    Merges two sorted linked lists into a single sorted linked list.

    Args:
    - list1: First sorted linked list to be merged.
    - list2: Second sorted linked list to be merged.

    Returns:
    - A new sorted linked list that contains the merged nodes from the input lists.
    """

    dummy = Node(None)
    current = dummy

    while list1 and list2:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 or list2

    return LinkedList(dummy.next)

```

This function uses a dummy node to keep track of the head of the merged list, and iterates over both lists, comparing the values of their nodes and appending the smaller one to the merged list. The time complexity of this approach is O(n), where n is the total length of both lists, because we need to iterate over all the nodes. The space complexity is O(1), because we are not creating any new nodes, just rearranging the pointers.