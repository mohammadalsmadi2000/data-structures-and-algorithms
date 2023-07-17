from graph import Graph

def test_add_vertex():
    graph = Graph()
    vertex = graph.add_vertex("A")
    assert vertex.value == "A"
    assert len(graph.get_vertices()) == 1

def test_add_edge():
    graph = Graph()
    vertex1 = graph.add_vertex("A")
    vertex2 = graph.add_vertex("B")
    graph.add_edge(vertex1, vertex2, 5)
    neighbors = graph.get_neighbors(vertex1)
    assert len(neighbors) == 1
    assert neighbors[0][0] == vertex2  
    assert neighbors[0][1] == 5

def test_get_vertices():
    graph = Graph()
    vertex1 = graph.add_vertex("A")
    vertex2 = graph.add_vertex("B")
    vertices = graph.get_vertices()
    assert len(vertices) == 2
    assert vertex1 in vertices
    assert vertex2 in vertices

def test_get_neighbors():
    graph = Graph()
    vertex1 = graph.add_vertex("A")
    vertex2 = graph.add_vertex("B")
    vertex3 = graph.add_vertex("C")
    graph.add_edge(vertex1, vertex2, 5)
    graph.add_edge(vertex1, vertex3, 3)
    neighbors = graph.get_neighbors(vertex1)
    assert len(neighbors) == 2
    assert neighbors[0][0] == vertex2
    assert neighbors[0][1] == 5
    assert neighbors[1][0] == vertex3
    assert neighbors[1][1] == 3

def test_neighbors_with_weight():
    graph = Graph()
    vertex1 = graph.add_vertex("A")
    vertex2 = graph.add_vertex("B")
    graph.add_edge(vertex1, vertex2, 5)
    neighbors = graph.get_neighbors(vertex1)
    assert len(neighbors) == 1
    assert neighbors[0][0] == vertex2
    assert neighbors[0][1] == 5

def test_size():
    graph = Graph()
    vertex1 = graph.add_vertex("A")
    vertex2 = graph.add_vertex("B")
    assert graph.size() == 2
    graph.add_edge(vertex1, vertex2, 5)
    assert graph.size() == 2

def test_graph_with_one_vertex_and_edge():
    graph = Graph()
    vertex1 = graph.add_vertex("A")
    graph.add_edge(vertex1, vertex1, 10)
    edges = graph.get_neighbors(vertex1)
    assert len(edges) == 2
    assert edges[0][0] == vertex1
    assert edges[0][1] == 10
    assert edges[1][0] == vertex1
    assert edges[1][1] == 10


def test_breadth_first():
    graph = Graph()

  
    pandora = graph.add_vertex("Pandora")
    arendelle = graph.add_vertex("Arendelle")
    metroville = graph.add_vertex("Metroville")
    monstroplolis = graph.add_vertex("Monstroplolis")
    narnia = graph.add_vertex("Narnia")
    naboo = graph.add_vertex("Naboo")

    
    graph.add_edge(pandora, arendelle, 4)
    graph.add_edge(pandora, metroville, 7)
    graph.add_edge(arendelle, metroville, 3)
    graph.add_edge(arendelle, monstroplolis, 8)
    graph.add_edge(metroville, monstroplolis, 6)
    graph.add_edge(metroville, narnia, 2)
    graph.add_edge(metroville, naboo, 5)
    graph.add_edge(monstroplolis, naboo, 9)
    graph.add_edge(narnia, naboo, 10)

    
    result = graph.breadth_first(pandora)
    expected_output = ["Pandora", "Arendelle", "Metroville", "Monstroplolis", "Narnia", "Naboo"]

    assert result == expected_output