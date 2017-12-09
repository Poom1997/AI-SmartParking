from pyswip import Prolog

class Graph:
    def __init__(self):
        #testing matrix 9 node
        self.adj_mat = [[0,1,0,1,0,0,0,0,0],
                        [1,0,1,0,0,0,0,0,0],
                        [0,1,0,0,0,1,0,0,0],
                        [1,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,1,0,0,0,0,0,1],
                        [0,0,0,1,0,0,0,1,0],
                        [0,0,0,0,0,0,1,0,1],
                        [0,0,0,0,0,1,0,1,0]];
        self.heuristic_dict = {}

    def setGraph(self, mat):
        # set inital matrix at first.
        pass

    def updateGraph(self):
        #also update h(n) using updateHeuristic()
        Fact_list = []
        for i in range(0, len(self.adj_mat)):
            for j in range(0, len(self.adj_mat[i])):
                if(self.adj_mat[i][j] == 1):
                    fact = "node(n" + str(i + 1) + ", n" + str(j + 1) + ",1)."
                    Fact_list.append(fact)
                    
        f= open("node.pl","w")
        fact_buffer = ""
        for i in Fact_list:
            fact_buffer += i + "\n"
        f.write(fact_buffer)
        f.close()
           

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

    def printHeuristic(self , Node):
        #use to debug
        destination = str(Node)
        p = Prolog()
        p.consult("node.pl")
        p.consult("heuristic.pl")
        result = p.query("heuristic(n" + destination + ",Result)")
        dict_hn = list(result)[0]
        
        #token to dict
        buffer_list = []
        for i in range(len(dict_hn['Result'])):
            temp_list = (str(dict_hn['Result'][i])).split(',')
            buffer_list.append(str(temp_list[0])[2:] + ":" + str(int(temp_list[1])))
        self.heuristic_dict['n' + str(Node)] = buffer_list
        print(self.heuristic_dict)
        
    def printAllNode(self):
        #use to debug
        for i in range(0, len(self.adj_mat)):
            for j in range(0, len(self.adj_mat[i])):
                print(self.adj_mat[i][j], end = "  ")
            print()
                
        
