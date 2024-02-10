from grid import Grid
import matplotlib.pyplot as plt

# Assuming the Grid class has an attribute `state` that stores the grid's state
def visualize_grid(grid_object):
    """
    Visualize a Grid object using matplotlib.

    Parameters:
    -----------
    grid_object: An instance of the Grid class.
    """
    grid = grid_object.state  # Access the state of the grid
    m = len(grid)  # Number of rows
    n = len(grid[0]) if m > 0 else 0  # Number of columns

    fig, ax = plt.subplots()
    ax.set_xlim(0, n)
    ax.set_ylim(0, m)
    plt.gca().invert_yaxis()

    for x in range(n + 1):
        ax.axvline(x, color='black')
    for y in range(m + 1):
        ax.axhline(y, color='black')

    for i in range(m):
        for j in range(n):
            ax.text(j + 0.5, i + 0.5, str(grid[i][j]), va='center', ha='center')

    plt.xticks([])
    plt.yticks([])
    plt.show()


# Example grid
grid = Grid(2,4, [[1,2,3,4], [5,6,7,8]])

visualize_grid(grid)
