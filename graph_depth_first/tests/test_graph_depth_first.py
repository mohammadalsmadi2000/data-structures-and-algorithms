import pytest
from graph_depth_first.graph_depth_first import Graph

@pytest.fixture
def create_graph():
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'G')
    g.add_edge('C', 'D')
    g.add_edge('C', 'E')
    g.add_edge('E', 'H')
    g.add_edge('D', 'F')
    return g

def test_depth_first_traversal(create_graph):
    g = create_graph
    start_node = 'A'
    traversal_result = g.depth_first(start_node)
    assert traversal_result == ['A', 'C', 'E', 'H', 'D', 'F', 'B', 'G']

def test_depth_first_empty_graph():
    g = Graph()
    start_node = 'A'
    traversal_result = g.depth_first(start_node)
    assert traversal_result == ['A']

def test_depth_first_single_node_graph():
    g = Graph()
    g.add_edge('A', 'A')
    start_node = 'A'
    traversal_result = g.depth_first(start_node)
    assert traversal_result == ['A']

def test_depth_first_isolated_nodes(create_graph):
    g = create_graph
    g.add_edge('X', 'Y')  
    g.add_edge('Z', 'Z')  
    start_node = 'X'
    traversal_result = g.depth_first(start_node)
    assert traversal_result == ['X', 'Y']

def test_depth_first_invalid_start_node(create_graph):
    g = create_graph
    start_node = 'InvalidNode'
    traversal_result = g.depth_first(start_node)
    assert traversal_result == []
