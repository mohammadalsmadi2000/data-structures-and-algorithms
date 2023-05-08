# Create a new PseudoQueue
from stack_queue_pseudo.stack_queue_pseudo import PseudoQueue
pq = PseudoQueue()

# Test enqueue method
pq.enqueue(10)
pq.enqueue(15)
pq.enqueue(20)
assert pq.stack1.items == [10, 15, 20]

# Test dequeue method
assert pq.dequeue() == 10
assert pq.stack1.items == []
assert pq.stack2.items == [20, 15]

# Test enqueue and dequeue in combination
pq.enqueue(25)
assert pq.dequeue() == 15
assert pq.stack1.items == []
assert pq.stack2.items == [20, 25]

# Test dequeue when both stacks are empty
assert pq.dequeue() == 20
assert pq.dequeue() == 25
assert pq.dequeue() == None
assert pq.stack1.items == []
assert pq.stack2.items == []
