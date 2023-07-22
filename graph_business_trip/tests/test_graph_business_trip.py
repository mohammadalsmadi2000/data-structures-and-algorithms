import pytest
from graph_business_trip.graph_business_trip import Graph, business_trip

@pytest.fixture
def sample_graph():
    graph = Graph()
    graph.add_edge("Metroville", "Pandora", 82)
    graph.add_edge("Arendelle", "New Monstropolis", 42)
    graph.add_edge("Arendelle", "Naboo", 70)
    graph.add_edge("New Monstropolis", "Naboo", 73)
    return graph

def test_business_trip_possible(sample_graph):
    assert business_trip(sample_graph, ["Metroville", "Pandora"]) == 82
    assert business_trip(sample_graph, ["Arendelle", "New Monstropolis", "Naboo"]) == 115

def test_business_trip_not_possible(sample_graph):
    assert business_trip(sample_graph, ["Naboo", "Pandora"]) == None
    assert business_trip(sample_graph, ["Narnia", "Arendelle", "Naboo"]) == None

def test_business_trip_empty_itinerary(sample_graph):
    assert business_trip(sample_graph, []) == 0

def test_business_trip_single_city(sample_graph):
    assert business_trip(sample_graph, ["Naboo"]) == 0

def test_business_trip_unconnected_cities(sample_graph):
    assert business_trip(sample_graph, ["Naboo", "New Monstropolis"]) == None

def test_business_trip_unknown_cities(sample_graph):
    assert business_trip(sample_graph, ["Agrabah", "Atlantica"]) == None
