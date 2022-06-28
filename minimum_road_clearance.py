"""A heavy snow has caused road closures in the city. The first priority is to 
make sure all locations in the city are safely reachable and connected to each 
other so that essential services can be provided. The goal is to clear the least 
amount of road surface so that all locations are reachable.
"""

from math import inf
def uw_adjacency_list(graph_str):
    """Creates an udirected - weighted graph adjacency list from the inputted
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
    """Helper function for Prim's algorithm. Selects the next vertex to
       run the while loop (which checks its adjacent vertices to see if the
       any values in the current distance array can be reduced)."""
    min_list = []
    for i in range(0, len(in_tree)):
        if in_tree[i] == False:
            min_list.append((distance[i], i))
    weight, index = min(min_list)
    return index


def prim(adj, start):
    """Implementation of Prim's algorithm, used to find a
       minimum spanning tree from a given adjacency list.
    """
    n = len(adj)
    in_tree = [False]*n
    distance = [inf]*n
    parent = [None]*n
    distance[start] = 0
    while not all(in_tree):
        current = next_vertex(in_tree, distance)
        in_tree[current] = True
        for vert, weight in adj[current]:
            if not in_tree[vert] and weight < distance[vert]:
                distance[vert] = weight
                parent[vert] = current
    return parent, distance


def road_segments(city_map):
    """Returns the road segments that correspond to the minimum amount of road
       surface that must be cleared to allow all locations in the city are
       reachable.
       """
    output = []
    adj_list = uw_adjacency_list(city_map)
    parent, distance = prim_imp(adj_list, 0)
    for i in range(1, len(parent)):
        checker = []
        checker.append(parent[i])
        checker.append(i)
        checker.sort()
        output.append((checker[0], checker[1]))
    return output