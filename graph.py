class BSGraph(object):
    
    def __init__(self, size):
        self.vertices = {} #dictionary to maintain distinct vertices
        self.verticesList = [0]*size
        self.size = size
        self.movies = [] #List of all movies
        self.actors = [] #List of all actors
        self.edges = [] # Adjacency Matrix
        self.first_call_displayMoviesOfActor = True
        self.first_call_displayActorsOfMovie = True
        self.first_call_findMovieRelation = True
        self.first_call_findMovieTransRelation = True

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
        
        with open('outputPS2.txt', 'w') as f:
            f.writelines([])
            
        temp_ls = []
        self.movies = []
        self.actors = []
        with open(filename, 'r') as f:
            for x in f:
                temp_ls = x.split('/')
                for idx, item in enumerate(temp_ls):
                    item = item.strip("\n").strip(" ")
                    count = len(self.verticesList) - self.verticesList.count(0)
                    if count < self.size:
                        self.add_vertex(count, item)
                        if idx == 0: # 1st item in the list represents movie
                            self.movies.append(item)
                            movieName = item
                        else: # except 1st item, all are actors
                            self.actors.append(item)
                            self.add_edge(movieName, item)
                    else:
                        return 'error' #Increase the size of graph and re-run
            
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
        with open('outputPS2.txt', 'a') as f:
            f.writelines(lines)
        
        return None
    
    def readPromptFile(self, filename):
        """This method reads prompt file for different case conditions"""
        
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('searchActor'):
                    self.displayMoviesOfActor(line[13:].
                                                      strip(" ").
                                                      strip("\n"))

                elif line.startswith('searchMovie'):
                    self.displayActorsOfMovie(line[13:].
                                                      strip(" ").
                                                      strip("\n"))
                    
                elif line.startswith('RMovies'):
                    movieA = line.split(':')[1].strip(" ").strip("\n")
                    movieB = line.split(':')[2].strip(" ").strip("\n")
                    self.findMovieRelation(movieA, movieB)
                
                elif line.startswith('TMovies'):
                    movieA = line.split(':')[1].strip(" ").strip("\n")
                    movieB = line.split(':')[2].strip(" ").strip("\n")
                    self.findMovieTransRelation(movieA, movieB)
            
        return None
    
    def displayMoviesOfActor(self, actor):
        """This method appends to outfile movies for the search actor 
        passed in prompts file"""
        
        lines_to_write = []
        
        # Below code is executed for first time call only
        if self.first_call_displayMoviesOfActor:
            lines_to_write.append("\n\n--------Function displayMoviesOfActor--------")    
            self.first_call_displayMoviesOfActor = False
        
        # Below code lists movies for the search Actor. If the actor is not 
        # found in list, then display error accordingly
        
        if self.vertices.get(actor, -1) != -1:
            lines_to_write.append("\n\nActor Name: "+ actor)
            lines_to_write.append("\nList of Movies:")
            for idx, item in enumerate(self.edges[self.vertices.get(actor)]):
                if item == 1:
                    lines_to_write.append("\n")
                    lines_to_write.append(list(self.vertices.keys())[list(
                            self.vertices.values()).index(idx)])
                else:
                    pass
        else:
            lines_to_write.append("\n\nActor Name: "+ actor+ " is not found in the list")
        
        # Write data to outfile
        with open('outputPS2.txt', 'a') as f:
            f.writelines(lines_to_write)

        return None
    
    def displayActorsOfMovie(self, movie):
        lines_to_write = []
        
        # Below code is executed for first time call only
        if self.first_call_displayActorsOfMovie:
            lines_to_write.append("\n\n--------Function displayActorsOfMovies--------")    
            self.first_call_displayActorsOfMovie = False
        
        # Below code lists movies for the search Actor. If the actor is not 
        # found in list, then display error accordingly
        if self.vertices.get(movie, -1) != -1:
            lines_to_write.append("\n\nMovie Name: "+ movie)
            lines_to_write.append("\nList of Actors:")
            for idx, item in enumerate(self.edges[self.vertices.get(movie)]):
                if item == 1:
                    lines_to_write.append("\n")
                    lines_to_write.append(list(self.vertices.keys())[list(
                            self.vertices.values()).index(idx)])
                else:
                    pass
        else:
            lines_to_write.append("\n\nMovie Name: "+ movie+ " is not found in the list")
        
        # Write data to outfile
        with open('outputPS2.txt', 'a') as f:
            f.writelines(lines_to_write)

        return None
    
    
    def findMovieRelation(self, movieA, movieB):
        """This method uses Depth-First-Search traversal to traverse the 
        graph and find relation between the passed 2 movie names"""
        
        lines_to_write = []
        
        if self.first_call_findMovieRelation:
            lines_to_write.append("\n\n--------Function findMovieRelation --------")
            self.first_call_findMovieRelation = False
        
        lines_to_write.append("\n\nMovie: "+movieA)
        lines_to_write.append("\nMovie: "+movieB)
        
        movieB_id = self.vertices.get(movieB)
        
        # Recursive call to dfs() method to get the complete traversal with
        # movieA node as root. Recursion call is made only if movieA is in list
        if self.vertices.get(movieA, -1) != -1:
            
            path = self.dfs(self.vertices.get(movieA), [])

            # Traverse path until movieB is found and return related Actor
            count = 0
            previous = -1
            for i in path:
                count += 1
                if i == movieB_id:
                    related = previous
                    final_count = count
                    continue
                previous = i
    
            # Two movies are related by an actor, hence, final count should be 3
            if final_count == 3:
                lines_to_write.append("\nRelated: Yes, "+ 
                                    list(self.vertices.keys())[
                                    list(self.vertices.values()).index(related)])
            else:
                lines_to_write.append("\nRelated: No")
        else:
            lines_to_write.append("\nRelated: Movie %s is not found" %movieA)
        
        # Write to output file
        with open('outputPS2.txt', 'a') as f:
            f.writelines(lines_to_write)
            
        return None
    
    def findMovieTransRelation(self, movieA, movieB):
        """This method uses Depth-First-Search traversal to traverse the 
        graph and find relation between the passed 2 movie names"""
        
        lines_to_write = []
        
        if self.first_call_findMovieTransRelation:
            lines_to_write.append("\n\n--------Function findMovieTransRelation --------")
            self.first_call_findMovieTransRelation = False
        
        lines_to_write.append("\n\nMovie: "+movieA)
        lines_to_write.append("\nMovie: "+movieB)
        
        movieB_id = self.vertices.get(movieB)
        
        # Recursive call to dfs() method to get the complete traversal with
        # movieA node as root. Recursion call is made only if movieA is in list
        if self.vertices.get(movieA, -1) != -1:
            path = self.dfs(self.vertices.get(movieA), [])
        
            traverse = ""
            final_path = ""
            
            # Traverse path until movieB is found and return final path
            for i in path:
                traverse += list(self.vertices.keys())[
                                    list(self.vertices.values()).index(i)] + " > "
                if i == movieB_id:
                    final_path = traverse[0:-3]
                    continue
            
            # If length of final path is 0, then there is no relation
            if len(final_path) > 0:
                lines_to_write.append("\nRelated: Yes, "+ final_path)
            else:
                lines_to_write.append("\nRelated: No")
        else:
            lines_to_write.append("\nRelated: Movie %s is not found" %movieA)
        
        # Write to outfile
        with open('outputPS2.txt', 'a') as f:
            f.writelines(lines_to_write)
            
        return None
    
    
    def dfs(self, vertex, path=[]):
        """This is a method defined which is called recursively to traverse 
        using Adjacency Matrix"""
        path += [vertex]
                
        for idx, neighbour in enumerate(self.edges[vertex]):
            if neighbour and idx not in path:
                path = self.dfs(idx, path)
        return path
               

if __name__ == "__main__":

    # Instantiate Graph object
    movAct = BSGraph(100)
    
    # Read input file. If error, then don't call further methods
    if movAct.readActMovfile("inputPS2.txt") is None:
        # List movies and actors in input file
        movAct.displayActMov()
        
        # Reads prompt file and executes multiple functions
        movAct.readPromptFile("promptsPS2.txt")
    else:
        print("The graph object is instantiated with smaller size \
              than the vertices expected. Increase the size and re-run")
        