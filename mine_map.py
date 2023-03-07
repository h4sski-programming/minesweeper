

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
        self.check_neighbors()
        
    def check_neighbors(self):
        # print(self.map)
        # print(type(self.map))
        for row in self.map:
            # print(row)
            # print(type(row))
            for cell in row:
                print(cell.position)
                self.check_cell_neighbors(cell.position)
    
    
    def check_cell_neighbors(self, position):
        # neighbor_matrix = [[-1, -1], [-1, 0], [-1, 1],
        #                   [0, -1], [0, 1],
        #                   [1, -1], [1, 0], [1, 1]]
        
        # # removing if row = 0
        # if position[0] == 0:
        #     for index, neighbor in enumerate(neighbor_matrix):
        #         if neighbor[0] < 0 :
        #             neighbor_matrix[index].pop
                    
        # # remving if row == last row
        # if position[0] == len(self.map):
        #     for index, neighbor in enumerate(neighbor_matrix):
        #         if neighbor[0] > len(self.map) :
        #             neighbor_matrix[index].pop
        
        # # removing if column == 0
        # if position[1] == 0:
        #     for index, neighbor in enumerate(neighbor_matrix):
        #         if neighbor[1] < 0 :
        #             neighbor_matrix[index].pop
        
        # # removing if column == last column
        # if position[1] == len(self.map):
        #     for index, neighbor in enumerate(neighbor_matrix):
        #         if neighbor[1] > len(self.map[0]) :
        #             neighbor_matrix[index].pop
        
        
        
        neighbor_matrix = []
        
        # x_min_max = [-1, 1]
        # y_min_max = [-1, 1]
        # if position[0] <= 0:
        #     x_min_max[0] = 0
        # if position[0] >= len(self.map)-1:
        #     x_min_max[1] = 0
            
        # if position[1] <= 0:
        #     y_min_max[0] = 0
        # if position[1] >= len(self.map[0])-1:
        #     y_min_max[1] = 0
        
        # for x in range(x_min_max[0], x_min_max[1]):
        #     for y in range(y_min_max[0], y_min_max[1]):
        #         neighbor_matrix.append((x, y))
        
        
        neighbor_border = {'row': {'min': -1, 'max': 1}, 
                           'column': {'min': -1, 'max': 1}}
        
        # rows
        if position[0] <= 0:
            neighbor_border['row']['min'] = 0
        if position[0] >= len(self.map)-1:
            neighbor_border['row']['max'] = 0
        
        # columns
        if position[1] <= 0:
            neighbor_border['column']['min'] = 0
        if position[1] >= len(self.map[0])-1:
            neighbor_border['column']['max'] = 0
        
        print(neighbor_border)
        
        for row in range(neighbor_border['row']['min'], neighbor_border['row']['max']):
            for column in range(neighbor_border['column']['min'], neighbor_border['column']['max']):
                print(f'row = {row}, column = {column}')
                # neighbor_matrix.append((row, column))
        
        print(neighbor_matrix)
        
        
    
    def draw_map(self):
        for r in range(self.rows):
            for c in range(self.columns):
                self.map[r][c].display_cell(self.ttk, self.frame)
    
    def update_map(self, position):
        self.map[position[0]][position[1]].display_cell(self.ttk, self.frame)