
import numpy as np
import matplotlib.pyplot as plt
import time

def initialize_board(size):
    """
    Initialize a 2D board with random values.
    
    Args:
    size (int): The size of the board.
    
    Returns:
    np.ndarray: A 2D numpy array representing the board.
    """
    return np.random.choice([0, 1], size=(size, size))

def count_neighbors(board, x, y):
    """
    Count the number of live neighbours for a cell at position (x, y).
    
    Args:
    board (np.ndarray): The game board.
    x (int): The x-coordinate of the cell.
    y (int): The y-coordinate of the cell.
    
    Returns:
    int: The number of live neighbours.
    """
    size = board.shape[0]
    count = 0
    for i in range(max(0, x-1), min(size, x+2)):
        for j in range(max(0, y-1), min(size, y+2)):
            count += board[i, j]
    count -= board[x, y]
    return count

def next_generation(board):
    """
    Compute the next generation of the game.
    
    Args:
    board (np.ndarray): The current game board.
    
    Returns:
    np.ndarray: The next generation of the game.
    """
    size = board.shape[0]
    next_board = np.copy(board)
    for i in range(size):
        for j in range(size):
            live_neighbors = count_neighbors(board, i, j)
            if board[i, j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    next_board[i, j] = 0
            else:
                if live_neighbors == 3:
                    next_board[i, j] = 1
    return next_board

def draw_board(board):
    """
    Draw the game board using matplotlib.
    
    Args:
    board (np.ndarray): The game board.
    """
    plt.imshow(board, cmap='binary')
    plt.draw()
    plt.pause(0.1)
    plt.clf()

def game_of_life(size, generations):
    """
    Run the game of life for a specified number of generations.
    
    Args:
    size (int): The size of the game board.
    generations (int): The number of generations to run.
    """
    board = initialize_board(size)
    for i in range(generations):
        draw_board(board)
        board = next_generation(board)

# Run the game of life
game_of_life(50, 100)