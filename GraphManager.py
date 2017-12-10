from Graph import *

class GraphManager:
    def __init__(self):
        self.graph = Graph()

    def setGraph(self, mat):
        #always update the map when modify the map.
        self.graph.setGraph(mat)

    def getPath(self, A, B):
        #return list of path from start node to destination
        path_list = self.graph.getPath(A , B)
        return path_list

    def printNode(self):
        self.graph.printAllNode()
    
        
