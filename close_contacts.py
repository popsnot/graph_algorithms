import collections
from math import inf

def recursive_dfs(output, vertex, discovered, adjacent):
    """Recursive implementation of Depth First Search algorithm.
       Author: Luka Foy
    """
    discovered[vertex] = True
    output.append(vertex)
    for adj in adjacent[vertex]:
        if discovered[adj] == False:
            output = recursive_dfs(output, adj, discovered, adjacent)
    return output

def uu_adjacency_list(graph_str):
    """Given the graph string of an unweighted, undirected graph, returns an
       adjacency list for use in a Graph Traversal algorithm.
    """
    string = graph_str.split('\n')
    title = string[0].split()
    n = int(title[1])
    output = []
    for i in range(n):
        output.append([])
    for line in string[1:-1]:
        line = line.split()
        output[int(line[0])].append(int(line[1]))
        output[int(line[1])].append(int(line[0]))
    return output

def bubbles(physical_contact_info):
    """Determines from a graph whether people (nodes) should be placed
       within the same bubble, based on their contact with others (edges).
       Uses the Depth First Search run off an adjacency list.
       Author: Luka Foy
       Date: 29/06/22
    """
    adj_list = uu_adjacency_list(physical_contact_info)
    n = len(adj_list)
    discovered = [False]*n
    output = []
    for i in range(n):
        if discovered[i] == False:
            dfs_output = []
            output.append(recursive_dfs(dfs_output, i, discovered, adj_list))
    return output
