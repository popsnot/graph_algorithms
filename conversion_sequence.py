import collections
from math import inf

def du_adjacency_list(graph_str):
    """Creates a directed - unweighted graph adjacency list from the inputted
       graph string.
       The graph string is a description of the graph, number of nodes
       and a list of its edges.
    """
    string = graph_str.split('\n')
    title = string[0].split()
    n = int(title[1])
    output = []
    for i in range(n):
        output.append([])
    for edge in string[1:-1]:
        edge = edge.split()
        output[int(edge[0])].append((int(edge[1]), None))
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


def format_sequence(converters_info, source_format, destination_format):
    """Returns the fastest sequence in which video files can be converted, given
       the sequence of converters available. Uses Dijkstra's algorithm.
       Author: Luka Foy
       Date: 22/6/22
    """
    if source_format == destination_format:
        return [source_format]
    output = [source_format]
    temp = []
    adj_list = du_adjacency_list(converters_info)
    parent, distance = dijkstra(adj_list, source_format)
    current = destination_format
    if parent[current] == None:
        return "No solution!"
    while current != source_format:
        temp.append(current)
        placeholder = current
        if parent[current] == None:
            return "No solution!"
        current = parent[current]
    for item in reversed(temp):
        output.append(item)
    return output