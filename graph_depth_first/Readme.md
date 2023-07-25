### Problem Domain:
The class `Graph` represents a simple directed graph. It allows adding edges between nodes and performing a depth-first traversal starting from a given node.
## Visual 

![Day28Example](https://github.com/mohammadalsmadi2000/data-structures-and-algorithms/assets/60603704/785f2d5e-e47f-42ac-a47b-68e5fa335e21)

### Algorithm:
1. Initialize an empty graph with an empty dictionary to store nodes and their adjacent nodes.
2. The `add_edge` method adds an edge between two nodes by creating an entry in the graph dictionary.
3. The `depth_first` method performs a depth-first traversal starting from the given `start` node and returns a list of nodes in their pre-order depth-first traversal order.
4. Check if the graph is empty. If it is, return a list containing only the `start` node as there are no other nodes to visit.
5. Check if the `start` node exists in the graph. If not, return an empty list since the `start` node is not part of the graph.
6. Initialize an empty stack `S1`, a list `result` to store the traversal order, and a set `visite` to keep track of visited nodes.
7. Start a loop that continues until the stack `S1` becomes empty.
8. Pop the last element from the stack and assign it to the variable `node`.
9. If the `node` is not in the `visite` set (not visited yet), mark it as visited by adding it to the `visite` set, append it to the `result` list, and push its unvisited neighbors onto the stack.
10. Continue this process until all nodes are visited.
11. Return the `result` list containing the depth-first traversal order.

### Big O Analysis:
- Time Complexity : O(V + E) 
- Space Complexity: O(V) 


