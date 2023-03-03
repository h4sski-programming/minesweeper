

class Cell_mine():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.clicked = False
        self.value = 0
        
    def click(self):
        self.clicked = True
        
    