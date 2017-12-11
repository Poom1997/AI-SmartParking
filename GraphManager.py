from Graph import *

class GraphManager:
    def __init__(self):
        self.graph = Graph()

    def setGraph(self, mat , goal):
        #always update the map when modify the map.
        self.graph.setGraph(mat, [x + 1 for x in goal])

    def getPath(self, A, B , status):
        #return list of path from start node to destination
        path_list = self.graph.getPath(A + 1, B + 1, status)
        return [x - 1 for x in path_list]

    def printNode(self):
        self.graph.printAllNode()
    
        
