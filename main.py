from tkinter import *
from tkinter import ttk

from settings import Settings
from map import Map
from mine_map import Mine_map

settings = Settings()

class Main():
    def __init__(self) -> None:
        # self.running = True
        self.window = Tk()
        self.window.title('Minesweeper')

        self.frame = ttk.Frame(self.window, padding=10)
        self.frame.grid()

        input_value = StringVar()
        ttk.Label(self.frame, text='Hello h4sski').grid(column=0, row=0)
        ttk.Button(self.frame, text='Quit', command=self.window.destroy).grid(column=0, row=1)
        # ttk.Entry(self.frame, textvariable=input_value).grid(column=0, row=2)

        self.main_loop()

    def create_map(self):
        self.mine_frame = ttk.Frame(self.window, padding=10)
        self.mine_frame.grid()

    # map = Map()
    # map.generate_new_map()
    # for i in range(settings.rows):
    #     for j in range(settings.columns):
    #         ttk.Button(mine_frame, text=map.mines[i][j], width=3).grid(row=i, column=j)

        self.map = Mine_map(ttk, self.mine_frame)
        self.map.generate_map()
        self.map.draw_map()
    
    
    # def update(self, position):
    #     self.map.update_map(position, ttk, self.mine_frame)
    
    
    def main_loop(self):
        self.create_map()
        # while self.window:
        self.window.mainloop()



if __name__ == '__main__':
    Main()