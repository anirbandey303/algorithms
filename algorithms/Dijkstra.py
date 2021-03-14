import sys

class Graph():

  def __init__(self,vertices):
    self.V = vertices
    self.graph = [[0 for col in range(self.V)] for row in range(self.V)]

  def printPath(self,distances):
    for node in range(self.V):
      print(node, "costs", distances[node])
  
  def minDistanceVertex(self,isVisited,distances):
    minimum = sys.maxsize
    for vertex in range(self.V):
      if(distances[vertex] < minimum and isVisited[vertex] == False):
        minimum = distances[vertex]
        index = vertex
    return index

  def dijkstra(self, start):
    distances = [sys.maxsize] * self.V
    distances[start] = 0
    isVisited = [False] * self.V

    for node in range(self.V):
      u = self.minDistanceVertex(isVisited, distances)
      isVisited[u] = True

      for v in range(self.V):
        if(self.graph[u][v] > 0 and isVisited[v] == False and distances[v] > distances[u] + self.graph[u][v]):
          distances[v] = distances[u] + self.graph[u][v]
    
    self.printPath(distances)

g = Graph(9)

g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)
