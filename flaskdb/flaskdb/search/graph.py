from stack import Stack
from queue import Queue
from vertex import Vertex
import sys

class Graph():

    def __init__(self, maxsize):
        self.vertex_list = [None] * maxsize  # 頂点リスト
        self.adjacency_matrix = \
            [[0 for column in range(maxsize)] for row in range(maxsize)] # 隣接マトリクス（頂点間の関係を記述）
        self.number_vertexs = 0        # 全頂点数
        self.stack = Stack(maxsize)    # スタック（操作系）
        self.queue = Queue(maxsize)    # キュー（操作系）

    # 頂点を追加する
    def add_vertex(self, label):
        self.vertex_list[self.number_vertexs] = Vertex(label)
        self.number_vertexs += 1

    # エッヂを追加する
    def add_edge(self, start, end, weight = 1):
        self.adjacency_matrix[start][end] = weight  # 有向グラフ
        #self.adjacency_matrix[end][start] = weight  # 無向グラフの場合はコメントアウトを外す

    # 頂点の値を表示する
    def display_vertex(self, i):
        print(self.vertex_list[i].get_label(), end=" ")

    # マトリクスから頂点間の関係を取得する
    def get_adjacency_unvisite_vertex(self, i):
        for j in range(self.number_vertexs):
            if self.adjacency_matrix[i][j] >= 1 and self.vertex_list[j].was_visited() == False:
                return j
        return -1

    # 深さ優先探索を行う
    def depth_first_search(self):
        self.vertex_list[0].set_visited( True )
        self.display_vertex(0)
        self.stack.push(0)

        while not self.stack.is_empty():
            n = self.get_adjacency_unvisite_vertex( self.stack.peek() )
            if n == -1:
                self.stack.pop()
            else:
                self.vertex_list[n].set_visited( True )
                self.display_vertex(n)
                self.stack.push(n)
        self.clear()
    
    # 幅優先探索を行う
    def breadth_first_search(self):
        self.vertex_list[0].set_visited( True )
        self.display_vertex(0)
        self.queue.insert(0)
        rear = 0

        while not self.queue.is_empty():
            front = self.queue.remove()
            
            while True:
                rear = self.get_adjacency_unvisite_vertex( front )
                if rear == -1:
                    break
                self.vertex_list[ rear ].set_visited( True )
                self.display_vertex( rear )
                self.queue.insert( rear )
        self.clear()
    
    # 全リストをクリアする
    def clear(self):
        for i in range(self.number_vertexs):
            self.vertex_list[i].set_visited( False )
