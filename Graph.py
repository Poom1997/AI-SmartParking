from pyswip import Prolog

class Graph:
    def __init__(self):
        self.adj_mat = []
        self.heuristic_dict = {}
        self.goal = []

    def setGraph(self, mat, goal):
        # set inital matrix at first.
        self.adj_mat = mat
        self.updateGraph()
        self.setGoal(goal)
        self.updateHeuristic()

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

    def setGoal(self, goalList):
        self.goal = goalList
        
    def updateHeuristic(self):
        #generate heuristic (update every times that Map has been modified)
        #update to dictionary (ready to use)
        self.heuristic_dict = {}
        for Node in self.goal:
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

    def getPath(self, A , B ,status):
        #implement !!! A*!!!  use prolog  -genarate fact from adj_mat
        #findpath.p
        #return list of path from start node to destination
        #generate assert H(n) first
        list_heuristic = self.heuristic_dict['n' + str(B)]
        f= open("manhattan.pl","w")
        fact_buffer = ""
        for i in list_heuristic:
            temp_manhattan = i.split(':')
            fact_buffer += "manhattan(" + temp_manhattan[0]+ "," +temp_manhattan[1] + ").\n"
        f.write(fact_buffer)
        f.close()
        
        p = Prolog()
        p.consult("node.pl")
        p.consult("astar.pl")
        p.consult("manhattan.pl")
        result = p.query("astar(n" + str(A) + ',n' + str(B) + ",Result).")

        if (status == 'enter'):
            for i in range(len(self.adj_mat)):
                if (self.adj_mat[i][B-1] == 1):
                    self.adj_mat[i][B-1] = 2
        else:
            for i in range(len(self.adj_mat)):
                if (self.adj_mat[i][A-1] == 2):
                    self.adj_mat[i][A-1] = 1
        self.updateGraph()
        path_list = []
        
        try:
            for i in list(result)[0]['Result']:
                path_list.append(str(i)[1:])
        except:
            return []
        return [int(x) for x in path_list]
    
    def getHeuristic(self, Node):
        return self.heuristic_dict['n' + str(Node)]
 
    def printAllNode(self):
        for i in range(0, len(self.adj_mat)):
            for j in range(0, len(self.adj_mat[i])):
                print(self.adj_mat[i][j], end = "  ")
            print()
              
        
