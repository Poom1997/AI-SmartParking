from pyswip import Prolog

class GridController:
    def __init__(self):
        self.unavaible_list = []

    def lockGrid(self,grid):
        self.unavaible_list.append(list(grid))

    def unlockGrid(self,grid):
        for unavaible in self.unavaible_list:
            if (grid[0] == unavaible[0]) and (grid[1] == unavaible[1]):
                self.unavaible_list.remove(unavaible)
                break

    def isLock(self,grid):
        #use prolog to check
        p = Prolog()
        p.consult("utility.pl")
        result = p.query('isLock('+ str(list(grid)) + ',' + str(self.unavaible_list) + ').')
        if (list(result) != []):
            return True
        return False
    
