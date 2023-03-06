

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
        for r in self.map:
            for c in r:
                pass
        
    def draw_map(self):
        for r in range(self.rows):
            for c in range(self.columns):
                self.map[r][c].display_cell(self.ttk, self.frame)
    
    def update_map(self, position):
        self.map[position[0]][position[1]].display_cell(self.ttk, self.frame)