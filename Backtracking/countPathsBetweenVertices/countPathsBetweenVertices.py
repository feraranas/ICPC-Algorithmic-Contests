class Graph:

     def __init__(self, V):
          self.V = V
          self.adj = [[] for i in range(V)]
     
     def addEdge(self, u, v):
          # Add v to u's list
          self.adj[u].append(v)
     
     # Returns count of paths from 's' to 'd'
     def countPaths(self, s, d):

          # Mark all the vertices as not visited
          visited = [False] * self.V

          # Call the recursive helper function to print all paths
          pathCount = [0]

          self.countPathsUtil(s, d, visited, pathCount)
          
          return pathCount[0]
     
     def countPathsUtil(self, s, d, visited, pathCount):

          visited[s] = True

          # If current vertex is same as destination, then increment count
          if (s == d):
               pathCount[0] += 1
          
          # If current vertex is not destination
          else:
               # Recursion for all the vertices adjacent to current vertex
               i = 0
               while i < len(self.adj[s]):
                    if (not visited[self.adj[s][i]]):
                         self.countPathsUtil(self.adj[s][i], d, visited, pathCount)
                    i += 1
          
          visited[s] = False


if __name__ == '__main__':
     g = Graph(4)
     g.addEdge(0, 1)
     g.addEdge(0, 2)
     g.addEdge(0, 3)
     g.addEdge(2, 0)
     g.addEdge(2, 1)
     g.addEdge(1, 3)

     s = 2
     d = 3

     print(g.countPaths(s, d))