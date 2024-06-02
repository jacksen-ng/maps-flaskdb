import heapq

class Dijkstra():
    def __init__(self, graph):
        self.graph = graph
        self.distances = {node: float('infinity') for node in graph}
        self.visited = {node: False for node in graph}
        self.previous_nodes = {node: None for node in graph}
        self.queue = []
        self.path = []
    def calculate(self, start):
        self.distances[start] = 0
        heapq.heappush(self.queue, [0, start])
        while self.queue:
            current_distance, current_node = heapq.heappop(self.queue)
            if self.distances[current_node] < current_distance:
                continue
            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight
                if distance < self.distances[neighbor]:
                    self.distances[neighbor] = distance
                    self.previous_nodes[neighbor] = current_node
                    heapq.heappush(self.queue, [distance, neighbor])
        return self.distances, self.previous_nodes
    def get_path(self, start, end):
        while end:
            self.path.append(end)
            end = self.previous_nodes[end]
        return self.path[::-1]