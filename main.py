class Graph:
  def __init__(self,edges):
    self.edges = edges

    self.graph = {} #Creating empty graph dictionary
    for start,end in self.edges: #This is the syntax to go through all the elements of edges tuple
      if start in self.graph:
        self.graph[start].append(end)
      else:
        self.graph[start] = [end]

    print("Graph dict:",self.graph)

  def get_paths(self):  #This is a method to get paths 
      

  
    
  






if __name__ == '__main__':
  routes = [
    ("Mumbai","Paris"),
    ("Mumbai","Dubai"),
    ("Paris","Dubai"),
    ("Paris","New York"),
    ("New York","Toronto"),
    ("Toronto","Vancouver")
  ]

route_graph = Graph(routes)
