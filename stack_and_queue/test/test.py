from stack_and_queue.stack_and_queue import Stack ,Queue 

def test_stack():
    # Test stack initialization
    s = Stack()
    assert s.is_empty() == True

    # Test pushing onto a stack
    s.push(1)
    assert s.peek() == 1
    assert s.is_empty() == False

    # Test pushing multiple values onto a stack
    s.push(2)
    s.push(3)
    assert s.peek() == 3

    # Test popping off the stack
    assert s.pop() == 3
    assert s.peek() == 2

    # Test emptying a stack after multiple pops
    s.pop()
    s.pop()
    assert s.is_empty() == True

    # Test calling pop or peek on empty stack raises exception
    try:
        s.pop()
        assert False
    except:
        assert True

    try:
        s.peek()
        assert False
    except:
        assert True


def test_queue():
    # Test queue initialization
    q = Queue()
    assert q.is_empty() == True

    # Test enqueueing into a queue
    q.enqueue(1)
    assert q.peek() == 1
    assert q.is_empty() == False

    # Test enqueueing multiple values into a queue
    q.enqueue(2)
    q.enqueue(3)
    assert q.peek() == 1

    # Test dequeueing out of a queue the expected value
    assert q.dequeue() == 1
    assert q.peek() == 2

    # Test peeking into a queue, seeing the expected value
    assert q.peek() == 2

    # Test emptying a queue after multiple dequeues
    q.dequeue()
    q.dequeue()
    assert q.is_empty() == True

    # Test calling dequeue or peek on empty queue raises exception
    try:
        q.dequeue()
        assert False
    except:
        assert True

    try:
        q.peek()
        assert False
    except:
        assert True
