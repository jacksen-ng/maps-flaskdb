class Vertex():
    def __init__(self, label):
        self.label = label
        self.visited = False

    def get_label(self):
        return self.label

    def was_visited(self):
        return self.visited

    def set_visited(self, visited):
        self.visited = visited
