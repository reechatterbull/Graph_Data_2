class Graph:
  def __init__(self,edges):
    self.edges = edges

    self.graph = {} #Creating empty graph dictionary
    for start,end in self.edges: #This is the syntax to go through all the elements of edges tuple
      if start in self.graph:
        self.graph[start].append(end)
      else:
        self.graph[start] = [end]

    #print("Graph dict:",self.graph)

  def get_paths(self,start,end,path=[]):  #This is a method to get all paths between a start and end
    path = path + [start]
    if start == end:
      return [path]

    if start not in self.graph:
      return []

    all_routes = []
    
    for node in self.graph[start]:
      if node not in path:
        #print("New Path:", path)
        new_path = self.get_paths(node,end,path)
        
        for i in new_path:
          all_routes.append(i)
    return all_routes 

  def shortest_path(self,start,end,path = []):
    path = path + [start]
    if start not in self.graph:
      return None

    if start == end:
      return path

    shortest_routes = []

    shortest_path = None
    for node in self.graph[start]:
      if node not in path:
        sp = self.shortest_path(node,end,path)
        if sp:
          if shortest_path == None or len(sp) < len(shortest_path):
            shortest_path = sp
    return shortest_path
            
    

    

    
if __name__ == '__main__':
  routes = [
    ("Mumbai","Paris"),
    ("Mumbai","Dubai"),
    ("Dubai","Paris"),
    ("Paris","New York"),
    ("Dubai","New York"),
    ("New York","Toronto"),
    ("Toronto","Vancouver")
  ]

route_graph = Graph(routes)

start = "Mumbai"
end = "New York"
print(route_graph.get_paths(start,end))
print("Shortest Path:",route_graph.shortest_path("Mumbai","New York"))
