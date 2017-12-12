from Graph import *

class GraphManager:
    def __init__(self):
        self.graph = Graph()
        self.avaible_park = []
        self.unavaible_park = []
        self.exit = []

    def setGraph(self, mat , list_park , list_exit):
        #always update the map when modify the map.
        list_all_goal = list_goal + list_exit
        self.avaible_park = list_park
        self.exit = list_exit
        self.graph.setGraph(mat, [x + 1 for x in list_all_goal])

    def getPath(self, A, B , status):
        #return list of path from start node to destination
        path_list = self.graph.getPath(A + 1, B + 1, status)
        return [x - 1 for x in path_list]

    def printNode(self):
        self.graph.printAllNode()
    
        
