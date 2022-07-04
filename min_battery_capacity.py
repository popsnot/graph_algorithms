"""A distribution company is upgrading its delivery fleet to electric vehicles.
In doing so they have to determine the battery capacity required for vehicles.
The following factors must be considered:

1. The company has a single depot and it delivers to any location in the city that
is reachable from the depot.
2. A delivery vehicle can travel two units of distance for every 3 units of battery 
capacity (that is charged).
3. It is assumed that given a destination, the vehicle will always take a path with 
the shortest distance in order to go to the destination and come back.

A vehicle with a fully-charged battery must be able to make a trip from the depot
to any one location in the city and return to the depot with at least 25% charge
left in the battery.
"""
from math import inf
from math import ceil

def uw_adjacency_list(graph_str):
    """Creates an undirected, weighted graph adjacency list from the inputted
       graph string.
    """
    string = graph_str.split('\n')
    title = string[0].split()
    n = int(title[1])
    output = []
    for i in range(n):
        output.append([])
    for edge in string[1:-1]:
        edge = edge.split()
        first = int(edge[0])
        second = int(edge[1])
        weight = int(edge[2])
        output[first].append((second, weight))
        output[second].append((first, weight))
    return output


def next_vertex(in_tree, distance):
    """Helper function for Dijkstra's algorithm. Selects the next vertex to
       run the while loop (which checks its adjacent vertices to see if the
       any values in the current distance array can be reduced).
    """
    min_list = []
    for i in range(0, len(in_tree)):
        if in_tree[i] == False:
            min_list.append((distance[i], i))
    weight, index = min(min_list)
    return index


def dijkstra(adj_list, start):
    """Implementation of Dijkstra's algorithm given the adjacency list generated
       by my previous function. Returns a parent array and a distance array.
    """
    n = len(adj_list)
    in_tree = [False]*n  #array which tracks whether or node is in the spanning tree
    distance = [inf]*n  #the distance from each node to its parent
    parent = [None]*n  #the last node in the shortest path before the current node
    distance[start] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return parent, distance


def max_path(distance):
    """Returns a value related to the maximum distance that the vehicle will 
    have to travel, this will then be converted into the minimum battery capacity
    required."""
    all_inf = True
    for item in distance:
        if item != inf:
            all_inf = False
    if all_inf == True:
        return 0
    output = []
    for item in distance:
        if item != inf:
            output.append(item)
    return max(output)



def min_capacity(city_graph, depot_position):
    """Returns the minimum battery capacity required to travel from the processing
       depot to the furthest available location and back. The battery will have
       at least 25% charge remaining after the trip.
       Application of Dijkstra's algorithm.
       Author: Luka Foy
       Date: 4/7/22
    """
    adj = uw_adjacency_list(city_graph)
    distance = dijkstra(adj, depot_position)
    max_ = max_path(distance)
    capacity = max_*4
    return capacity