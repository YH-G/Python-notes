graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

visited = []

def dfs(graph, start):
    visited.append(start)
    
    for nxt in graph[start]:
        if nxt not in visited:
            dfs(graph, nxt)
    return visited

dfs(graph, 'A')