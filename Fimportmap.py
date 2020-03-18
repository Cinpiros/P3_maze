#loading map importe et formate la carte sous forme de tableau

class LoadingMap:
    #récupération de la taille de la carte et import de la carte depuis ressource/MapMaze.txt
    def __init__(self, t_map):
        self.map_height = t_map
        try:
            read_map = open("ressource/MapMaze.txt", "r")
            self.mapstr = read_map.readlines()
            read_map.close()

        except IOError:
            print("error load map")

    # création d'un tableau et formatage a l'intérieur de la carte importer
    def ep_map(self):
        self.map = [[0 for i in range(self.map_height)] for j in range(self.map_height)]
        ct2 = 0
        for line in self.mapstr:
            ct1 = 0
            line.rstrip('\n')
            for sp in line:
                self.map[ct2][ct1] = sp
                ct1 = ct1 + 1
                if ct1 == self.map_height:
                    break
            ct2 = ct2 + 1
            if ct2 == self.map_height:
                break
        return self.map