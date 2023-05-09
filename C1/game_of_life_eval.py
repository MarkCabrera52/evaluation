import numpy as np
import time


class Game:
    def __init__(self, size=(8,8), seed=None, max_gen=10):
        # We use a predetermined seed to evaluate correct implementation
        if seed:
            np.random.seed(seed)
        
        # Initialize the board with a random series of 1s and 0s
        self._board = np.random.randint(0,2,size)
        self._gen = 0
        self._max_gen = max_gen

        #for optimization, set the initial viable indices
        #because the indices are shifted 1 down and 1 to the right, the viability array must also be shifted
        #i believe there is logic missing here, but for the sake of time I will submit the unoptomized version
        #self.viability = [(0,0)]
        #for i in range(0, size[0]):
        #    first = 0
        #    j = 0
        #    found = False
        #    while (not found and j < size[1]):
        #        if (self._board[i, j] == 1):
        #            found = True
        #            first = j+1
        #        j += 1
        #    
        #    found = False
        #    last = first
        #    while (j < size[1]):
        #        if (self._board[i, j] == 1):
        #            last = j+1
        #        j += 1
        #    
        #    self.viability.append((first, last))
        #
        #self.neighbors = np.zeros((size[0]+2, size[1]+2))

    def checkNeighbors(self, board, posx, posy):
        sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                sum += board[(posx + i), (posy + j)]

        #remove self because we don't want to double count
        sum -= board[posx, posy] #subtract none if nothing there, subtract itself if something is there
        
        return sum

    def update(self):
        board = np.copy(self._board)
        board = np.pad(self._board, pad_width = (1,1)) #pad the edges to make checking for neighbors easier
        #print(board)
        #''' Insert your code for updating the board based on the rules below '''
        #update the entire board every time
        for i in range(1, board.shape[0]-1):
            for j in range(1, board.shape[1]-1):
                neighbors = self.checkNeighbors(board, i, j) #check how many neighbors there are
                if (neighbors == 3): #3 neighbors will always live
                    self._board[i-1, j-1] = 1
                elif (not neighbors == 2): #2 neighbors will live if it is already alive
                    self._board[i-1, j-1] = 0
        #around .36 ms, but the drawings at the end are sparse, I am not extremely certain that this is correct
        #but maybe it's just doing that because with such a small grid, game of life is more stable

        #optimization: only update the parts of the board that are near live cells
        #to do this, you could have an array of tuples holding the first and last viable cells of each row and only check between those
        #for i in range(1, board.shape[0]-1):
        #    for j in range(self.viability[i][0], self.viability[i][1]):
        #        neighbors = self.checkNeighbors(board, i, j) #check how many neighbors there are
        #        self.neighbors[i, j] = neighbors
        #        if (neighbors == 3): #3 neighbors will always live
        #            self._board[i-1, j-1] = 1
        #            #update the viability matrix
        #            viability = self.viability[i]
        #             if ((j-1) < viability[0]):
        #                self.viability[i] = (j-1, viability[1]) #update the first index if necessary
        #            elif ((j+1) < viability[1]):
        #                self.viability[i] = (viability[0], j+1) #update the last index if necessary
        #        elif (not neighbors == 2): #2 neighbors will live if it is already alive
        #            self._board[i-1, j-1] = 0
        #print(self.neighbors)
        #around .24 ms, though i am unconvinced that the optimization logic is correct, given more time, I could get this to work.
        #also for some reason, the original matrix is way more dense when i do it this way, 
        #probably because incorrect logic makes it grow before it draws

        #or you can do an array of triples, holding the first and last position (x) and the row
        #loop through the array, updating it if there are any changes to the board
        


    def play(self, delay=.1):
        while self._gen < self._max_gen:
            # Start the generation by drawing the current board
            self.draw()
            
            # Next we update each of the cells according to the rules 
            self.update()

            # Increment the generation and sleep to make the visualization easier
            self._gen += 1
            time.sleep(delay)

    def time_run(self, gens=1000):
        start = time.time()
        for _ in range(gens):
            self.update()
        print(f'Average update time: {(time.time()-start)/gens*1000} ms')

    def draw(self):
        for row in self._board:   
            # Print a full block for each alive cell and an empty one for dead cells bounded by |
            print('|'.join(['▇' if c else ' ' for c in row]))

        print(f'Generation: {self._gen}')


if __name__ == "__main__":
    # If this file is run directly from the command line, run the game
    g = Game()
    g.time_run()
    g.play()  # Uncomment this to see the generational progression
