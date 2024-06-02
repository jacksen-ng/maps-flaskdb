from graph import Graph

g = Graph(10)

g.add_vertex("S")   # 頂点リストを持つ配列index 0
g.add_vertex("A")   # 1
g.add_vertex("C")   # 2
g.add_vertex("B")   # 3
g.add_vertex("D")   # 4
g.add_vertex("G")   # 5
g.add_vertex("E")   # 6
g.add_vertex("F")   # 7
g.add_vertex("H")   # 8

g.add_edge(0, 1)    # 頂点同士の関係を記述
g.add_edge(0, 3)    #
g.add_edge(0, 4)    #
g.add_edge(1, 2)    #
g.add_edge(3, 6)    #
g.add_edge(3, 7)    #
g.add_edge(4, 2)    #
g.add_edge(4, 8)    #
g.add_edge(6, 4)    #
g.add_edge(6, 7)    #
g.add_edge(8, 5)    #
g.add_edge(8, 7)    #

print("Adjacency Matrix: ")
for am in g.adjacency_matrix:
    print(am)

print("Visits in breadth_first_search: ")
g.breadth_first_search()
print()

print("Visits in depth_first_search: ")
g.depth_first_search()
print()

#print("Visits in dijkstra: ")
#g.dijkstra(); 
#print()
