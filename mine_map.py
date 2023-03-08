import math
from random import randint, random

from settings import Settings
from cell_mine import Cell_mine


class Mine_map():
    def __init__(self, ttk, frame) -> None:
        self.map = ()
        self.rows = Settings.rows
        self.columns = Settings.columns
        self.ttk = ttk
        self.frame = frame
        
    def generate_map(self):
        for r in range(self.rows):
            row = ()
            for c in range(self.columns):
                row += (Cell_mine(r, c),)
            self.map += (row,)
        # print(self.map)
        self.get_bombs()
        self.set_numders_near_bomb()
    
    
    def get_bombs(self):
        bomb_number = math.ceil(self.rows * self.columns * Settings.mines_ratio)
        for i in range(bomb_number):
            random_row = randint(0, self.rows - 1)
            random_column = randint(0, self.columns - 1)
            if self.map[random_row][random_column].value == 'b':
                i -= 1
                continue
            self.map[random_row][random_column].value = 'b'
    
    
    def set_numders_near_bomb(self):
        for row_temp in range(self.rows):
            for column_temp in range(self.columns):
                if self.map[row_temp][column_temp].value == 'b':
                    print(row_temp, column_temp)
                    self.check_cell_neighbors((row_temp, column_temp))
    
    
    def check_neighbors(self):
        # print(self.map)
        # print(type(self.map))
        for row in self.map:
            # print(row)
            # print(type(row))
            for column in row:
                # print(cell.position)
                self.check_cell_neighbors(column.position)
    
    
    def check_cell_neighbors(self, position):
        matrix = self.generate_neighbour_matrix(position=position)
        for n in matrix:
            if type(self.map[position[0] + n[0]][position[1] + n[1]].value) == type(0):
                self.map[position[0] + n[0]][position[1] + n[1]].value += 1
    
    
    def generate_neighbour_matrix(self, position):
        neighbor_matrix = []
        neighbor_border = {'row': {'min': -1, 'max': 1}, 
                           'column': {'min': -1, 'max': 1}}
        # rows
        if position[0] <= 0:
            neighbor_border['row']['min'] = 0
        if position[0] >= self.rows-1:
            neighbor_border['row']['max'] = 0
        # columns
        if position[1] <= 0:
            neighbor_border['column']['min'] = 0
        if position[1] >= self.columns-1:
            neighbor_border['column']['max'] = 0
        # print(neighbor_border)
        
        for row in range(neighbor_border['row']['min'], neighbor_border['row']['max']+1):
            for column in range(neighbor_border['column']['min'], neighbor_border['column']['max']+1):
                neighbor_matrix.append((row, column))
        
        # print(neighbor_matrix)
        return neighbor_matrix
        
    
    def draw_map(self):
        for r in range(self.rows):
            for c in range(self.columns):
                self.map[r][c].display_cell(self.ttk, self.frame)
    
    def update_map(self, position):
        self.map[position[0]][position[1]].display_cell(self.ttk, self.frame)