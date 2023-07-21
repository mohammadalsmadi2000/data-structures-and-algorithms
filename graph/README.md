# Graph

This is a simple implementation of a graph data structure in Python.
# graph-breadth-first
## Whiteboard
[Link to the BFS page](https://github.com/mohammadalsmadi2000/data-structures-and-algorithms/blob/main/graph/breadth_first.md)


## Whiteboard Process

### 1. Problem Domain

The problem is to implement a graph data structure with the following functionalities:

1. Add a vertex to the graph.
2. Add an edge between two vertices with a given weight.
3. Retrieve a collection of all vertices in the graph.
4. Retrieve the neighbors of a vertex.
5. Ensure that neighbors are returned with 6. the weight between vertices included.
7. Get the size of the graph, representing the number of vertices.

### 2. Algorithm
The graph is implemented using an adjacency list representation. The Graph class maintains a dictionary edj_list to store the vertices as keys and their corresponding edges as values.

### 3. Visual 
```
       A
  (5) / \ (3)
     B - C
``` 
In this example, the graph has three vertices: A, B, and C. The edges: `(A, B)` with weight `5` and `(A, C)` with weight `3`.

### Testing Approach
To test the functionality of the graph, we can use the pytest framework.


## Approach & Efficiency

The graph is implemented using an adjacency list representation. The `edj_list` dictionary is used to store the vertices as keys and their corresponding edges as values. The space complexity of this implementation is O(V + E), where V is the number of vertices and E is the number of edges.

- Adding a vertex takes O(1) time complexity.
- Adding an edge takes O(1) time complexity.
- Retrieving the vertices takes O(V) time complexity.
- Retrieving the neighbors of a vertex takes O(1) time complexity.
- Finding the size of the graph takes O(1) time complexity.

## Solution

To use this code, you need to have the `Edge` and `Vertices` classes defined in separate files. You can then create an instance of the `Graph` class and perform operations such as adding vertices, adding edges, retrieving vertices and neighbors, and getting the size of the graph.

Here's an example of how to use the code:

```python
from graph import Graph


graph = Graph()


vertex1 = graph.add_vertex("A")
vertex2 = graph.add_vertex("B")


graph.add_edge(vertex1, vertex2, 5)

vertices = graph.get_vertices()
print(vertices)  # Output: ['A', 'B']


neighbors = graph.get_neighbors(vertex1)
print(neighbors)  # Output: [Edge(vertex='B', weight=5)]


size = graph.size()
print(size)  # Output: 2
