from settings import Settings

class Cell_mine():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        self.clicked = False
        self.value = 0
        self.width = Settings.width
        
        
    def display_cell(self, ttk, frame):
        self.label = ttk.Label(frame, text=self.value, width=self.width)
        self.label.grid(row=self.position[0], column=self.position[1])
        
        self.btn = ttk.Button(frame, text='', width=self.width)
        self.btn['command'] = self.btn.destroy
        self.btn.grid(row=self.position[0], column=self.position[1])
