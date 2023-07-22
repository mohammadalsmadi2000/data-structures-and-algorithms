# Business Trip Algorithm

## Problem Description

Given a graph representing direct flights and their costs between cities, and an array of city names representing a business trip itinerary, the task is to determine whether the trip is possible with direct flights and calculate the total cost of the trip if possible.

## Class: Graph

### Properties

- `graph`: A dictionary representing the graph, where keys are city names, and values are dictionaries representing direct flight routes and their costs.

### Methods

1. `__init__(self)`: Initializes an empty graph.

2. `add_edge(self, C1, C2, cost)`: Adds a direct flight route between city `C1` and city `C2` with the given `cost` to the graph.

3. `direct_flight(self, C1, C2)`: Checks if there is a direct flight between city `C1` and city `C2`. Returns `True` if a direct flight exists, otherwise `False`.

4. `flight_cost(self, C1, C2)`: Returns the cost of the direct flight between city `C1` and city `C2`.

## Function: business_trip(graph, path)

### Parameters

- `graph`: An instance of the `Graph` class representing the flight routes and costs between cities.

- `path`: An array of city names representing the business trip itinerary.

### Returns

- `total_cost`: The total cost of the trip if it's possible with direct flights, otherwise `None`.

## Algorithm

1. Initialize `total_cost` to 0.

2. Iterate through the `path` array from index 0 to `len(path) - 1`:

   a. Get the current city and the next city from the `path`.

   b. Check if there is a direct flight between the current city and the next city using the `direct_flight` method of the `graph`.

   c. If there is no direct flight, return `None` as the trip is not possible.

   d. If there is a direct flight, add the cost of the flight between the current city and the next city to `total_cost`.

3. After iterating through the entire itinerary, return the `total_cost`.

## Big O
Time complexity of the business_trip function is linear time O(N)

Space complexity : O(N)