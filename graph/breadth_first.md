## Problem Domain:

The problem involves implementing a breadth-first traversal algorithm for a graph. Given a graph, the task is to visit all its vertices in breadth-first order, starting from a given `start_vertex`.

## Visual:

Visual representation of a simple graph with vertices and edges.


## Algorithm:

1. Create an empty set `visited` to keep track of visited vertices.
2. Create an empty list `result` to store the vertices visited in breadth-first order.
3. Create a queue `to_visit` and add `start_vertex` to it.
4. Add `start_vertex` to the `visited` set.
5. While the `to_visit` queue is not empty:
   - Dequeue the front vertex from `to_visit` and set it as `current_vertex`.
   - Append the string representation of `current_vertex` to the `result` list.
   - For each neighbor `neighbor` of `current_vertex`:
     - If `neighbor` is not in `visited`:
       - Enqueue `neighbor` to `to_visit`.
       - Add `neighbor` to the `visited` set.
   - Increment `index` to process the next vertex in the queue.

6. Return the `result` list containing the vertices visited in breadth-first order.

## Big O:

- Time Complexity: The time complexity of the breadth-first traversal algorithm is O(V + E), where V is the number of vertices and E is the number of edges in the graph. In the worst case, we may need to visit all vertices and edges in the graph.
- Space Complexity: The space complexity is O(V), where V is the number of vertices. This is because we use additional space to store the `visited` set, `result` list, and `to_visit` queue.

