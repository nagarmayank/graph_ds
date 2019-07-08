class BSGraph(object):
    
    def __init__(self, size):
        self.vertices = {} #dictionary to maintain distinct vertices
        self.verticesList = [0]*size
        self.size = size
        self.movies = [] #List of all movies
        self.actors = [] #List of all actors
        self.edges = [] # Adjacency Matrix
        for i in range(size):
            self.edges.append([0 for i in range(size)])
    
    def add_vertex(self, vertex, id):
        
        '''This method is defined to add a new vertex to the graph. This also
        checks if the vertex is not present in graph and adds accordingly'''

        if vertex <= self.size-1:
            if id not in self.vertices.keys():
                self.vertices[id] = vertex
                self.verticesList[vertex] = id
        else:
            print("Cannot add any more vertex to the graph")
            return None
        
    def add_edge(self, v1, v2):
        
        '''This method adds an edge between two vertices of the graph. Since,
         this is an undirected graph, add vertices for both 
         from - to and to - from vertices'''
        
        frm = self.vertices[v1]
        to = self.vertices[v2]
        self.edges[frm][to] = 1
        self.edges[to][frm] = 1

        return None
        
    def readActMovfile(self, filename):
        
        '''This method reads the input file, parses movies and actors 
        and creates graph data structure. Each distinct movie and actor is a
        graph vertex and there is an edge if an actor has worked in the 
        specified movie'''
        
        temp_ls = []
        self.movies = []
        self.actors = []
        with open(filename, 'r') as f:
            for x in f:
                temp_ls = x.split('/')
                for idx, item in enumerate(temp_ls):
                    item = item.strip("\n").strip(" ")
                    count = len(self.verticesList) - self.verticesList.count(0)
                    self.add_vertex(count, item)
                    if idx == 0: # 1st item in the list represents movie
                        self.movies.append(item)
                        movieName = item
                    else: # except 1st item, all are actors
                        self.actors.append(item)
                        self.add_edge(movieName, item)
            
        return None
    
    def displayActMov(self):
        ''' This method is defined to list the movie names and actor list
        in a text output file'''
        
        # Create a list of all the line items to be written to the text file
        # and write using the above created list
        lines = []
        lines.append("--------Function displayActMov--------")
        lines.append("\nTotal number of movies: "+ 
                     str(len(list(set(self.movies)))))
        lines.append("\nTotal number of actors: "+ 
                     str(len(list(set(self.actors)))))
        
        lines.append("\nList of movies:\n")
        
        # Loop through all movies list and write to file
        for movie in list(set(self.movies)):
            lines.append(movie)
            lines.append("\n")
        
        lines.append("\n")
        lines.append("List of actors:\n")
        
        # Loop through all actors list and write to file        
        for actor in list(set(self.actors)):
            lines.append(actor)
            lines.append("\n")
        
        lines.append("--------------------------------------")
        
        # Open the file in write mode and write data using the list created
        with open('outputPS2.txt', 'w') as f:
            f.writelines(lines)
        
        return None

if __name__ == "__main__":
    movAct = BSGraph(100)
    movAct.readActMovfile("inputPS2.txt") # Read input file
    movAct.displayActMov() # List movies and actors in input file

#print(mov.vertices)
#print(mov.verticesList)
#print(mov.edges)