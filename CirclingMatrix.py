import numpy as np


class CirclingMatrix:
    def __init__(self, dimension):
        self.dimension = dimension
        self.matrix = np.zeros((dimension, dimension), dtype=int)
        self.filled = np.full((dimension+2, dimension+2), False)
        for i in range(len(self.filled)):
            for j in range(len(self.filled[0])):
                if i == 0 or j == 0 or i == dimension+1 or j == dimension+1:
                    self.filled[i][j] = True
        self.facing = "r"
        self.position = [0, 0]

    def turn_attempt(self):
        filled_position_row = self.position[0] + 1
        filled_position_col = self.position[1] + 1
        if self.facing == 'r' and self.filled[filled_position_row][filled_position_col+1]:
            self.facing = 'd'
        if self.facing == 'd' and self.filled[filled_position_row+1][filled_position_col]:
            self.facing = 'l'
        if self.facing == 'l' and self.filled[filled_position_row][filled_position_col-1]:
            self.facing = 'u'
        if self.facing == 'u' and self.filled[filled_position_row-1][filled_position_col]:
            self.facing = 'r'

    def fill(self):
        number = 1
        while number <= self.dimension ** 2:
            self.matrix[self.position[0]][self.position[1]] = number
            self.filled[self.position[0]+1][self.position[1]+1] = True
            number += 1
            self.turn_attempt()
            if self.facing == "r":
                self.position[1] += 1
            elif self.facing == 'd':
                self.position[0] += 1
            elif self.facing == 'l':
                self.position[1] -= 1
            elif self.facing == 'u':
                self.position[0] -= 1

    def print_matrix(self):
        for row in self.matrix:
            for number in row:
                print(number, end="\t")
            print()


mat = CirclingMatrix(18)
mat.fill()
mat.print_matrix()