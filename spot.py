import pygame

# RGB Color Codes
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:
    """
    Class Definition of Spot in Grid
    """
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    # get position of the spot
    def get_pos(self):
        return self.row, self.col

    # to check if spot is closed 
    def is_closed(self):
        return self.color == RED

    # to check if spot is opened
    def is_open(self):
        return self.color == GREEN

    # to check if spot is barrier
    def is_barrier(self):
        return self.color == BLACK

    # to check if spot is starting position
    def is_start(self):
        return self.color == ORANGE

    # to check if spot is starting position
    def is_end(self):
        return self.color == TURQUOISE

    # to reset the spot position
    def reset(self):
        self.color = WHITE

    # to set the starting position
    def make_start(self):
        self.color = ORANGE

    # to set the closed position
    def make_closed(self):
        self.color = RED

    # to set the opened position
    def make_open(self):
        self.color = GREEN

    # to set the barrier position
    def make_barrier(self):
        self.color = BLACK

    # to set the ending position
    def make_end(self):
        self.color = TURQUOISE

    # to set the path spot
    def make_path(self):
        self.color = PURPLE

    # draw the path
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    # update the neighbouring positions
    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
