from grid import Grid

class Solver():

    # TODO: implement this function (and remove the line "raise NotImplementedError").
    def __init__(self, grid):
        """
        Initializes the solver with a grid object.
        """
        self.grid = grid
    
    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        
        solution = []  # Initialize the list to store the swaps
        
        m, n = self.grid.m, self.grid.n
        
        # Iterate through each cell in the grid
        for i in range(m):
            for j in range(n):
                # Calculate the correct position for the current value
                correct_i = (self.grid.state[i][j] - 1) // n
                correct_j = (self.grid.state[i][j] - 1) % n
                
                # If the current cell is not in its sorted position
                if (i, j) != (correct_i, correct_j):
                    # Swap the current cell with the cell in its correct position
                    solution.append(((i, j), (correct_i, correct_j)))
                    self.grid.swap((i, j), (correct_i, correct_j))
        
        return solution

