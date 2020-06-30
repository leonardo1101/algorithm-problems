def find_cycle(graph):
  visited = [] 
  current_graphs = graph
  while current_graphs:
    new_graphs = {}
    nodes = current_graphs.keys()
    for node in nodes:
      if node in visited:
        return True
      else:
        visited.append(node)
        for child_node in current_graphs[node]:
          new_graphs[child_node] = current_graphs[node][child_node]
    current_graphs = new_graphs
  return False

graph = {
  'a': {'a2':{}, 'a3':{} },
  'b': {'b2':{}},
  'c' : {}
}
print find_cycle(graph)
# False
graph['c'] = graph
print find_cycle(graph)
# True
