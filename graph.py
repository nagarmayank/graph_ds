class BSGraph(object):
    
    def __init__(self, size):
        self.edges = []
        for i in range(size):
            self.edges.append([0 for i in range(size)])
        self.vertices = {}
        self.verticesList = [0]*size
        self.size = size
    
    def add_vertex(self, vertex, id):
        if vertex <= self.size-1:
            if id not in self.vertices.keys():
                self.vertices[id] = vertex
                self.verticesList[vertex] = id
        else:
            print("Cannot add any more vertex to the graph")
            return None
        
    def add_edge(self, v1, v2):
        frm = self.vertices[v1]
        to = self.vertices[v2]
        self.edges[frm][to] = 1
        self.edges[to][frm] = 1
        return None
        
    def readActMovfile(self, filename):
        ls = []
        movies = []
        actors = []
        with open(filename, 'r') as f:
            for x in f:
                ls = x.split('/')
                for idx, item in enumerate(ls):
                    item = item.strip("\n").strip(" ")
                    count = len(self.verticesList) - self.verticesList.count(0)
                    self.add_vertex(count, item)
                    if idx == 0:
                        movies.append(item)
                        movieName = item
                        #movieIndex = count
                        #self.add_edge(item, item)
                    else:
                        actors.append(item)
                        self.add_edge(movieName, item)
            
        print(list(set(movies)))
        print(list(set(actors)))
        return None


mov = BSGraph(10)

mov.readActMovfile("inputPS2.txt")

#print(mov.edges)