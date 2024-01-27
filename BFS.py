from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            current_node = queue.popleft()
            print(current_node, end=" ")

            if current_node in self.graph:
                for neighbor in self.graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

    def shortest_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            return None

        visited = set()
        queue = deque([(start, [start])])
        visited.add(start)

        while queue:
            current_node, path = queue.popleft()

            if current_node == end:
                return path

            if current_node in self.graph:
                for neighbor in self.graph[current_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
                        visited.add(neighbor)

      
        return None


g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'F')
g.add_edge('D', 'G')
g.add_edge('F', 'G')

print("BFS traversal:")
g.bfs('A')

print("\nShortest path from 'A' to 'G':")
shortest_path = g.shortest_path('A', 'G')
print(shortest_path if shortest_path is not None else "No path found")
