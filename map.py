import math
from random import randint
from settings import Settings

settings = Settings()

class Map():
    
    def __init__(self) -> None:
        self.mines = []
        for i in range(settings.rows):
            row = []
            for j in range(settings.columns):
                row.append(0)
            self.mines.append(row)
        self.map_size = settings.rows * settings.columns
        self.mines_number = math.ceil(self.map_size * settings.mines_ratio)
    
    def generate_new_map(self):
        for i in range(self.mines_number):
            row = randint(0, settings.rows - 1)
            column = randint(0, settings.columns - 1)
            
            if self.mines[row][column] != 0:
                i = i - 1
                continue
            self.mines[row][column] = 'b'
            # self.add_bomb_nearby(row=row, column=column)
        self.set_numbers_into_cells()
        
    
    def get_neighbor_matrix(self, r, c):
        rows = []
        if r > 0:
            rows.append(-1)
        rows.append(0)
        if r < settings.rows - 1:
            rows.append(1)
            
        cols = []
        if c > 0:
            cols.append(-1)
        cols.append(0)
        if c < settings.columns - 1:
            cols.append(1)
        
        return_matrix = []
        for rw in rows:
            for cl in cols:
                if rw == 0 and cl == 0:
                    continue
                return_matrix.append([rw, cl])
                
        return return_matrix
    
    def check_neighbor(self, r, c):
        # edge_matrix = [[-1, -1], [-1, 0], [-1, 1],
        #                [0, -1], [0, 1],
        #                [1, -1], [1, 0], [1, 1]
        #                ]
        neighbor_matrix = self.get_neighbor_matrix(r, c)
        # print(f'Cell ({r}, {c})')
        # print(neighbor_matrix)
        for neighbor_cell in neighbor_matrix:
            # neighbor = self.mines[r + neighbor_cell[0]][c + neighbor_cell[1]]
            if self.mines[r + neighbor_cell[0]][c + neighbor_cell[1]] != 'b':
                self.mines[r + neighbor_cell[0]][c + neighbor_cell[1]] += 1
    
    def set_numbers_into_cells(self):
        
        for i in range(settings.rows):
            for j in range(settings.columns):
                if self.mines[i][j] == 'b':
                    self.check_neighbor(i, j)
            
    
    # def add_bomb_nearby(self, row, column):
        
    #     # TODO: make edge values check to not take cells out of the matrix
        
    #     rows_to_be_checked = []
    #     if row > 0:
    #         rows_to_be_checked.append(-1)
    #     rows_to_be_checked.append(0)
    #     if row < settings.rows - 1:
    #         rows_to_be_checked.append(1)
            
    #     columns_to_be_checked = []
    #     if column > 0:
    #         columns_to_be_checked.append(-1)
    #     columns_to_be_checked.append(0)
    #     if column < settings.columns - 1:
    #         columns_to_be_checked.append(1)
        
    #     edge_matrix = []
    #     for r in rows_to_be_checked:
    #         for c in columns_to_be_checked:
    #             edge_matrix.append([r, c])
    #     print(f'Cell ({row}, {column})')
    #     # print(edge_matrix)
        
    #     # edge_matrix = [[-1, -1], [-1, 0], [-1, 1],
    #     #                [0, -1], [0, 1],
    #     #                [1, -1], [1, 0], [1, 1]
    #     #                ]
        
    #     for edge_cell in edge_matrix:
    #         cell = self.mines[row + edge_cell[0]][column + edge_cell[1]]
    #         if cell != 'b':
    #             cell += 1
            
            
    