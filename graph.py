class BSGraph(object):
    
    def __init__(self, size):
        self.edges = []
        for i in range(size):
            self.edges.append([0 for i in range(size)])
        self.vertices = {}
        self.verticesList = [0]*size
        self.size = size
        self.movies = []
        self.actors = []
    
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
        self.movies = []
        self.actors = []
        with open(filename, 'r') as f:
            for x in f:
                ls = x.split('/')
                for idx, item in enumerate(ls):
                    item = item.strip("\n").strip(" ")
                    count = len(self.verticesList) - self.verticesList.count(0)
                    self.add_vertex(count, item)
                    if idx == 0:
                        self.movies.append(item)
                        movieName = item
                        #movieIndex = count
                        #self.add_edge(item, item)
                    else:
                        self.actors.append(item)
                        self.add_edge(movieName, item)
            
        #print(list(set(movies)))
        #print(list(set(actors)))
        return None
    
    def displayActMov(self):
        ''' This method is defined to list the movie names and actor list
        in a text output file'''
        
        lines = []
        lines.append("--------Function displayActMov--------")
        lines.append("\nTotal number of movies: "+ 
                     str(len(list(set(self.movies)))))
        lines.append("\nTotal number of actors: "+ 
                     str(len(list(set(self.actors)))))
        
        lines.append("\nList of movies:\n")
        
        for movie in list(set(self.movies)):
            lines.append(movie)
            lines.append("\n")
        
        lines.append("\n")
        lines.append("List of actors:\n")
        
        for actor in list(set(self.actors)):
            lines.append(actor)
            lines.append("\n")
        
        lines.append("--------------------------------------")
        
        with open('outputPS2.txt', 'w') as f:
            f.writelines(lines)
        
        return None
    
            
mov = BSGraph(100)

mov.readActMovfile("inputPS2.txt")
mov.displayActMov()

#print(mov.vertices)
#print(mov.verticesList)
#print(mov.edges)