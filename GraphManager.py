from Graph import *
from pyswip import Prolog

class GraphManager:
    def __init__(self):
        self.graph = Graph()
        self.avaible_park = []
        self.unavaible_park = []
        self.exit = []
        
    def setGraph(self, mat , list_park , list_exit):
        #always update the map when modify the map.
        list_all_goal = list_park + list_exit
        self.avaible_park = list_park
        self.exit = list_exit
        self.graph.setGraph(mat, [x + 1 for x in list_all_goal])

    def getPath(self, A, B , status):
        #return list of path from start node to destination
        path_list = self.graph.getPath(A + 1, B + 1, status)
        return [x - 1 for x in path_list]  

    def park(self, node):
        #park nearest exit (use prolog)
        if(self.avaible_park == []):
            return []
        heuristic_exit_list = []
        park_node = 0
        for i in self.exit:
            heuristic_exit_list += self.graph.getHeuristic(i + 1)
    
        f = open("park.pl","w")
        fact_list = ""
        for fact in heuristic_exit_list:
            fact_buffer = fact.split(':')
            if(int(fact_buffer[0][1:]) - 1 in self.avaible_park):
                fact_list += ('park(' + fact_buffer[0] + ',' + fact_buffer[1] + ').\n')
        f.write(fact_list)
        f.close()
        
        if fact_list == "":
            return []
        
        p = Prolog()
        p.consult("park.pl")
        p.consult("utility.pl")
        result = p.query("parknode(" + str(['n' + str(x+1) for x in self.avaible_park]).replace('\'',"") + ",Result).")
        park_node = str(list(result)[0]['Result'])
        #update avaible and unavbaible park list
        path_list = self.getPath(node ,int(park_node[1:]) - 1 ,'enter')
        self.avaible_park.remove(int(park_node[1:]) - 1)
        self.unavaible_park.append(int(park_node[1:]) - 1)
        return path_list

    def autoexit(self, node):
        #exit at nearest exit (use prolog)
        if(node not in self.unavaible_park):
            return []
        
        heuristic_exit_list = []
        heuristic_list = []
        exit_node = 0
        heuristic_list = self.graph.getHeuristic(node + 1)
        
        for i in heuristic_list:
            if (int(i.split(':')[0][1:])-1 in self.exit):
                heuristic_exit_list.append(i)
    
        f = open("exit.pl","w")
        fact_list = ""
        for fact in heuristic_exit_list:
            fact_buffer = fact.split(':')
            if(int(fact_buffer[0][1:]) - 1 in self.exit):
                fact_list += ('exit(' + fact_buffer[0] + ',' + fact_buffer[1] + ').\n')
        f.write(fact_list)
        f.close()
        if fact_list == "":
            return []
        
        p = Prolog()
        p.consult("exit.pl")
        p.consult("utility.pl")
        result = p.query("exitnode(" + str(['n' + str(x+1) for x in self.exit]).replace('\'',"") + ",Result).")
        exit_node = str(list(result)[0]['Result'])
        self.avaible_park.append(node)
        self.unavaible_park.remove(node)
        path_list = self.getPath(node ,int(exit_node[1:]) - 1,'exit')
        return path_list

    def manual_exit(self, node, exit_node):
        if(node not in self.unavaible_park or exit_node not in self.exit):
            return []
        self.avaible_park.append(node)
        self.unavaible_park.remove(node)
        return self.getPath(node ,exit_node ,'exit')
                

    def printNode(self):
        self.graph.printAllNode()

    def getLenPark(self):
        return len(self.avaible_park)
        
