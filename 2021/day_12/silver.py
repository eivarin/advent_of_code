from aocd import get_data
lns = get_data(day=11, year=2021).splitlines()
# f = open("input.txt")
# lns = f.read().splitlines()


# Python program to print all paths from a source to destination.
  
from collections import defaultdict
  
# This class represents a directed graph
# using adjacency list representation
class Graph:
  
    def __init__(self):
        # No. of vertices
        self.V = 0
         
        # default dictionary to store graph
        self.graph = defaultdict(set)
        self.result = []
  
    # function to add an edge to graph
    def addEdge(self, u, v):
        if u not in self.graph:
            self.V += 1
        if v not in self.graph:
            self.V += 1
        self.graph[v].add(u)
        self.graph[u].add(v)

  
    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path):
        result = []
        # Mark the current node as visited and store in path
        path.append(u)
 
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            self.result.append(path.copy())
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i]== False:
                    self.printAllPathsUtil(i, d, visited, path)
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False
  
  
    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):
 
        # Mark all the vertices as not visited
        visited =[False]*(self.V)
 
        # Create an array to store paths
        path = []
 
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)
        return self.result
  
  
  
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)
  

s = 2 ; d = 3
paths = g.printAllPaths(s, d)
print(paths)