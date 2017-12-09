class Graph:
    def __init__(self):
        self.adj_mat = [];

    def setGraph(self, mat):
        #also update h(n) using updateHeuristic()
        pass

    def updateHeuristic(self):
        #generate heuristic (update every times that Map has been modified)
        #update to prolog fact(heuristic.p)
        pass

    def markGraph(self, Node, status):
        #change mark status re-vise adj_mat
        pass    

    def getPath(self, A , B):
        #implement !!! A*!!!  use prolog  -genarate fact from adj_mat
        #findpath.p
        #return list of path from start node to destination
        pass

    def printHeuristic(self):
        #use to debug
        pass

    def printAllNode(self):
        #use to debug
        pass
