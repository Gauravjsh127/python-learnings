
"""
BFS :  Use Queue

Source: 

https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
"""

class Graph: 
    # Constructor
    def __init__(self):

        # default dictionary to store grap
        self.graph = {} 
  
    # function to add an edge to graph
    def addEdge(self,u ,v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
        # Create a queue for BFS 
        queue = []   
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s) 
        visited[s] = True

        while queue:   
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) 
            print(s, end = " ") 
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
  
# Driver code 
  
# Create a graph given in 
# the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print(g.graph)

g.BFS(2) 